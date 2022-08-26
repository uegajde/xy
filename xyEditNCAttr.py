# editNCAttr
# func: modify the netcdf file attribute
# cmd : xyEditNCAttr (path of netcdf file) (name of attribute) (valueType) (newValue)

import sys
from netCDF4 import Dataset

args = sys.argv
ncfilePath = args[1]
attrName = args[2]
valueType = args[3]
newValue = args[4]
ncfile = Dataset(ncfilePath, 'r+')

if valueType in ('int', 'integer', 'INT', 'INTEGER', 'i', 'I'):
    newValue = int(newValue)
elif valueType in ('float', 'real', 'FLOAT', 'REAL', 'f', 'F'):
    newValue = float(newValue)
elif valueType in ('bool', 'boolean', 'b', 'B'):
    if args[4] in ('True', 'true', '.True.', '.true.', '1'):
        newValue = True
    elif args[4] in ('False', 'false', '.False.', '.false.', '0'):
        newValue = False

ncfile.setncattr(attrName, newValue)
ncfile.close()
