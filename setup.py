import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
buildOptions = dict(include_files=['images/'])
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
elif sys.platform == "win64":
    base = "Win64GUI"

setup(
    name="Catur Jawa",
    version="0.8",
    author="Faizal Adhitama Prabowo & Tinna Fauzia Azhar",
    description="Catur Jawa Game",
    options={"build_exe": build_exe_options},
    executables=[Executable("Main.py", base=base)])
