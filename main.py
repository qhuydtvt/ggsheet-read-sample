import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('GGSpreadSheetReadDemo-67e5e6cf4ad9.json', scope)
client = gspread.authorize(creds)

first_sheet = client.open('KPI').sheet1

telemedicine = first_sheet.get_all_records()
print(telemedicine)