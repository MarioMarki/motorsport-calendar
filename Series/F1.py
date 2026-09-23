import requests
data = requests.get("https://api.jolpi.ca/ergast/f1/2026.json").json()
races = data["MRData"]["RaceTable"]["Races"]
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
    'Sprint':'Sprint',
    'Qualifying':'Qualifying',
    'Race':'Race',
}
def ics_stamp(date, time):
    date = date.replace("-","")
    time = time.replace(":","")
    return f"{date}T{time}"



def get_session():
    result = []
    for race in races:
        race["Race"] = {"date": race["date"], "time": race["time"]}
        for session in Sessions:
            ses = race.get(session)
            if ses:
                name = NAMES.get(session)
                uid = f'{race["season"]}-{race["round"]}-{session}'
                start = f'{ics_stamp(ses["date"],ses["time"])}'
                duration = f'{Lengths.get(session,"PT1H")}'
                title = f'F1 - {race["raceName"]} - {name}'
                summary = {
                    'uid' : uid,
                    'start' : start,
                    'duration' : duration,
                    'title' : title,
                }
                result.append(summary)
    return result
