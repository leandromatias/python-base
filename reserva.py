#!/usr/bin/env python3
"""Reserva em hoteis"""

import logging
import sys
import pprint

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome_quarto, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome_quarto,
            "dias": dias,
        }
except FileNotFoundError:
    logging.error("Arquivo `reservas.txt` não existe.")
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome_quarto, preco_diaria = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome_quarto,
            "preco": float(preco_diaria), # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True,
        }
except FileNotFoundError:
    logging.error("Arquivo `quartos.txt` não existe.")
    sys.exit(1) 

quartos_items = quartos.items()

print("Reserva Hotel Pythonico")
print("-" * 40)
if len(ocupados) == len(quartos):
    print("Hotel lotado, tente outro dia.")
    sys.exit(1)
# TODO: Tratar exceptions do nome_cliente
nome_cliente = input("Nome do cliente: ").strip()
print("-" * 40)
print("Lista de quartos:")

for codigo, dados in quartos_items: # key(codigo) values(dados)
    nome_quarto = dados["nome"]
    preco_diaria = dados["preco"]
    disponivel = "Indisponível" if not dados["disponivel"] else "Disponível"
    print(f"{codigo} - {nome_quarto} - R$ {preco_diaria:.2f} - {disponivel}.")
print("-" * 40)
# TODO: for para iterar as duas perguntas
try:
    num_quarto = int(input("Número do quarto: ").strip())
    # TODO: while para permitir ao usuario escolher outro quarto
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido, insira apenas digitos válidos.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)

try:
    dias = int(input("Quantos dias deseja permanecer? ").strip())
except ValueError:
    logging.error("Número inválido, insira apenas digitos válidos.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
disponivel = quartos[num_quarto]["disponivel"]
preco_quarto = quartos[num_quarto]["preco"]
total = preco_quarto * dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome_cliente},{num_quarto},{dias}\n")

print("Reservado!")
print(f"{nome_cliente}, você escolheu o {nome_quarto} e vai custar {total:.2f}.")
