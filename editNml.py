# editNml
# func: operate "nml[field][varaible] = newValue"
# cmd : python editNml.py (path of nml) (field) (varaible) (newValue)
#
# warning:
# 1. only able to handle int/float/str/boolean, besides the three all treat as string
# 2. DO NOT support array

import f90nml
import sys

args = sys.argv
nml = f90nml.read(args[1])

oriValue = nml[args[2]][args[3]]
if type(oriValue) is int:
    nml[args[2]][args[3]] = int(args[4])
elif type(oriValue) is float:
    nml[args[2]][args[3]] = float(args[4])
elif type(oriValue) is bool:
    if args[4] in ('True', 'true', '.True.', '.true.', '1'):
        nml[args[2]][args[3]] = True
    elif args[4] in ('False', 'false', '.False.', '.false.', '0'):
        nml[args[2]][args[3]] = False
else:
    nml[args[2]][args[3]] = args[4]

nml.write(args[1], force=True, align=True)
