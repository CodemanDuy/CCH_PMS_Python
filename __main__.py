import wx
import os
import sys


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from app_gui.main_gui import MainFrame

"""
doc: Main base class
"""
class Main():

    def __init__(self):
        pass

    def mainProcess(self):

        try:
            app = wx.App(0)
            frame = MainFrame(None, title='CCH Property Management System')
            frame.Show()
            app.MainLoop()
        except Exception as ex:
            print('Error: ', ex)

        print('#'*40)
        return

"""
doc: Code will begin from here
"""
if __name__ == '__main__':
    proc = Main()
    proc.mainProcess()  


### BUILD APP
# Step 1: Put all images folder to "dist" folder (folder to deploy app) 
# Step 2: Open CMD/Terminal and change directory path to main.py
# Step 3: Run command => pyinstaller main.py
