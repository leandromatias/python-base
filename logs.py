#!/usr/bin/env python3
"""Logs"""
__version__ = "0.1.0"

import logging
import os
from logging import handlers

# Configurar Logging - BOILERPLATE:
# TODO: usar função
## TODO: usar lib (loguru)
## Nossa instância de log
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("leandro", log_level)
## Level
### Handlers - Classe responsável pelo destino onde o log será impresso
# ch = logging.StreamHandler() # Console Handler, por default é stderr
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=100, # 10**6
    backupCount=10,
)
fh.setLevel(log_level)
## Formatação
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s  l:%(lineno)d  '
    'f:%(filename)s:  %(message)s'
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
## Destino
# log.addHandler(ch)
log.addHandler(fh)

"""
log.critical("Erro geral. Ex: sumiu banco de dados - 50")
log.error("Erro que afeta uma única execução - 40")
log.warning("Pode dar ruim ou é algo estranho, não causa erro - 30")
log.info("Mensagem geral para usuários - 20")
log.debug("Mensagem pro dev, qe, sysadmin - 10")
print("-----")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    """
    print(f"[Error] {str(e)}." # com print na tela
    print(f"[Error] {str(e)}.", file=open()) # com print em arquivo
    stdout
    ...
    stderr
    """
