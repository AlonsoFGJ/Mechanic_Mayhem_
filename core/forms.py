from django import forms
from .models import Empleado, SubirProyecto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField  # Asegúrate de importar ReCaptchaField desde django_recaptcha

class EmpleadoForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Empleado
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificamos el campo 'imagen' para que sea opcional
        self.fields['imagen'].required = False

class SubirProyectoForm(forms.ModelForm):  # Aquí corregimos la importación de ModelForm
    captcha = ReCaptchaField()

    class Meta:
        model = SubirProyecto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']