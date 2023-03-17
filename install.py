import os

os.system("python setup.py build")
os.system("xcopy %cd%\images\* %cd%\\build\exe.win32-3.6\images\ /S /Y")
os.system("xcopy %cd%\music\* %cd%\\build\exe.win32-3.6\music\ /S /Y")
