#!/usr/bin/env python3
"""Script para aprendizado de tratamento de erros."""
import os
import sys

# EAFP - Easy to Ask Forgiviness than Permission
# (É mais fácil pedir perdão do que permissão)

try:
    raise RuntimeError("Ocorreu um erro.")
except Exception as e:
    print(str(e))
    print("-" * 30)

try:
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Isso vai ser executado se não disparar except.")
finally:
    print("Isso vai ser sempre executado.")
    print("-" * 30)

try:
    print(names[3])
except:
    print("[ERROR]: Missing name in the list.")
    sys.exit(1)

# A premissa desse programa é de que quando executado o arquivo existe, ainda que vazio.
# Em operações de I/O, a abordagem LBYL pode ser problemática pela questão de tempo de acesso. Não há garantia de que após a validação e antes da execução o arquivo não poderia ser deletado, por exemplo.
#if os.path.exists("names.txt"):
#    print("O arquivo existe.")
#    input("...") # Race Condition
    # Nesse intervalo, um outro programa pode apagar o name.txt ou alterar de forma prejudicial ao programa escrito.
#    names = open("names.txt").readlines()
#else:
#    print("[ERROR]: Files names.txt not found.")
#    sys.exit(1)

# LBYL - Look Before You Leap (Olhe antes de atravessar)

#if len(names) >= 4:
#    print(names[3])
#else:
#    print("[ERROR]: Missing name in the list.")
#    sys.exit(1)
