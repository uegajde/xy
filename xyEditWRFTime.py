# editWRFTime
# func: update start, end and run time in namelist.input (for WRF)
# cmd : python editWRFTime.py (path of namelist.input) (startTime) (endTime) (timeFormat)

import f90nml
import sys
from datetime import datetime
from datetime import timedelta

args = sys.argv
WRFnml = f90nml.read(args[1])
startTime = datetime.strptime(args[2], args[4])
endTime = datetime.strptime(args[3], args[4])

# read domain number
dmLen = len(WRFnml['time_control']['start_year'])

# update start/end time
for iDM in range(0, dmLen):
    WRFnml['time_control']['start_year'][iDM] = startTime.year
    WRFnml['time_control']['start_month'][iDM] = startTime.month
    WRFnml['time_control']['start_day'][iDM] = startTime.day
    WRFnml['time_control']['start_hour'][iDM] = startTime.hour
    WRFnml['time_control']['start_minute'][iDM] = startTime.minute
    WRFnml['time_control']['start_second'][iDM] = startTime.second
    WRFnml['time_control']['end_year'][iDM] = endTime.year
    WRFnml['time_control']['end_month'][iDM] = endTime.month
    WRFnml['time_control']['end_day'][iDM] = endTime.day
    WRFnml['time_control']['end_hour'][iDM] = endTime.hour
    WRFnml['time_control']['end_minute'][iDM] = endTime.minute
    WRFnml['time_control']['end_second'][iDM] = endTime.second

# update run time
runTime = endTime - startTime
runDays = runTime.days
runHours = runTime.seconds//3600
runMins = (runTime.seconds-runHours*3600)//60
runSecs = runTime.seconds-runHours*3600-runMins*60
WRFnml['time_control']['run_days'] = runDays
WRFnml['time_control']['run_hours'] = runHours
WRFnml['time_control']['run_minutes'] = runMins
WRFnml['time_control']['run_seconds'] = runSecs

# write nml
WRFnml.write(args[1], force=True, align=True)
