from ..models import Matricula
from .matriculas import generar_letras, validar_respuesta


# -----------
# MATRÍCULAS
# -----------

def inicializar(usuario_):

    pendiente = Matricula.objects.filter(
        usuario=usuario_,
        respuesta__isnull=True
    ).first()

    letras_ = ''

    if pendiente:
        letras_ = pendiente.letras
    else:
        letras_ = generar_letras()

        existente = Matricula.objects.filter(
            usuario=usuario_,
            letras=letras_
        ).first()

        if existente:
            return inicializar(usuario_)

        Matricula.objects.create(
            letras=letras_,
            usuario=usuario_
        
        )

    return letras_


def procesar_intento(usuario_,letras_,respuesta_):

    matricula = Matricula.objects.filter(
        usuario=usuario_,
        letras=letras_,
        respuesta__isnull=True
    ).first()

    if not matricula:
        return False, "No se ha encontrado la matrícula activa."
    

    valida, msj = validar_respuesta(letras_,respuesta_)

    if valida:
        matricula.respuesta = respuesta_
        matricula.save()
        return True, "¡Genial! " + msj
    else:
        return False, "¡Inténtalo de nuevo! " + msj
    

def saltar_matricula_activa(usuario_):
    
    Matricula.objects.filter(
        usuario=usuario_,
        respuesta__isnull=True
    ).delete()
