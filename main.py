from unittest import case

import requests
import json
data = requests.get("https://api.jolpi.ca/ergast/f1/2026.json").json()
races = data["MRData"]["RaceTable"]["Races"]
header = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//mario//motorsport//EN
CALSCALE:GREGORIAN"""
footer = """END:VCALENDAR"""

Sessions = ['FirstPractice','SecondPractice','ThirdPractice','SprintQualifying','Sprint','Qualifying','Race']
Lengths = {
    'FirstPractice':'PT1H',
    'SecondPractice':'PT1H',
    'ThirdPractice':'PT1H',
    'SprintQualifying':'PT44M',
    'Sprint':'PT44M',
    'Qualifying':'PT1H',
    'Race':'PT2H',
}
NAMES={
    'FirstPractice':'First Practice',
    'SecondPractice':'Second Practice',
    'ThirdPractice':'Third Practice',
    'SprintQualifying':'Sprint Qualifying',
}
def ics_stamp(date, time):
    date = date.replace("-","")
    time = time.replace(":","")
    return f"{date}T{time}"
def summary(race,session):
    name = NAMES.get(session, session)
    return f"F1 - {race} - {name}"
def event_block(race, session):
    ses = race.get(session)
    length = Lengths.get(session,"PT1H")
    return f"""BEGIN:VEVENT
UID:{race["season"]}-{race["round"]}-{session}
DTSTAMP:20260824T120000Z
DTSTART:{ics_stamp(ses['date'],ses['time'])}
DURATION:{length}
SUMMARY:{summary(race["raceName"],session)}
BEGIN:VALARM
TRIGGER:-PT30M
ACTION:DISPLAY
DESCRIPTION:Session starting soon
END:VALARM
END:VEVENT"""

blocks = []

for race in races:
    race["Race"] = {"date": race["date"], "time": race["time"]}
    for session in Sessions:
        ses = race.get(session)
        if ses:
            blocks.append(event_block(race, session))
print(len(blocks))
print(header+"\n"+"\n".join(blocks)+"\n"+footer)

with open("f1.ics","w",encoding="utf-8") as f:
    f.write(header+"\n"+"\n".join(blocks)+"\n"+footer)

#git config --global user.name "Your Name"
# git config --global user.email "your@email.com"