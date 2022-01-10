# readWRFTime
# func: read start or ens time in WRF configuration file (namelist.input)
# cmd : xyReadWRFTime (path of namelist.input) timeFormat
# output: startTime or endTime
# seChoice: startTime or endTime
#
# timeFormat: follow python's format
# example: xyReadWRFTime ${mainDir}/namelist.input startTime %Y-%m-%d_%H:%M:%S

import f90nml
import sys
from datetime import datetime

args = sys.argv
wrfnml = f90nml.read(args[1])
seChoice = args[2]
timeFormat = args[3]

if seChoice == 'startTime':
    sYear = wrfnml['time_control']['start_year'][0]
    sMonth = wrfnml['time_control']['start_month'][0]
    sDay = wrfnml['time_control']['start_day'][0]
    sHour = wrfnml['time_control']['start_hour'][0]
    sMin = wrfnml['time_control']['start_minute'][0]
    sSec = wrfnml['time_control']['start_second'][0]
    time = datetime(
        year=sYear, month=sMonth, day=sDay, hour=sHour, minute=sMin, second=sSec, microsecond=0)
elif seChoice == 'endTime':
    eYear = wrfnml['time_control']['end_year'][0]
    eMonth = wrfnml['time_control']['end_month'][0]
    eDay = wrfnml['time_control']['end_day'][0]
    eHour = wrfnml['time_control']['end_hour'][0]
    eMin = wrfnml['time_control']['end_minute'][0]
    eSec = wrfnml['time_control']['end_second'][0]
    time = datetime(
        year=eYear, month=eMonth, day=eDay, hour=eHour, minute=eMin, second=eSec, microsecond=0)
else:
    time = datetime(
        year=9999, month=12, day=31, hour=0, minute=0, second=0, microsecond=0)

print(time.strftime(timeFormat))
