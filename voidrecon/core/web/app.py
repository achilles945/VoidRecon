# voidrecon/core/web/app.py

from flask import Flask, jsonify, render_template, request, abort
from pathlib import Path
from voidrecon.core.base import Recon
import sqlite3

# Flask instance named FlaskApp to match voidrecon.py
FlaskApp = Flask(__name__, template_folder="templates", static_folder="static")

# Initialize Recon instance
recon = Recon()
recon.start()  # ensure default workspace exists

VALID_WS_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"

def is_valid_workspace(ws_name):
    return all(c in VALID_WS_CHARS for c in ws_name)

# -----------------------------
# Routes
# -----------------------------

@FlaskApp.route("/")
def index():
    return render_template("index.html")

@FlaskApp.route("/api/workspaces")
def api_workspaces():
    try:
        workspaces = recon.list_workspaces()
        return jsonify(workspaces)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@FlaskApp.route("/api/workspace/<workspace>/tables")
def api_tables(workspace):
    if not is_valid_workspace(workspace):
        abort(400, "Invalid workspace name")
    try:
        recon.switch_workspace(workspace)
        tables = [
            "domains", "companies", "netblocks", "locations", "vulnerabilities",
            "ports", "hosts", "contacts", "credentials", "leaks", "profiles",
            "repositories", "dashboard", "whois"
        ]
        return jsonify(tables)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@FlaskApp.route("/api/workspace/<workspace>/table/<table>")
def api_table_data(workspace, table):
    if not is_valid_workspace(workspace):
        abort(400, "Invalid workspace name")
    try:
        limit = int(request.args.get("limit", 200))
        recon.switch_workspace(workspace)
        rows = recon.get_data(table)
        if rows is None:
            rows = []

        recon.data_cur.execute(f"SELECT * FROM {table} LIMIT 1")
        col_names = [desc[0] for desc in recon.data_cur.description]

        result = [dict(zip(col_names, row)) for row in rows]
        return jsonify(result[:limit])
    except sqlite3.OperationalError:
        return jsonify({"error": f"Table '{table}' not found in workspace '{workspace}'"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@FlaskApp.route("/api/workspace/<workspace>/tasks")
def api_tasks(workspace):
    if not is_valid_workspace(workspace):
        abort(400, "Invalid workspace name")
    try:
        recon.switch_workspace(workspace)
        tasks = recon.get_tasks()
        columns = ["id","module","arguments","status","start_time","end_time"]
        tasks_dict = [dict(zip(columns, t)) for t in tasks]
        return jsonify(tasks_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
