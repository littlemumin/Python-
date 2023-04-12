import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1GItSKnoekSL8xgHC6p57QJTpuWpZM5Bups62xUpz-Rc"


def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A1:D4").execute()
        values = result.get("values", [])
        for row in values:
            print(row)
    except HttpError as error:
        print(error)


if __name__ == "__main__":
    main()

























# # # import gspread
# # # import json
# # #
# # #
# # # def get_spreadsheet():
# # #     """
# # #     スプレッドシートとの連携の関数
# # #     :return: ワークシート
# # #     """
# # #     #ここから編集
# # #     keyfile_path = "C:\Development/stately-lodge-383318-b9873d01ec70.json" # 秘密鍵のjsonのパスを記入
# # #     SPREADSHEET_KEY = "1GItSKnoekSL8xgHC6p57QJTpuWpZM5Bups62xUpz-Rc" # 転記したいワークブックのIDを記入
# # #     #ここまで
# # #
# # #     #ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成。
# # #     from oauth2client.service_account import ServiceAccountCredentials
# # #
# # #     #2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
# # #     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# # #
# # #     #認証情報設定
# # #     #ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
# # #     credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile_path, scope)
# # #
# # #     #OAuth2の資格情報を使用してGoogle APIにログインします。
# # #     gc = gspread.authorize(credentials)
# # #
# # #     #共有設定したスプレッドシートのシート1を開く
# # #     workbook = gc.open_by_key(SPREADSHEET_KEY)
# # #     # return workbook
# # #
# # #
# # #     ##############################################
# #
# # from google.oauth2.service_account import Credentials
# # import gspread
# #
# #
# # scopes = [
# #     'https://www.googleapis.com/auth/spreadsheets',
# #     'https://www.googleapis.com/auth/drive'
# # ]
# #
# #
# # credentials = Credentials.from_service_account_file("C:\Development/stately-lodge-383318-b9873d01ec70.jso", scopes=scopes)
# # gc = gspread.authorize(credentials)
# # spreadsheet_url = "https://docs.google.com/spreadsheets/d/1GItSKnoekSL8xgHC6p57QJTpuWpZM5Bups62xUpz-Rc/edit#gid=0"
# # spreadsheet = gc.open_by_url(spreadsheet_url)
#
# import gspread
# import json
# from oauth2client.service_account import ServiceAccountCredentials
# # from gspread_dataframe import get_as_dataframe, set_with_dataframe
#
# # (1) Google Spread Sheetsにアクセス
#
# def connect_gspread(jsonf,key):
#     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
#     gc = gspread.authorize(credentials)
#     SPREADSHEET_KEY = key
#     worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
#     return worksheet
#
# # ここでjsonfile名と用意したkeyを入力
# jsonf = "C:\Development/stately-lodge-383318-b9873d01ec70.json"
# spread_sheet_key = "1GItSKnoekSL8xgHC6p57QJTpuWpZM5Bups62xUpz-Rc"
# ws = connect_gspread(jsonf, spread_sheet_key)
#
# # 予め用意したデータフレーム(df)を指定のスプレッドシートに反映させる
# df = 123456789
#
# ws.append_rows(df.values.tolist())