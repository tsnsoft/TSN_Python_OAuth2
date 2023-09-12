# Пример получения данных пользователя с помощью Google API OAuth2

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Создаем проект в Google Cloud Platform
# https://console.cloud.google.com/apis/credentials

# Делаем запрос на получение данных пользователя через браузер и Google API OAuth2
flow = (InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=['openid','https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/userinfo.profile']))
flow.run_local_server()

# Получаем данные пользователя
credentials = flow.credentials
user_info_service = build('oauth2', 'v2', credentials=credentials)
user_info = user_info_service.userinfo().get().execute()

# Выводим данные пользователя если email подтвержден
if user_info['verified_email'] == True:
    print(user_info['email'])
    print(user_info['name'])
