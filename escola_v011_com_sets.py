#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:
    print(f"Os alunos de {nome_atividade}, por sala, são:".upper())
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    # intersecção de alunos da sala 1 com a atividade

    print("Sala 1:", atividade_sala1)
    print("Sala 2:", atividade_sala2)
    print("-" * 40)
