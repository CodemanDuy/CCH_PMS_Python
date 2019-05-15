import wx

class BaseTableGUI(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(BaseTableGUI, self).__init__(*args, **kwargs)
        self.initControls()
        self.bindEvents()
        self.initLayout()

    ''' Subclasses need to implement these methods or it will raise a NotImplementedError '''
    def initControls(self):
        raise NotImplementedError 

    def bindEvents(self):
       raise NotImplementedError 

    def initLayout(self):
        raise NotImplementedError 

    

    