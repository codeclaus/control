from django.shortcuts import render, redirect
from .forms import FormularioCliente
# Create your views here.


def formularioCliente(request):
    datos = FormularioCliente()
    if request.method == 'POST':
        datos = FormularioCliente(data=request.POST)
        if datos.is_valid():
            nombre = request.POST.get('nombre')
            direccion = request.POST.get('direccion')
            email = request.POST.get('email')
            comentarioqueja = request.POST.get('queja')
            return redirect("home")

    return render(request, "forms/formulario.html", {"all_data": datos})
