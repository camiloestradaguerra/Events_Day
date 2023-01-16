from typing import Iterator, Dict
import datetime as _dt
import json as _json

import scraper as _scraper

def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]:
    #print(start_date)
    #print(end_date)
    #delta_t = int((end_date-start_date).days)
    for n in range(0, int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n)
    #    print(start_date + _dt.timedelta(n))

def create_events_dict() -> Dict:
    events = dict()
    start_date = _dt.date(2020, 1, 10)
    end_date = _dt.date(2020, 1, 13)

    for date in _date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()

        events[month][date.day] = _scraper.events_of_the_day(month, date.day)

    return events

if __name__ == "__main__":
    events = create_events_dict()
    with open("events.json", mode='w') as events_file:
        _json.dump(events, events_file, ensure_ascii=False)
