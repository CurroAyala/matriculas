'''
GESTIÓN DE MATRÍCULAS Y VERIFICACIÓN DE RESPUESTAS
'''

import random

from spellchecker import SpellChecker


# -----------
# CONSTANTES
# -----------
letras = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'Z')

corrector = SpellChecker(language='es')


# --------
# MÉTODOS
# --------
def obtener_letra():
    return random.choice(letras)


def generar_letras():
    res = ''

    while len(res) < 3:
        nuevaLetra = obtener_letra()

        if nuevaLetra not in res:
            res += nuevaLetra

    return res


def validar_respuesta(letras,respuesta):

    letras = letras.strip().lower()
    respuesta = respuesta.strip().lower()

    res = True
    msj = "Palabra válida."

    if respuesta not in corrector:
        res = False
        msj = "La palabra no existe en español."
    else:
        for letra in letras:

            if letra not in respuesta:
                res = False
                msj = "La palabra no contiene las todas letras de la matrícula."
                break

            restoRespuesta = respuesta.partition(letra)[2]
            if restoRespuesta != '':
                restoLetras = letras.partition(letra)[2]

                if restoLetras != '':
                    for letra in restoLetras:
                        if letra not in restoRespuesta:
                            res = False
                            msj = "Las letras de la matrícula no aparecen en el orden correcto."
                            break

    return (res,msj)