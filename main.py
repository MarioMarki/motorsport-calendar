from Series import F1, MotoGP, WEC
import ics

ics.write_calendar(F1.get_session(), "ICS Files/F1.ics")
ics.write_calendar(MotoGP.get_session(), "ICS Files/MotoGP.ics")
ics.write_calendar(WEC.get_session(), "ICS Files/WEC.ics")