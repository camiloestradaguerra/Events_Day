from typing import Dict
import json as _json

def get_all_events() -> Dict:
    with open("events.json") as events_file:
        data = _json.load(events_file)
    return data

def get_month_events(month: str) -> Dict:
    events = get_all_events()
    month = month.lower() 
    try: 
        month_events = events[month]
        return month_events
    except KeyError:
        return " this month isn't real you fool"

def get_day_events(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower() 
    try: 
        day_events = events[month][str(day)]
        return day_events
    except KeyError:
        return "what is wrong with you"
