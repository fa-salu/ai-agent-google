 

import requests
import os
from my_agent.tools.parse_date_period import parse_date_period

BASE_URL = os.getenv("EXPENSE_API_URL", "http://127.0.0.1:5000/api/transactions")

def get_expense_summary():
    """Get overall expense summary (income, expense, balance)."""
    response = requests.get(f"{BASE_URL}/summary")
    return response.json()

def get_expense_by_category(category: str):
    """Get total and list of transactions for a given category."""
    response = requests.get(f"{BASE_URL}/by-category", params={"category": category})
    return response.json()

def get_expense_by_period(query: str):
    start, end = parse_date_period(query)
    response = requests.get(f"{BASE_URL}/by-date",
                            params={"start": start.isoformat(), "end": end.isoformat()})
    return response.json()