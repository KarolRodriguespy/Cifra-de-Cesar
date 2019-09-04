import requests
import json
import hashlib

resposta = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=7658d6862ebdd9fc82eaa090e8a5523dfae88905')
if resposta.status_code == 200:
    conteudo = json.loads(resposta.content)

frase = conteudo['cifrado']
chave = conteudo['numero_casas']

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

decifrado = ''

frase = frase.lower()

for caractere in frase:
        num = 0
        if caractere in alfabeto:
            num = alfabeto.find(caractere)
            num = num - chave
            decifrado = decifrado + alfabeto[num]
        else:
            decifrado = decifrado + caractere

resumo_criptografico = (hashlib.sha1(decifrado.encode('UTF-8')).hexdigest())

conteudo['decifrado'] = decifrado
conteudo['resumo_criptografico'] = resumo_criptografico

print(conteudo)

#answer = open('answer.json','a')
#answer.write('numero_casas: 1, token: 7658d6862ebdd9fc82eaa090e8a5523dfae88905, cifrado: efwfmpqfs: bo pshbojtn uibu uvsot dpggff joup dpef. volopxo, decifrado: developer: an organism that turns coffee into code. unknown, resumo_criptografico: 9c7354ba4d33fcaa91c1050f15214497dca9cb56')
#answer.close()

#print(answer)

with open('answer.json', 'w') as outfile:
    json.dump(conteudo, outfile)

#answer = open('answer.json', 'r')
#usar write pra escrever o arquivo e salvar informações e fechar o arquivo

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=7658d6862ebdd9fc82eaa090e8a5523dfae88905'
data = {'answer':('answer.json', open('answer.json', 'rb')) }

#data = {'token': '7658d6862ebdd9fc82eaa090e8a5523dfae88905',
 #       'api_option': 'paste',
  #      'api_paste_code': answer,
   #     'api_paste_format': 'json'}

r = requests.post(url,files=data)
print(r.text)
print(r.status_code)


