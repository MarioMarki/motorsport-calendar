import json
import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

from ics import iso_to_ics_stamp

BASE_URL = "https://www.fiawec.com"

DURATIONS = {
    "Free Practice": "PT1H30M",
    "Qualifying":    "PT15M",
    "Hyperpole":     "PT12M",
    "Race":          "PT6H",
}

TIMEZONES = {
    "fuji":        "Asia/Tokyo",
    "sao-paulo":   "America/Sao_Paulo",
    "lone-star":   "America/Chicago",
    "qatar":       "Asia/Qatar",
    "bahrain":     "Asia/Bahrain",
    "silverstone": "Europe/London",
}


def wec_to_ics_stamp(time, link):
    for keyword, zone in TIMEZONES.items():
        if keyword in link:
            local = datetime.fromisoformat(time).replace(tzinfo=ZoneInfo(zone))
            return local.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    return iso_to_ics_stamp(time)


def get_session():
    result = []
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "lxml")
    seen_links = set()
    for link in soup.find_all("a", href=re.compile(r"^/en/race/[a-z0-9-]+-\d{4}$")):
        seen_links.add(link.get("href"))
    for link in seen_links:
        response2 = requests.get(BASE_URL + link)
        soup = BeautifulSoup(response2.text, "lxml")
        script_tag = soup.find("script", type="application/ld+json")
        if script_tag is None:
            continue
        data = json.loads(script_tag.get_text())
        for session in data.get("subEvent", []):
            if session["name"].startswith(tuple(DURATIONS)):
                duration = "PT1H"
                for prefix in DURATIONS:
                    if session["name"].startswith(prefix):
                        duration = DURATIONS[prefix]
                        break
                result.append({
                    "uid": session["@id"],
                    "start": wec_to_ics_stamp(session["startDate"], link),
                    "duration": duration,
                    "title": f"{data['name']} - {session['name'].rsplit(' - ', 1)[0]}",
                })
    return result