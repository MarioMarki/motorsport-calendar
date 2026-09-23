import requests
from datetime import datetime,timezone

data = requests.get("https://api.pulselive.motogp.com/motogp/v1/events?seasonYear=2026").json()
# i=0
# for item in data:
#     if item["kind"] == "GP":
#         broadcast = item["broadcasts"]
#         for event in broadcast:
#             if event["category"]["acronym"] == "MGP":
#                 if event["kind"] == "QUALIFYING" or event["kind"] == "RACE":
#                     i+=1
# print(i)

def iso_to_ics_stamp(time):
    parsed_dt = datetime.fromisoformat(time)
    utc_dt = parsed_dt.astimezone(timezone.utc)
    result = utc_dt.strftime('%Y%m%dT%H%M%SZ')
    return result