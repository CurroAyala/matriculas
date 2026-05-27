from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .services.services import inicializar, procesar_intento, saltar_matricula_activa, obtener_total, obtener_rankin, obtener_coleccion


# ---------
# REGISTRO
# ---------

def registro(request):
    """
    Esta vista gestiona la creación de nuevos usuarios.
    """
    
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()
            
            login(request, usuario)
            messages.success(request, f"¡Cuenta creada con éxito! Bienvenido, {usuario.username}.")
            
            return redirect('inicio')
    else:

        form = UserCreationForm()

    contexto = {
        'form': form
    }
    return render(request, 'registration/registro.html', contexto)


# -----------------
# PÁGINA PRINCIPAL
# -----------------

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


# -------------
# ESTADÍSTICAS
# -------------

@login_required
def estadisticas(request):

    rankin = obtener_rankin()
    total = obtener_total(request.user)
    coleccion = obtener_coleccion(request.user)

    contexto = {
        'rankin': rankin,
        'total': total,
        'coleccion': coleccion
    }

    return render(request, 'juego/estadisticas.html', contexto)