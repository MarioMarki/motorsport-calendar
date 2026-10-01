from datetime import datetime,timezone
header = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//mario//motorsport//EN
CALSCALE:GREGORIAN"""
footer = """END:VCALENDAR"""
def event_block(uid,start,duration,title):
    return f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:20260824T120000Z
DTSTART:{start}
DURATION:{duration}
SUMMARY:{title}
BEGIN:VALARM
TRIGGER:-PT30M
ACTION:DISPLAY
DESCRIPTION:Session starting soon
END:VALARM
END:VEVENT"""
def iso_to_ics_stamp(time):
    parsed_dt = datetime.fromisoformat(time)
    utc_dt = parsed_dt.astimezone(timezone.utc)
    result = utc_dt.strftime('%Y%m%dT%H%M%SZ')
    return result

def write_calendar(sessions, path):
    with open(path, "w", encoding="utf-8") as ics_file:
        ics_file.write(f"{header}\n")
        for session in sessions:
            ics_file.write(f"{event_block(**session)}\n")
        ics_file.write(footer)