import random

def getCargadaRandom():
    with open('cargadas_mas_parametros_de_los_debidos.txt') as f_cargadas:
        cargadas_disponibles = f_cargadas.readlines();
    # Por alguna razón no toma los caracteres especiales    
    print(cargadas_disponibles)
    randomInt = random.randint(0, len(cargadas_disponibles) - 1);
    return cargadas_disponibles[randomInt]