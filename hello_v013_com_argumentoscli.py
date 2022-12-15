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

__version__ = "0.1.3"
__author__ = "Leandro Matias"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("leandro", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # Abordagem de LBYL:
    # if "=" in arg:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging com lib
        log.error(
            "You need to use `=`, you passed %s. Try --key=value: %s.",
            arg,
            str(e)
        )
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    # Não chega a ser um LBYL, e sim uma validação
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repetição
    if current_language is None:
        current_language = input(
            "Choose a language: "
        )

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# EAFP:
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}.")
    print(f"Language is invalid, choose from: {list(msg.keys())}.")
    sys.exit(1)

"""
# Se tratamento de erro via get() dos dicionários:
# Usabilidade dessa abordagem é ruim, o resultado é implícito e não auxilia a observar, tratar e corrigir comportamentos inesperados.
message = msg.get(current_language, msg["en_US"])
"""


# Se LBYL:
# if current_language in msg:
#    message = msg[current_language]
# else:
#    print(f"Language is invalid.")
#    sys.exit(1)

# O(1) - constante
print(message * int(arguments["count"]))
