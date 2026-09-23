from Series.F1 import get_session
import ics
sessions = get_session()
with open("ICS Files/f1.ics", "w",encoding="utf-8") as ics_file:
    ics_file.write(f"{ics.header}\n")
    for session in sessions:
        ics_file.write(f"{ics.event_block(**session)}\n")
    ics_file.write(ics.footer)