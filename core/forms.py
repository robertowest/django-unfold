from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from unfold.widgets import BASE_INPUT_CLASSES


class LoginForm(BaseAuthenticationForm):
    """
    Formulario de acceso compartido por todos los usuarios.

    Usa el AuthenticationForm de Django en lugar del de admin para que
    los usuarios sin is_staff también puedan iniciar sesión.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # aplicamos las clases de unfold para que los campos tengan marco
        for name in ('username', 'password'):
            self.fields[name].widget.attrs['class'] = ' '.join(BASE_INPUT_CLASSES)
        self.fields['username'].widget.attrs['autofocus'] = ''
