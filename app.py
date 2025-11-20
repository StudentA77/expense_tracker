import argparse
from utils.config import load_config
from utils.db import connect
import csv
from openpyxl import Workbook
from datetime import datetime

def init_db():
    cfg = load_config()
    conn = connect(cfg["database_path"])
    with open("database/schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    print("Database klaar.")

def add_category(name):
    cfg = load_config()
    conn = connect(cfg["database_path"])
    cur = conn.cursor()
    cur.execute("INSERT INTO category (name) VALUES (?)", (name,))
    conn.commit()
    print("Categorie toegevoegd.")

def add_expense(category_id, amount, description):
    cfg = load_config()
    conn = connect(cfg["database_path"])
    date = datetime.now().strftime("%Y-%m-%d")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expense (category_id, amount, description, date) VALUES (?, ?, ?, ?)",
        (category_id, amount, description, date)
    )
    conn.commit()
    print("Uitgave toegevoegd.")

def export_csv():
    cfg = load_config()
    conn = connect(cfg["database_path"])
    cur = conn.cursor()
    cur.execute("""
        SELECT e.id, c.name, e.amount, e.description, e.date
        FROM expense e JOIN category c ON e.category_id = c.id
    """)
    rows = cur.fetchall()

    with open("exports/report.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Categorie", "Bedrag", "Beschrijving", "Datum"])
        w.writerows(rows)

    print("CSV geëxporteerd.")

def export_excel():
    cfg = load_config()
    conn = connect(cfg["database_path"])
    cur = conn.cursor()
    cur.execute("""
        SELECT e.id, c.name, e.amount, e.description, e.date
        FROM expense e JOIN category c ON e.category_id = c.id
    """)
    rows = cur.fetchall()

    wb = Workbook()
    ws = wb.active
    ws.append(["ID", "Categorie", "Bedrag", "Beschrijving", "Datum"])
    for r in rows:
        ws.append(r)

    wb.save("exports/report.xlsx")
    print("Excel geëxporteerd.")

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("--name")
parser.add_argument("--category_id")
parser.add_argument("--amount")
parser.add_argument("--description")
args = parser.parse_args()

if args.command == "init-db":
    init_db()
elif args.command == "add-category":
    add_category(args.name)
elif args.command == "add-expense":
    add_expense(int(args.category_id), float(args.amount), args.description)
elif args.command == "export-csv":
    export_csv()
elif args.command == "export-excel":
    export_excel()
