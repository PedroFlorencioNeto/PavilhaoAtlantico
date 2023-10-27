import requests
import configparser

# acessando ao token
parser = configparser.ConfigParser()
parser.read('pipeline.conf')
TOKEN = parser.get('datawrapper_token','token')

# login com erro
url = f"https://api.datawrapper.de/v3/auth/login/{TOKEN}"
print(url)
headers = {"accept": "*/*"}
response = requests.get(url, headers=headers)

# print(response.text)