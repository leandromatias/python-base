#!/usr/bin/env python3
"""Alarme de temperatura"""

import sys
import logging

log = logging.Logger("alerta")
info = {
    "temperatura": None,
    "umidade": None,
} # Dict -> mutável
keys = info.keys()

#for key in info: # iterando um dict mutável
#for key in info.keys(): # outro objeto criado, em outro lugar da memória
for key in keys: # forma mais explícita possível sem correr riscos de runtimeerror
    try:
        info[key] = float(input(f"Qual a {key}?").strip())
    except ValueError:
        log.error(f"A {key} informada é inválida.")
        sys.exit(1)

# Extrair os valores do dicionário
temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("Alerta!!! Perigo de calor extremo.")
elif (temp * 3) >= umidade:
    print("Alerta! Perigo de calor úmido.")
elif temp >= 10 and temp <= 30:
    print("A temperatura informada é considerada normal.")
elif temp >= 0 and temp <= 10:
    print("Alerta! O frio pode trazer doenças respiratórias.")
elif temp < 0:
    print("Alerta!!! Perigo com o frio extremo.")
