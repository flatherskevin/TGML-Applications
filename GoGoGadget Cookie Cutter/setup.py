from SETTINGS import *
from cx_Freeze import Executable
from cx_Freeze import setup
import os
import sys

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)

os.environ['TCL_LIBRARY'] = os.path.expanduser('~/AppData/Local/Programs/Python/Python36-32/tcl/tcl8.6')
os.environ['TK_LIBRARY'] = os.path.expanduser('~/AppData/Local/Programs/Python/Python36-32/tcl/tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    'packages': [
        'os'
    ], 
    'excludes': [],
    'includes': [
        'lxml',
        'lxml._elementpath',
        'lxml.etree',
        'tkinter',
        'tkinter.filedialog'
    ],
    'include_files': [
				os.path.expanduser('~/AppData/Local/Programs/Python/Python36-32/DLLs/tcl86t.dll'),
				os.path.expanduser('~/AppData/Local/Programs/Python/Python36-32/DLLs/tk86t.dll'),
        'TGML',
        'icon.ico'
    ]
}


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(name=NAME,
      version=VERSION,
      description='We all love homemade cookie :)',
      options={'build_exe': build_exe_options},
      executables=[Executable(
      'GoGoGadget Cookie Cutter.py',
      base=base,
			icon = ICON)]
			)