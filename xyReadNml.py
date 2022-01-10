# readNml
# func: read nml[field][variable]
# cmd : xyReadNml (path of nml) (name of field) (name of variable)

import f90nml
import sys

args = sys.argv
xynml = f90nml.read(args[1])

varInNml = xynml[args[2]][args[3]]

print(varInNml)
