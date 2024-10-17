from .forms import RegistroUsuarioForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# basado en una funcion


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirige a la página principal después del registro
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro/registro.html', {'form': form})
