#!/usr/bin/env python3
"""Alarme de temperatura"""

import sys
import logging

log = logging.Logger("alerta")

# TODO: Usar funções para ler input
info = {
    "temperatura": None,
    "umidade": None,
} # Dict -> mutável

keys = info.keys()

while True:
    # Condição de parada
    # O dicionário está completamente preenchido
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break # Cessa o while

    for key in keys: # ["temperatura", "umidade"]
        # não podemoss alterar a estrutura dos dicionários iterados
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"Qual a {key}? ").strip())
        except ValueError:
            log.error(f"A {key} informada é inválida.")
            break # Cessa o for

# Desempacotar temp e umidade da lista de valores do dicionário
temp, umidade = info.values()

if temp > 45:
    print("Alerta!!! Perigo de calor extremo.")
elif temp > 30 and (temp * 3) >= umidade:
    print("Alerta! Perigo de calor úmido.")
elif temp >= 10 and temp <= 30:
    print("A temperatura informada é considerada normal.")
elif temp >= 0 and temp <= 10:
    print("Alerta! O frio pode trazer doenças respiratórias.")
elif temp < 0:
    print("Alerta!!! Perigo com o frio extremo.")
