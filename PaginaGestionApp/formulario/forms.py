

from django import forms


class FormularioCliente(forms.Form):
    nombre = forms.CharField(required=True, max_length=30, label="nombre")
    direccion = forms.CharField(
        max_length=40, required=True, label="direccion")
    email = forms.EmailField(required=False, label="email")
    queja = forms.CharField(label="comentarioqueja", max_length=1000,
                            required=True, widget=forms.Textarea)
