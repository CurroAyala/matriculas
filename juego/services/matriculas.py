'''
GESTIÓN DE MATRÍCULAS Y VERIFICACIÓN DE RESPUESTAS
'''

import random

from spellchecker import SpellChecker


# -----------
# CONSTANTES
# -----------
letras = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z')

corrector = SpellChecker(language='es')


# --------
# MÉTODOS
# --------
def obtener_letra():
    return random.choice(letras)


def generar_matricula():
    res = ''

    while len(res) < 3:
        nuevaLetra = obtener_letra()

        if nuevaLetra not in res:
            res += nuevaLetra

    return res


def verificar_respuesta(matricula,respuesta):

    matricula_ = matricula.strip().lower()
    respuesta_ = respuesta.strip().lower()

    res = True
    msj = "Palabra válida"

    if respuesta_ not in corrector:
        res = False
        msj = "La palabra no existe en español"
    else:
        for letra in matricula_:

            if letra not in respuesta_:
                res = False
                msj = "La palabra no contiene las todas letras de la matrícula"
                break

            restoRespuesta = respuesta_.partition(letra)[2]
            if restoRespuesta != '':
                restoMatricula = matricula_.partition(letra)[2]

                if restoMatricula != '':
                    for letra in restoMatricula:
                        if letra not in restoRespuesta:
                            res = False
                            msj = "Las letras de la matrícula no aparecen en el orden correcto"
                            break

    return (res,msj)