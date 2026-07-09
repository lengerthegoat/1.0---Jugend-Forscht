"""
Kleine Webseite + Datenbank fuer Messwerte.

Starten mit:  python webdatenbank.py
Dann im Browser: http://127.0.0.1:5000

Braucht: pip install flask
"""

import sqlite3

import numpy as np
from flask import Flask, request, redirect, jsonify, render_template_string

DB_DATEI = "messwerte.db"

app = Flask(__name__)


def get_verbindung():
    conn = sqlite3.connect(DB_DATEI)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_verbindung() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messwerte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                experiment TEXT NOT NULL,
                wert REAL NOT NULL
            )
        """)


def lade_als_array(experiment):
    """Laedt alle Werte einer Experiment-Gruppe als numpy-Array (fuer z.B. den Gaussian Process)."""
    with get_verbindung() as conn:
        rows = conn.execute(
            "SELECT wert FROM messwerte WHERE experiment = ? ORDER BY id",
            (experiment,),
        ).fetchall()
    return np.array([row["wert"] for row in rows])


SEITE = """
<!doctype html>
<html lang="de">
<head><meta charset="utf-8"><title>Messwerte</title></head>
<body style="font-family: sans-serif; max-width: 700px; margin: 2rem auto;">
    <h1>Messwerte eintragen</h1>
    <form method="post" action="/hinzufuegen">
        <label>Experiment: <input type="text" name="experiment" value="{{ letztes_experiment }}" required></label><br><br>
        <label>Wert: <input type="number" step="any" name="wert" required></label><br><br>
        <button type="submit">Hinzufügen</button>
    </form>

    <h2>Letzte Einträge</h2>
    <table border="1" cellpadding="6" style="border-collapse: collapse;">
        <tr><th>ID</th><th>Experiment</th><th>Wert</th></tr>
        {% for row in eintraege %}
        <tr>
            <td>{{ row["id"] }}</td>
            <td>{{ row["experiment"] }}</td>
            <td>{{ row["wert"] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route("/")
def start():
    with get_verbindung() as conn:
        eintraege = conn.execute(
            "SELECT * FROM messwerte ORDER BY id DESC LIMIT 50"
        ).fetchall()
    letztes_experiment = eintraege[0]["experiment"] if eintraege else ""
    return render_template_string(SEITE, eintraege=eintraege, letztes_experiment=letztes_experiment)


@app.route("/hinzufuegen", methods=["POST"])
def hinzufuegen():
    experiment = request.form["experiment"]
    wert = float(request.form["wert"])
    with get_verbindung() as conn:
        conn.execute(
            "INSERT INTO messwerte (experiment, wert) VALUES (?, ?)",
            (experiment, wert),
        )
    return redirect("/")


@app.route("/api/messwerte/<experiment>")
def api_messwerte(experiment):
    return jsonify(lade_als_array(experiment).tolist())


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
