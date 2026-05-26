from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .services.services import inicializar, procesar_intento, saltar_matricula_activa


@login_required
def inicio(request):
    """
    Esta vista se encarga de renderizar la página de inicio.
    """

    if request.method == 'POST':

        accion = request.POST.get('accion')

        if accion == 'saltar':
            saltar_matricula_activa(request.user)
            messages.info(request, "Matrícula descartada. Se han generado nuevas letras.")
            return redirect('inicio')


        respuesta_usuario = request.POST.get('respuesta')
        letras_matricula = request.POST.get('letras')
        
        valida, msj = procesar_intento(request.user, letras_matricula, respuesta_usuario)
        
        if valida:
            messages.success(request, msj)
        else:
            messages.error(request, msj)
            
        return redirect('inicio')

    letras = inicializar(request.user)

    contexto = {
        'letras': letras
    }

    return render(request, 'juego/inicio.html', contexto)


