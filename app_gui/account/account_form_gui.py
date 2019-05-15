import wx
import os
import sys
import wx.grid as gridlib

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from app_gui.generic.base_form_gui import BaseFormGUI

from services.account.account_service import AccountService


class AcountFormGUI(BaseFormGUI):


    def initControls(self):

        self.btnSave = wx.Button(self, label="Lưu")

        self.lbAccountId = wx.StaticText(self, label="Mã Tài Khoản KH")
        self.txtAccountId = wx.TextCtrl(self, style=wx.TE_READONLY)

        # self.lbIndexNo = wx.StaticText(self, label="So Thu Tu")
        # self.txtIndexNo = wx.TextCtrl(self, style=wx.TE_READONLY)

        self.lbUsername = wx.StaticText(self, label="Tên Đăng Nhập")
        self.txtUsername = wx.TextCtrl(self, value="")

        self.chkIsBooker = wx.CheckBox(self, label="Tài khoản này của Người Đại Diện?")       

        self.chkIsClientAvailable = wx.CheckBox(self, label="Xác nhận Khách Hàng hợp lệ")

        ###Region: Grid DATA        
        service = AccountService()
        data = service.get_account_all()

        totalrows = len(data)+1 or 20
        totalcolumns = 2

        self.tblData = gridlib.Grid(self)
        self.tblData.CreateGrid(totalrows, totalcolumns)        
        self.tblData.SetCellValue(0,0, "Mã TK", )        
        self.tblData.SetCellValue(0,1, "Tên Đăng Nhập")                
        # Set Style for Header Column
        for index in range(0, 2):
            self.tblData.SetCellBackgroundColour(0, index, wx.BLACK)        
            self.tblData.SetCellTextColour(0, index, wx.WHITE)

        for idx, item in enumerate(data):
            self.tblData.SetCellValue(idx+1, 0, item.AccountId)
            self.tblData.SetCellValue(idx+1, 1, item.Username)
        
        self.tblData.SetSelectionMode(wx.grid.Grid.SelectRows)
        ###End Region: Grid DATA 

    def bindEvents(self):
        for control, event, handler in [
            (self.btnSave, wx.EVT_BUTTON, self.onSave),
            (self.tblData, wx.grid.EVT_GRID_SELECT_CELL, self.onSelectRow)
        ]:
            control.Bind(event, handler)

    def initLayout(self):
       
        # Container wrap all
        bxsMainContainer = wx.BoxSizer(orient=wx.HORIZONTAL)

        # Split to two big section rows
        bxsBodyTopContainer = wx.BoxSizer(orient=wx.HORIZONTAL)
        bxsBodyBottomContainer = wx.BoxSizer(orient=wx.HORIZONTAL)

        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)


        # A GridSizer will contain the form controls:
        gdsFormContainer = wx.FlexGridSizer(rows=20, cols=2, vgap=20, hgap=20)    
        for control, options in [
            (self.lbAccountId, noOptions),
            (self.txtAccountId, expandOption),
            (self.lbUsername, expandOption),
            (self.txtUsername, noOptions),            
            (self.chkIsBooker, expandOption),
            emptySpace,
            (self.chkIsClientAvailable, expandOption),
            emptySpace,
            (self.btnSave, dict(flag=wx.ALIGN_CENTER))
        ]:           
            # if(control is not (0, 0)):
            #     control.SetBackgroundColour("red")
            gdsFormContainer.Add(control, **options)
        
        bxsBodyTopContainer.Add(gdsFormContainer, 1, wx.EXPAND)             
                        
        ### Add table data to container
        bxsBodyBottomContainer.Add(self.tblData, 1, wx.EXPAND)     

        # Add two big section rows to container
        for control, options in [(bxsBodyTopContainer, dict(border=5, flag=wx.ALL)), (bxsBodyBottomContainer, dict(border=5, flag=wx.ALL))]:
            bxsMainContainer.Add(control, **options)

        self.SetSizerAndFit(bxsMainContainer)



    # Callback methods:

    def onSave(self, event):
        
        result = None
        service = AccountService()

        modelAcc = service.Account
        modelAcc.Username = self.txtUsername.GetValue()
        modelAcc.IsBooker = self.chkIsBooker.GetValue() is True and 1 or 0
        modelAcc.IsAvailable = self.chkIsClientAvailable.GetValue() is True and 1 or 0

        accountId = self.txtAccountId.GetValue()
        if not accountId:
            result = service.add_account(modelAcc)
        else: 
            modelAcc.AccountId = accountId
            result = service.update_account(modelAcc)
        
        service.ec.print_ValueEntityClass(result)
    
    
    def onSelectRow(self, event):       
        rowIndex = self.tblData.GetSelectedRows()[0]
        accountId = self.tblData.GetCellValue(rowIndex, 0)
        userName = self.tblData.GetCellValue(rowIndex, 1)
        # print(accountId)

        self.txtAccountId.SetValue(accountId)
        self.txtUsername.SetValue(userName)

        event.Skip()