from typing import List
import requests as _requests
import bs4 as _bs4

def _gen_url(month: str, day: int) -> str:
    # Page to work
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url

def _get_page(url: str) -> _bs4.BeautifulSoup:
    # Conversion to html format
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def events_of_the_day(month: str, day: int) -> List[str]:
    #Return the events of a given day
    url = _gen_url(month, day)
    page = _get_page(url)
    raw_events = page.find_all(class_="event")
    events = [event.text for event in raw_events]
    return events
    
events_of_the_day("february", 24)