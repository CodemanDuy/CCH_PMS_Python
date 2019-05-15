import csv
import os, sys
from os.path import join, dirname, abspath
import xlrd


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from datacontext.sqlite_dbcontext import Database
# from datacontext.entities_container import EntitiesContainer
# entity = EntitiesContainer()
from datacontext.entities.City import City
from datacontext.entities.District import District
from datacontext.entities.Subdistrict import Subdistrict

#### Analyze Excel File and push to list
fname = join(dirname(dirname(abspath(__file__))),
             'datacontext/datasources', 'DataAdministrativeUnitVn_190503.xls')
# open a workbook
workbook = xlrd.open_workbook(fname)
# open sheet by name
# worksheet = workbook.sheet_by_name('Sheet1')
# open sheet by index
worksheet = workbook.sheet_by_index(0)
# read cell value
worksheet.cell(0, 0).value
# Print all values, iterating through rows and columns
num_cols = worksheet.ncols   # Number of columns


lstCity = []
lstDist = []
lstSubDist = []

cityId = 1
distId = 1
subDistId = 1

parentFirstId = 0
parentSecondId = 0

for row_idx in range(0, worksheet.nrows):    # Iterate through rows
#     print ('-'*40)
#     print ('Row: %s' % row_idx)   # Print row number
    if(row_idx == 0):
        continue
    for col_idx in range(0, num_cols):  # Iterate through columns
        # Get cell object by row, col
        cell_obj = worksheet.cell(row_idx, col_idx)
        # print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
        # print(str(cell_obj.value))
        if(col_idx == 0):
            if(("Thành phố" in str(cell_obj.value) or "Tỉnh" in str(cell_obj.value)) and not any(c for c in lstCity if str(cell_obj.value) == c.Name)):
                modelCity = City()
                modelCity.CityId = cityId
                modelCity.CountryId = 249
                modelCity.ParentId = 0
                modelCity.Name = cell_obj.value
                lstCity.append(modelCity)
                parentFirstId = cityId
                cityId += 1
        if(col_idx == 1 and cell_obj is not None):
            city = lstCity[-1]
            city.CityCode = cell_obj.value
        if(col_idx == 2):
            if(("Thành phố" in str(cell_obj.value) or "Tỉnh" in str(cell_obj.value)) and not any(c for c in lstCity if str(cell_obj.value) == c.Name)):
                modelCity = City()
                modelCity.CityId = cityId
                modelCity.CountryId = 249
                modelCity.ParentId = parentFirstId
                modelCity.Name = cell_obj.value
                lstCity.append(modelCity)
                parentSecondId = cityId
                cityId += 1
            if(("Quận" in str(cell_obj.value) or "Huyện" in str(cell_obj.value) or "Thị xã" in str(cell_obj.value)) and not any(c for c in lstDist if str(cell_obj.value) == c.Name)):
                modelDistrict = District()
                modelDistrict.DistrictId = distId
                modelDistrict.CityId = parentFirstId
                modelDistrict.Name = cell_obj.value
                lstDist.append(modelDistrict)
                parentSecondId = distId
                distId += 1
        if(col_idx == 3 and cell_obj is not None):
            city = lstCity[-1]
            city.CityCode = cell_obj.value
            dist = lstDist[-1]
            dist.DistrictCode = cell_obj.value
        if(col_idx == 4):
            if(("Phường" in str(cell_obj.value) or "Xã" in str(cell_obj.value)) and not any(c for c in lstDist if str(cell_obj.value) == c.Name)):
                modelSubDistrict = Subdistrict()
                modelSubDistrict.SubdistrictId = subDistId
                modelSubDistrict.DistrictId = parentSecondId
                modelSubDistrict.Name = cell_obj.value
                lstSubDist.append(modelSubDistrict)
                subDistId += 1
        if(col_idx == 5 and cell_obj is not None):
            subdist = lstSubDist[-1]
            subdist.SubdistrictCode = cell_obj.value


# #### Write to txt file to test data before insert to Database
# # Get current directory
# dire = os.getcwd()
# print("Directory:", dire)
# # Change directory
# os.chdir(r'' + dire + r'/CCHouseStudio_PMS/datacontext/datasources/')
# # Open with Append mode for Text
# fo = open('AdministrationVn.txt', 'a')
# print("Name of the file:", fo.name)
# print('Current File Python:', __file__)
# # Write to a file
# for ct in lstCity:
#     txtCity = 'CityId: {0} - City Name: {1} - CityParentId: {2} - CityCode: {3}'.format(
#         str(ct.CityId), ct.Name, str(ct.ParentId), str(ct.CityCode))
#     fo.write(txtCity)
#     fo.write("\n")

# fo.write("\n")
# for dt in lstDist:
#     txtDistrict = 'DistrictId: {0} - District Name: {1} - CityId: {2} - DistrictCode: {3}'.format(
#         str(dt.DistrictId), dt.Name, str(dt.CityId), str(dt.DistrictCode))
#     fo.write(txtDistrict)
#     fo.write("\n")

# fo.write("\n")
# for sdt in lstSubDist:
#     txtSubDistrict = 'SubDistrictId: {0} - Sub District Name: {1} - DistrictId: {2}'.format(
#         str(sdt.SubdistrictId), sdt.Name, str(sdt.DistrictId))
#     fo.write(txtSubDistrict)
#     fo.write("\n")

# fo.close()

#### Insert to Db from excel file
# db_filedir = "/Users/duyle/Desktop/CodeSpace/Data/CCH_PMS.db"
# with Database(db_filedir) as __context:
#     # fields = '"CityId", "CountryId", "ParentId", "CityCode", "Name", "SortOrder"'
#     # values = '''(3, 1, 0, NULL, "Ho Chi Minh", NULL), (4, 1, 0, NULL, "Ha Noi", NULL)'''
#     # result = __context.table('City').insert(fields, values)
    
#     resultCity = __context.table(City.__name__).insert_by_listmodel(lstCity)
#     resultDistrict = __context.table(District.__name__).insert_by_listmodel(lstDist)
#     resultSubDistrict = __context.table(Subdistrict.__name__).insert_by_listmodel(lstSubDist)
