from google.oauth2.service_account import Credentials
import gspread


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]


credentials = Credentials.from_service_account_file(
    "C:\Development\stately-lodge-383318-b9873d01ec70.json",
    scopes=scopes
)


gc = gspread.authorize(credentials)


spreadsheet_url = "https://docs.google.com/spreadsheets/d/1GItSKnoekSL8xgHC6p57QJTpuWpZM5Bups62xUpz-Rc/edit#gid=0"


spreadsheet = gc.open_by_url(spreadsheet_url)