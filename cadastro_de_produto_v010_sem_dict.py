#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"


# muita variável pra representar um objeto só, seria muito mais fácil usar um tipo de dados que seja capaz de representar um objeto com significado semântico
produto_nome = "Caneta"
produto_cor1 = "azul"
produto_cor2 = "branco"
produto_preco = 3.23
produto_dimensao_altura = 12.1
produto_dimensao_largura = 0.8
produto_em_estoque = True
produto_codigo = 45678
produto_codebar = None


# dentro de uma tupla, mas só conseguimos exprimir no print porque sabemos as posições dos dados nessa estrutura.
compra = ("Bruno", produto_nome, 3)
total_compra = compra[2] * produto_preco

print(
    f"O cliente {compra[0]} comprou {compra[1]}"
    f" e pagou o total de {total_compra}."
)
