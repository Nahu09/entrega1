from django import forms


class FormularioTele(forms.Form):

    nombre = forms.CharField()
    precio = forms.DecimalField(max_digits=9, decimal_places=2)

class FormularioCelular(forms.Form):

    nombre = forms.CharField()
    precio = forms.DecimalField(max_digits=9, decimal_places=2)

class FormularioNotebook(forms.Form):

    nombre = forms.CharField()
    precio = forms.DecimalField(max_digits=9, decimal_places=2)

