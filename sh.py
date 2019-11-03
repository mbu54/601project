#pip install gspread oauth2client


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds= ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client=gspread.authorize(creds)

sheet=client.open("Coded Aperture Database").sheet1

data=sheet.get_all_records()

row=sheet.row_values(1)
col=sheet.col_values(1)
cell=sheet.cell(1,2).value

#Insert row, will not override
#insertRow=["hello",5,"blue"]
#sheet.insert_row(insertRow,2)

#Delete
#sheet.delete_row(1)
#Update
#sheet.update_cell(1,1,"Name")

print(len(data))