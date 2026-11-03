from django.urls import reverse


def get_post_login_url(user):
    """
    Devuelve la url de destino tras iniciar sesión según el rol del usuario.

    - Superusuario: panel de admin de unfold, con sus permisos.
    - Staff: ejemplos de interfaz gráfica.
    - Usuario normal: página de inicio de la aplicación.
    """
    # superusuario y staff comparten panel; los permisos limitan lo visible
    if user.is_superuser:
        return reverse('admin:index')

    elif user.is_staff:
        return reverse('ui:dashboard')

    return reverse('home:index')
