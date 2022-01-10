# calTime
# func: operate time calculation
# cmd : xyCalTime (rawTime) (rawTimeFormat) (delta) (unit)
#
# rawTimeFormat: follow python's format
# supported unit: days,day,d / hours,hour,hr / minutes,minute,min / seconds/second/sec
# example: xyCalTime 2015-09-16_00:00:00 %Y-%m-%d_%H:%M:%S -3 hours

import sys
from datetime import datetime
from datetime import timedelta

args = sys.argv
rawTime = args[1]
rawTimeFormat = args[2]
delta = int(args[3])
unit = args[4]

if (unit == 'days') or (unit == 'day') or (unit == 'd'):
    timedeltaAmount = timedelta(delta)
elif (unit == 'hours') or (unit == 'hour') or (unit == 'hr'):
    timedeltaAmount = timedelta(0, delta*3600)
elif (unit == 'minutes') or (unit == 'minute') or (unit == 'min'):
    timedeltaAmount = timedelta(0, delta*60)
elif (unit == 'seconds') or (unit == 'second') or (unit == 'sec'):
    timedeltaAmount = timedelta(0, delta)
else:
    print('error in calTime: unspported unit', file=sys.stderr)
    timedeltaAmount = timedelta(0, 0)

rawTime = datetime.strptime(rawTime, rawTimeFormat)
newTime = rawTime + timedeltaAmount
print(newTime.strftime(rawTimeFormat))
