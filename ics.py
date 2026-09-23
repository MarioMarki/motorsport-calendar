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