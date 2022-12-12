# !/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente, o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada. Ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.1.2"
__author__ = "Leandro Matias"
__license__ = "Unlicense"

from os import getenv

current_language = getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# O(1) - constante
print(msg[current_language])
