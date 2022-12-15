#!/usr/bin/env python3
"""Repete vogais"""


words = []
# TODO: tratar quando mais de uma palavra for escrita
# TODO: tratar quando vier algo diferente de letras
# TODO: adicionar sacadinhas, tipo "poxa, parece que você não digitou vogais"
# TODO: procurar se há como não disparar erro quando aperto ctrl + c
# TODO: o que fazer com a lista de palavras?
while True:
    word = input("Digite uma palavra (ou <enter> para sair): ").strip()
    if not word:
        break
    final_word = ""
    for letter in word:
        # TODO: caracteres acentuados + especiais
        if letter.lower() in "aeiou":
            final_word += (letter * 2)
        else:
            final_word += letter
        # if ternário alternativo
        #final_word += (
        #    letter * 2
        #    if letter.lower() in "aeiou"
        #    else letter
        #)
            
    words.append(final_word)

print(*words, sep="\n") # estratégia útil para evitar um for simples
