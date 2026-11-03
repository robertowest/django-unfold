from django import forms
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm

class LoginForm(BaseAuthenticationForm):
    """
    Formulario de acceso compartido por todos los usuarios.

    Usa el AuthenticationForm de Django en lugar del de admin para que
    los usuarios sin is_staff también puedan iniciar sesión.
    """
