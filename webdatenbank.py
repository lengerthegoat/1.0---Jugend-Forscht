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
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Messwerte</title>
<style>
    :root {
        --akzent: #4f6df5;
        --hintergrund: #f4f6fb;
        --karte: #ffffff;
        --text: #1f2430;
        --text-schwach: #6b7280;
        --rand: #e5e7eb;
    }
    * { box-sizing: border-box; }
    body {
        font-family: "Segoe UI", system-ui, sans-serif;
        background: var(--hintergrund);
        color: var(--text);
        max-width: 720px;
        margin: 2.5rem auto;
        padding: 0 1rem;
    }
    h1 { font-size: 1.6rem; margin-bottom: 0.25rem; }
    h2 { font-size: 1.15rem; color: var(--text-schwach); margin-top: 2.5rem; }
    .karte {
        background: var(--karte);
        border: 1px solid var(--rand);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
    }
    form { display: flex; flex-wrap: wrap; gap: 1rem; align-items: end; }
    .feld { display: flex; flex-direction: column; gap: 0.35rem; flex: 1; min-width: 160px; }
    label { font-size: 0.85rem; color: var(--text-schwach); }
    input {
        padding: 0.55rem 0.7rem;
        border: 1px solid var(--rand);
        border-radius: 8px;
        font-size: 1rem;
    }
    input:focus { outline: 2px solid var(--akzent); border-color: transparent; }
    button {
        background: var(--akzent);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.3rem;
        font-size: 1rem;
        cursor: pointer;
    }
    button:hover { opacity: 0.9; }
    table { width: 100%; border-collapse: collapse; margin-top: 0.5rem; }
    th, td { text-align: left; padding: 0.6rem 0.7rem; font-size: 0.95rem; }
    th { color: var(--text-schwach); font-weight: 600; border-bottom: 2px solid var(--rand); }
    tr:not(:last-child) td { border-bottom: 1px solid var(--rand); }
    tr:hover td { background: #f9fafc; }
    .leer { color: var(--text-schwach); font-style: italic; padding: 1rem 0; }
</style>
</head>
<body>
    <h1>Messwerte</h1>
    <p style="color: var(--text-schwach); margin-top: 0;">Neue Messung eintragen und die letzten Einträge einsehen.</p>

    <div class="karte">
        <form method="post" action="/hinzufuegen">
            <div class="feld">
                <label for="experiment">Experiment</label>
                <input type="text" id="experiment" name="experiment" value="{{ letztes_experiment }}" required>
            </div>
            <div class="feld">
                <label for="wert">Wert</label>
                <input type="number" id="wert" step="any" name="wert" required>
            </div>
            <button type="submit">Hinzufügen</button>
        </form>
    </div>

    <h2>Letzte Einträge</h2>
    <div class="karte">
        {% if eintraege %}
        <table>
            <tr><th>ID</th><th>Experiment</th><th>Wert</th></tr>
            {% for row in eintraege %}
            <tr>
                <td>{{ row["id"] }}</td>
                <td>{{ row["experiment"] }}</td>
                <td>{{ row["wert"] }}</td>
            </tr>
            {% endfor %}
        </table>
        {% else %}
        <p class="leer">Noch keine Messwerte eingetragen.</p>
        {% endif %}
    </div>
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
