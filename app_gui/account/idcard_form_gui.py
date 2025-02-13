import wx
import os
import sys

ROOT_DIR = os.getcwd()  # Get root directory
# Add absolute path to current sys.path
sys.path.append(os.path.dirname(ROOT_DIR + '/'))

from app_gui.generic.base_form_gui import BaseFormGUI

class IdCardFormGUI(BaseFormGUI):


    def initControls(self):

        self.referrers = ['friends', 'advertising', 'websearch', 'yellowpages']
        self.colors = ['blue', 'red', 'yellow', 'orange', 'green', 'purple',
                       'navy blue', 'black', 'gray']

        self.logger = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.saveButton = wx.Button(self, label="Save")

        self.nameLabel = wx.StaticText(self, label="Your name:")
        self.nameTextCtrl = wx.TextCtrl(self, value="Enter here your name")

        self.referrerLabel = wx.StaticText(self, label="How did you hear from us?")
        self.referrerComboBox = wx.ComboBox(self, choices=self.referrers, style=wx.CB_DROPDOWN)
        self.insuranceCheckBox = wx.CheckBox(self, label="Do you want Insured Shipment?")
        self.colorRadioBox = wx.RadioBox(self, label="What color would you like?", choices=self.colors, majorDimension=3, style=wx.RA_SPECIFY_COLS)
        

    def bindEvents(self):

        for control, event, handler in \
            [(self.saveButton, wx.EVT_BUTTON, self.onSave),
             (self.nameTextCtrl, wx.EVT_TEXT, self.onNameEntered),
             (self.nameTextCtrl, wx.EVT_CHAR, self.onNameChanged),
             (self.referrerComboBox, wx.EVT_COMBOBOX, self.onReferrerEntered),
             (self.referrerComboBox, wx.EVT_TEXT, self.onReferrerEntered),
             (self.insuranceCheckBox, wx.EVT_CHECKBOX, self.onInsuranceChanged),
             (self.colorRadioBox, wx.EVT_RADIOBOX, self.onColorchanged)]:

            control.Bind(event, handler)


    def initLayout(self):

        # A horizontal BoxSizer will contain the GridSizer (on the left)
        # and the logger text control (on the right):
        boxSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        # A GridSizer will contain the other controls:
        gridSizer = wx.FlexGridSizer(rows=5, cols=2, vgap=30, hgap=30)

        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)

        # Add the controls to the sizers:
        for control, options in \
                [(self.nameLabel, noOptions),
                 (self.nameTextCtrl, expandOption),
                 (self.referrerLabel, noOptions),
                 (self.referrerComboBox, expandOption),
                 emptySpace,
                 (self.insuranceCheckBox, noOptions),
                 emptySpace,
                 (self.colorRadioBox, noOptions),
                 emptySpace,
                 (self.saveButton, dict(flag=wx.ALIGN_CENTER))]:
            gridSizer.Add(control, **options)

        for control, options in \
                [(gridSizer, dict(border=5, flag=wx.ALL)),
                 (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND,
                                    proportion=1))]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)


    # Callback methods:

    def onColorchanged(self, event):
        self.__log('User wants color: %s'%self.colors[event.GetInt()])

    def onReferrerEntered(self, event):
        self.__log('User entered referrer: %s'%event.GetString())

    def onSave(self,event):
        self.__log('User clicked on button with id %d'%event.GetId())

    def onNameEntered(self, event):
        self.__log('User entered name: %s'%event.GetString())

    def onNameChanged(self, event):
        self.__log('User typed character: %d'%event.GetKeyCode())
        event.Skip()

    def onInsuranceChanged(self, event):
        self.__log('User wants insurance: %s'%bool(event.Checked()))

    # Helper method(s):

    def __log(self, message):
        ''' Private method to append a string to the logger text
            control. '''
        self.logger.AppendText('%s\n'%message)