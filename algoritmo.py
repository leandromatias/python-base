# PSEUDO CÓDIGO EM PYTHON
import ir, pegar, pedir, tem, comer, ficar

# Premissas
hoje = "Monday"
horario = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

# Algoritmo
## Padaria aberta ou não
if hoje in feriados and not natal:
    padaria_aberta = False
elif hoje not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif hoje in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta: # o padrão é ser true
#    if chovendo: # short circuit, se a primeira é verdadeira não avalia o resto
#        pegar("guarda-chuva")
    if chovendo and (frio or nevando):
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuva")
        pegar("água")
    elif chovendo:
        pegar("guarda-chuva")
    ir("padaria")
    if tem("pão integral") and tem("baguete"):
        pedir(6, "pão integral")
        pedir(6, "baguete")
    elif tem("pão integral") or tem("baguete"):
        pedir(12, "qualquer um dos 2")
    else:
        pedir(6, "qualquer pão")

else:
    ficar("casa")
    comer("bolacha")


# Statements:
# - Se -> if
# - Senão, se -> elif
# - Senão -> else
# - E -> and
# - Ou -> or
# - Não -> not

# Assigments:
# - horário de abertura da padaria
# - quando a padaria está aberta

# Expressions:
# - é feriado? -> bool True, False
# - é natal?
# - é feriado E NÃO é natal? - True
# - é sabado?
# - é domingo?
# - é sábado OU é domingo?

# Actions:
# função / método / instrução
