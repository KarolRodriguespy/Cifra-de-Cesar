import sys
import string
import hashlib



frase = input("Digite frase a ser descriptografa: ")
chave = int(input('Entre com o valor da chave (deslocamento): '))

alfabeto = 'abcdefghijklmnopqrstuvwxyz' ':' '.'

conversao = ''

frase = frase.lower().center(15)


for caractere in frase:
    if caractere in alfabeto:
        posicao = alfabeto.find(caractere)
        posicao = (posicao - chave) % 26
        conversao = conversao + alfabeto[posicao]

conversao = conversao.encode('utf-8')

print('O texto decriptado é ', conversao)

print (hashlib.sha1(conversao).hexdigest())