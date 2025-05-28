from google.oauth2 import service_account
from google.cloud import translate_v2 as translate

credentials = service_account.Credentials.from_service_account_file('/Users/next/Downloads/top-moment-460306-t1-03517f5f6b06.json')
translate_client = translate.Client(credentials=credentials)