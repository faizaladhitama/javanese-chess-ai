import os

os.system("python setup.py build")
os.system("xcopy %cd%\images\* %cd%\\build\exe.win32-3.6\images\ /S /Y")
