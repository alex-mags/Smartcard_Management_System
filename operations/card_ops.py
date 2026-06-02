import sqlite3
import json
from db.database import get_connection
#Defines add card subroutine
def add_card(card_number, holder_name, card_type, balance, issue_date, expiry_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cards (card_number, holder_name, card_type, balance, issue_date, expiry_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (card_number, holder_name, card_type, balance, issue_date, expiry_date))
    conn.commit()
    conn.close()
    print("Card added successfully.")

def amend_card(card_number, **kwargs):
    conn = get_connection()
    cursor = conn.cursor()
    for field, value in kwargs.items():
        cursor.execute(f"UPDATE cards SET {field} = ? WHERE card_number = ?", (value, card_number))
    conn.commit()
    conn.close()
    print("Card updated successfully.")

def remove_card(card_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cards WHERE card_number = ?", (card_number,))
    conn.commit()
    conn.close()
    print("Card removed successfully.")

def search_cards(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def export_to_json(filepath="data/export.json"):
    results = search_cards("SELECT * FROM cards")
    keys = ["id", "card_number", "holder_name", "card_type", "balance", "status", "issue_date", "expiry_date"]
    data = [dict(zip(keys, row)) for row in results]
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Exported {len(data)} cards to {filepath}")