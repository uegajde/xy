#!/bin/bash

sourcePath="./"

pythonPath=$(which python)
pythonBinPath=${pythonPath%%/python}
echo "xy is going to install in "$pythonBinPath

printf "#!"$pythonBinPath"/python\n\n" > temp_pyPathHeader

for ifile in $sourcePath/xy*.py; do
    oriFileName=$(basename $ifile)
    execName=${oriFileName%%.*}
    
    cat temp_pyPathHeader $ifile > $pythonBinPath"/"$execName
    chmod +x $pythonBinPath"/"$execName
done

rm temp_pyPathHeader
echo "xy is installed."
