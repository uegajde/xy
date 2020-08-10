# scriptDone
# func: note a script done
# cmd : python scriptDone.py (path of xyFlowControl.nml) (name of script)

import f90nml
import sys
from datetime import datetime

args = sys.argv
xynml = f90nml.read(args[1])
scriptName = args[2]
nowTime = datetime.now()

xynml['xyFlowControl']['script'] = scriptName
xynml['xyFlowControl']['scriptdone'] = nowTime.strftime('%Y-%m-%d_%H:%M:%S')

xynml.write(args[1], force=True)
