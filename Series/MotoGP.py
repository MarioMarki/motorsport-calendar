import requests
from datetime import datetime,timezone

data = requests.get("https://api.pulselive.motogp.com/motogp/v1/events?seasonYear=2026").json()
LENGHTS = {
    "FP1":"PT45M",
    "PR":"PT1H",
    "FP2":"PT30M",
    "Q1":"PT15M",
    "Q2":"PT15M",
    "SPR":"PT20M",
    "RAC":"PT40M",
    "RAC2":"PT40M",
    "RAC3":"PT40M",
}
NAMES = {
    "Free Practice Nr. 1":"FP1",
    "Free Practice Nr. 2":"FP2",
    "Qualifying Nr. 1 ":"Q1",
    "Qualifying Nr. 2 ":"Q2",
    "Grand Prix":"Race"
}

def iso_to_ics_stamp(time):
    parsed_dt = datetime.fromisoformat(time)
    utc_dt = parsed_dt.astimezone(timezone.utc)
    result = utc_dt.strftime('%Y%m%dT%H%M%SZ')
    return result

def get_session():
    result = []
    for item in data:
        if item['kind'] == "GP":
            broadcast = item['broadcasts']
            for event in broadcast:
                if event['kind'] == "PRACTICE" or event['kind'] == "QUALIFYING" or event['kind'] == "RACE":
                    if event["category"]["acronym"] == "MGP":
                        duration = f"{LENGHTS.get(event['shortname'], 'PT1H')}"
                        uid = f"{event['id']}"
                        start = f"{iso_to_ics_stamp(event['date_start'])}"
                        title = f"{event['category']['name']} - {item['hashtag'].replace('#','')} - {NAMES.get(event['name'],event['name'])}"
                        summary = {
                            'uid': uid,
                            'start': start,
                            'duration': duration,
                            'title': title,
                        }
                        result.append(summary)
    return result

print(len(get_session()))