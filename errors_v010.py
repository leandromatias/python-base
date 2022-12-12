#!/usr/bin/env python3
"""Script para aprendizado de tratamento de erros."""
import os
import sys

# names = ["Marco", "Maria", "Leticia", "Leandro"]
# A premissa desse programa é de que quando executado o arquivo existe, ainda que vazio.
# Em operações de I/O, a abordagem LBYL pode ser problemática pela questão de tempo de acesso. Não há garantia de que após a validação e antes da execução o arquivo não poderia ser deletado, por exemplo.
if os.path.exists("names.txt"):
    print("O arquivo existe.")
    input("...") # Race Condition
    # Nesse intervalo, um outro programa pode apagar o name.txt ou alterar de forma prejudicial ao programa escrito.
    names = open("names.txt").readlines()
else:
    print("[ERROR]: Files names.txt not found.")
    sys.exit(1)

# LBYL - Look Before You Leap (Olhe antes de atravessar)

if len(names) >= 4:
    print(names[3])
else:
    print("[ERROR]: Missing name in the list.")
    sys.exit(1)
