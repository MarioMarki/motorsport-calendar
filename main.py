from Series import F1
from Series import MotoGP
import ics
sessions_f1 = F1.get_session()
sessions_motoGP = MotoGP.get_session()
with open("ICS Files/F1.ics", "w",encoding="utf-8") as ics_file:
    ics_file.write(f"{ics.header}\n")
    for session in sessions_f1:
        ics_file.write(f"{ics.event_block(**session)}\n")
    ics_file.write(ics.footer)

with open("ICS Files/MotoGP.ics", "w",encoding="utf-8") as ics_file:
    ics_file.write(f"{ics.header}\n")
    for session in sessions_motoGP:
        ics_file.write(f"{ics.event_block(**session)}\n")
    ics_file.write(ics.footer)