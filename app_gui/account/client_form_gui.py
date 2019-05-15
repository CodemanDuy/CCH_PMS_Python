import wx
import os
import sys
import wx.grid as gridlib

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from app_gui.generic.base_form_gui import BaseFormGUI

from services.account.client_service import ClientService
from services.account.identitycard_service import IdentityCardService
from services.generalunit.country_service import CountryService

class ClientFormGUI(BaseFormGUI):

    
    
    def initControls(self):

        self.btnSave = wx.Button(self, label="Lưu")

        self.lbClientId = wx.StaticText(self, label="Mã Khách Hàng")
        self.txtClientId = wx.TextCtrl(self, style=wx.TE_READONLY)

        # self.lbIndexNo = wx.StaticText(self, label="So Thu Tu")
        # self.txtIndexNo = wx.TextCtrl(self, style=wx.TE_READONLY)

        self.lbBookerCode = wx.StaticText(self, label="Mã 4G Người Đại Diện")
        self.txtBookerCode = wx.TextCtrl(self, style=wx.TE_READONLY)

        self.lbFullName = wx.StaticText(self, label="Họ Tên")
        self.txtFullName = wx.TextCtrl(self, value="")

        self.lstIdCardType = ['CCCD', 'PASSPORT', 'BẰNG LÁI']
        self.lbIdCardType = wx.StaticText(self, label="Loại Giấy Tờ Tùy Thân")
        self.cbbIdCardType = wx.ComboBox(self, choices=self.lstIdCardType, style=wx.CB_DROPDOWN)

        self.lbIdentityNo = wx.StaticText(self, label="Mã Công Dân")
        self.txtIdentityNo = wx.TextCtrl(self, value="")

        self.lbPhone1 = wx.StaticText(self, label="Số Điện Thoại 1")
        self.txtPhone1 = wx.TextCtrl(self, value="")

        self.lbPhone2 = wx.StaticText(self, label="Số Điện Thoại 2")
        self.txtPhone2 = wx.TextCtrl(self, value="")

        self.lbEmail = wx.StaticText(self, label="Email")
        self.txtEmail = wx.TextCtrl(self, value="")

        self.lbTempAddress = wx.StaticText(self, label="Địa Chỉ Tạm Trú")
        self.txaTempAddress = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.lbCurrentJob = wx.StaticText(self, label="Nghề Nghiệp")
        self.txtCurrentJob = wx.TextCtrl(self, value="")

        self.lbDOB = wx.StaticText(self, label="Ngày Sinh")
        self.txtDOB = wx.TextCtrl(self, value="")

        self.lstGender = ['Nam', 'Nữ']
        self.radGender = wx.RadioBox(
            self, label="Giới Tính", choices=self.lstGender, majorDimension=2, style=wx.RA_SPECIFY_COLS)

        countryService = CountryService()
        self.lstCountry = [c.Name for c in countryService.get_country_all()]
        self.lbCountry = wx.StaticText(self, label="Quốc Tịch")
        self.cbbCountry = wx.ComboBox(self, choices=self.lstCountry, style=wx.CB_DROPDOWN)

        self.lbHomeTown = wx.StaticText(self, label="Quê Quán")
        self.txtHomeTown = wx.TextCtrl(self, value="")

        self.lbPermAddress = wx.StaticText(self, label="Địa Chỉ Thường Trú")
        self.txaPermAddress = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.lbDateIssued = wx.StaticText(self, label="Ngày Cấp")
        self.txtDateIssued = wx.TextCtrl(self, value="")

        self.lbDateExpired = wx.StaticText(self, label="Ngày Hết Hạn")
        self.txtDateExpired = wx.TextCtrl(self, value="")

        self.chkIsClientAvailable = wx.CheckBox(
            self, label="Xác nhận Khách Hàng hợp lệ")

    def bindEvents(self):
        for control, event, handler in [
            (self.btnSave, wx.EVT_BUTTON, self.onSave)
        ]:
            control.Bind(event, handler)

    def initLayout(self):

        # Container wrap all
        bxsMainContainer = wx.BoxSizer(orient=wx.HORIZONTAL)

        # Split to two big section rows
        bxsBodyTopContainer = wx.BoxSizer(orient=wx.HORIZONTAL)
        bxsBodyBottomContainer = wx.BoxSizer(orient=wx.HORIZONTAL)

        # Split to two big section columns
        bxsLeftContainer = wx.BoxSizer(orient=wx.VERTICAL)
        bxsRightContainer = wx.BoxSizer(orient=wx.VERTICAL)

        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)


        # A GridSizer will contain the form controls:
        gdsFormContainer = wx.FlexGridSizer(rows=20, cols=4, vgap=20, hgap=20)    
        for control, options in [
            (self.lbClientId, noOptions),
            (self.txtClientId, expandOption),
            (self.lbBookerCode, noOptions),
            (self.txtBookerCode, expandOption),
            (self.lbFullName, noOptions),
            (self.txtFullName, expandOption),
            (self.lbEmail, noOptions),
            (self.txtEmail, expandOption),
            (self.lbPhone1, noOptions),
            (self.txtPhone1, expandOption),
            (self.lbPhone2, noOptions),
            (self.txtPhone2, expandOption),
            (self.lbTempAddress, noOptions),
            (self.txaTempAddress, expandOption),
            emptySpace,
            emptySpace,
            (self.lbCurrentJob, noOptions),
            (self.txtCurrentJob, expandOption),            
            (self.radGender, expandOption),
            emptySpace,
            (self.chkIsClientAvailable, expandOption),
            emptySpace,
            emptySpace,
            emptySpace,
            (self.btnSave, dict(flag=wx.ALIGN_CENTER))
        ]:           
            # if(control is not (0, 0)):
            #     control.SetBackgroundColour("red")
            gdsFormContainer.Add(control, **options)
        
        bxsLeftContainer.Add(gdsFormContainer)

        # Add controls to the right sizers:
        sbIdCard = wx.StaticBox(self, label="Giấy Tờ Tùy Thân")
        bxsIdCard = wx.StaticBoxSizer(sbIdCard, wx.VERTICAL)
        for control, options in [
            (self.lbIdCardType, noOptions),
            (self.cbbIdCardType, expandOption),
            (self.lbIdentityNo, noOptions),
            (self.txtIdentityNo, expandOption),
            (self.lbDOB, noOptions),
            (self.txtDOB, expandOption),
            (self.lbCountry, noOptions),
            (self.cbbCountry, expandOption),
            (self.lbHomeTown, noOptions),
            (self.txtHomeTown, expandOption),
            (self.lbPermAddress, noOptions),
            (self.txaPermAddress, expandOption),
            (self.lbDateIssued, noOptions),
            (self.txtDateIssued, expandOption),
            (self.lbDateExpired, noOptions),
            (self.txtDateExpired, expandOption)
        ]:
            bxsIdCard.Add(control, **options)
        
        bxsRightContainer.Add(bxsIdCard)
        
        # Add two big section columns to top container
        for control, options in [(bxsLeftContainer, dict(border=5, flag=wx.ALL)), (bxsRightContainer, dict(border=5, flag=wx.ALL))]:
            bxsBodyTopContainer.Add(control, **options)        

        
        ###Region: Grid DATA        
        clientService = ClientService()
        idcardService = IdentityCardService()

        data = clientService.get_client_all()

        totalrows = len(data)+1 or 20
        totalcolumns = 6
        # Create Grid for Table
        tblData = gridlib.Grid(self)
        tblData.CreateGrid(totalrows, totalcolumns)        
        tblData.SetCellValue(0,0, "Mã KH")
        tblData.SetCellValue(0,1, "Mã 4G Người Đại Diện")
        tblData.SetCellValue(0,2, "Mã Công Dân")
        tblData.SetCellValue(0,3, "Họ Tên")
        tblData.SetCellValue(0,4, "Email")
        tblData.SetCellValue(0,5, "Số Điện Thoại")
        # Set Style for Header Column
        for index in range(0, totalcolumns):
            tblData.SetCellBackgroundColour(0, index, wx.BLACK)        
            tblData.SetCellTextColour(0, index, wx.WHITE)

        # Push data to grid
        for idx, item in enumerate(data):
            cardItem = idcardService.get_idcard_byId(item.IdentityCardId)
                
            tblData.SetCellValue(idx+1, 0, item.ClientId or 'NULL')                
            tblData.SetCellValue(idx+1, 1, item.BookerFgCode or 'NULL')
            tblData.SetCellValue(idx+1, 2, (cardItem is not None) and str(cardItem.IdentityNo) or 'NULL')
            tblData.SetCellValue(idx+1, 3, (cardItem is not None) and cardItem.FullName or item.FullName or 'NULL')
            tblData.SetCellValue(idx+1, 4, item.Email or 'NULL')
            tblData.SetCellValue(idx+1, 5, item.Phone1 or item.Phone2 or 'NULL')

        bxsBodyBottomContainer.Add(tblData, 1, wx.EXPAND)       
        ###End Region: Grid DATA

        # Add two big section rows to container
        for control, options in [(bxsBodyTopContainer, dict(border=5, flag=wx.ALL)), (bxsBodyBottomContainer, dict(border=5, flag=wx.ALL))]:
            bxsMainContainer.Add(control, **options)

        self.SetSizerAndFit(bxsMainContainer)



    # Callback methods:

    def onSave(self,event):
        self.__log('User clicked on button with id %d'%event.GetId())