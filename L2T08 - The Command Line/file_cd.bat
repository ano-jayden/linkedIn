:: Create the initial directories
mkdir hyper
mkdir dev
mkdir level

:: Navigate into the 'hyper' directory and create subdirectories
cd hyper
mkdir level1
mkdir level2
mkdir level3

:: Go back to the parent directory before deleting 'dev' and 'level'
cd ..

:: Delete the 'dev' and 'level' directories and their contents
rd /s /q dev
rd /s /q level
