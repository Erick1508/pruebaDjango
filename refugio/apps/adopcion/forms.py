from django import forms
from refugio.apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):

	class Meta:
		model  = Persona

		fields = [
			'nombre',
			'apellido',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]

		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellidos',
			'edad': 'Edad',
			'telefono' : 'Telefono',
			'correo' : 'Correo electronico',
			'domicilio': 'Domicilio',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'edad' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'correo' : forms.TextInput(attrs={'class':'form-control'}),
			'domicilio' : forms.Textarea(attrs={'class':'form-control'}),
			
		}

class SolicitudForm(forms.ModelForm):
	class Meta:
		model = Solicitud
		fields = [
			'numero_mascotas',
			'razones',
		]

		labels = {
			'numero_mascotas': 'Numeros de mascotas',
			'razones': 'Razones para adoptar',
		}

		widgets = {
			'numero_mascotas': forms.TextInput(attrs={'class':'form-control'}),
			'razones': forms.Textarea(attrs={'class':'form-control'}),
		}