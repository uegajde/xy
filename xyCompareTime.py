# compareTime
# func: operate time calculation
# cmd : xyCompareTime (time1) (time2) (timeFormat)
# output: 0 when time1 < time2
#         1 when time1 = time2
#         2 when time1 > time2
# example: xyCompareTime 2015-09-15_21:00:00 2015-09-15_21:02:00 %Y-%m-%d_%H:%M:%S

import sys
from datetime import datetime

args = sys.argv
time1 = datetime.strptime(args[1], args[3])
time2 = datetime.strptime(args[2], args[3])

if time1 < time2:
    print('0')
elif time1 == time2:
    print('1')
elif time1 > time2:
    print('2')
