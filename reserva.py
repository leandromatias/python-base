#!/usr/bin/env python3
"""Reserva em hoteis"""

import logging
import sys
import pprint


# Acesso ao banco de dados / parsing
# TODO: Usar função para ler os arquivos
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

# Programa principal
quartos_items = quartos.items()
print("Reserva Hotel Pythonico")
print("-" * 60)
if len(ocupados) == len(quartos):
    # TODO: sistema de aviso
    print("Hotel lotado, tente outro dia.")
    sys.exit(0)
# TODO: Tratar exceptions do nome_cliente
nome_cliente = input("Nome do cliente: ").strip()
print("-" * 60)
print("Lista de quartos:")
# TODO: usar lib Rich
print()
head = ["Número", "Nome do Quarto", "Preço", "Disponível"]
print(f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")
print("-" * 60)
for codigo, dados in quartos_items: # key(codigo) values(dados)
    nome_quarto = dados["nome"]
    preco_diaria = dados["preco"]
    disponivel = "Indisponível" if not dados["disponivel"] else "Disponível"
    print(
        f"{codigo:<6} - {nome_quarto:<14} - "
        f"R$ {preco_diaria:<9.2f} - {disponivel:<10}."
    )
print("-" * 60)
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
preco_quarto = quartos[num_quarto]["preco"]
total = preco_quarto * dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome_cliente},{num_quarto},{dias}\n")
# TODO: sistema de confirmação
print("Reservado!")
print(f"{nome_cliente}, você escolheu o {nome_quarto} e vai custar {total:.2f}.")
