import webbrowser
import requests

#Rotas para limpar os caches e gerar um novo
rota='http://127.0.0.1:8000/'
clearCache=rota+'cache/clear/cache'
clearViewCache=rota+'cache/clear/view'
makeCache=rota+'cache/make'

webbrowser.open(clearCache)
response=requests.get(clearCache)
if response.status_code == 200:
    webbrowser.open(clearViewCache)
    response = requests.get(clearViewCache)
    if response.status_code == 200:
        webbrowser.open(makeCache)
        response = requests.get(makeCache)
        if response.status_code == 200:
            print('success')
        elif response.status_code == 404:
            print('Erro no make cache')
    elif response.status_code == 404:
        print('Erro no clean cache view')
elif response.status_code == 404:
    print('Erro no clean cache')