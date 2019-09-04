import requests
import json
import hashlib

resposta = requests.get('')
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

with open('answer.json', 'w') as outfile:
    json.dump(conteudo, outfile)

url = ''
data = {'answer':('answer.json', open('answer.json', 'rb')) }

r = requests.post(url,files=data)
print(r.text)
print(r.status_code)


