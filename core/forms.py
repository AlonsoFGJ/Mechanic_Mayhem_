from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField   
from django_recaptcha.fields import ReCaptchaField                                                                                                                      

class EmpleadoForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Empleado
        fields = '__all__'

class SubirProyectoForm(ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = SubirProyecto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    #captcha = CaptchaField()
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']                                                                                              