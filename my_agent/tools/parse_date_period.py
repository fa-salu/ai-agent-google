from datetime import datetime, timedelta
import re

def parse_date_period(user_input: str):
    text = user_input.lower()
    today = datetime.now().date()

    # explicit range
    if match := re.search(r"from (\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})", text):
        start = datetime.strptime(match.group(1), "%Y-%m-%d").date()
        end = datetime.strptime(match.group(2), "%Y-%m-%d").date()
        return start, end

    if "today" in text:
        return today, today
    if "yesterday" in text:
        return today - timedelta(days=1), today - timedelta(days=1)
    if "last week" in text or "past week" in text:
        return today - timedelta(days=7), today
    if "last month" in text or "past month" in text:
        return today - timedelta(days=30), today
    if match := re.search(r"(?:past|previous) (\d+) days?", text):
        days = int(match.group(1))
        return today - timedelta(days=days), today

    return today - timedelta(days=7), today 