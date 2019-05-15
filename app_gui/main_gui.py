import wx
import sys
import os


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from app_gui.account.client_form_gui import ClientFormGUI
from app_gui.account.account_form_gui import AcountFormGUI



class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        notebook = wx.Notebook(self,style=wx.BORDER_RAISED)

        account_form = AcountFormGUI(notebook)
        client_form = ClientFormGUI(notebook)

        notebook.AddPage(account_form, 'Account')
        notebook.AddPage(client_form, 'Client')

        self.SetClientSize(notebook.GetBestSize())


