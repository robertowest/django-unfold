from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _

from core.services import get_post_login_url

from core.forms import LoginForm


class UnfoldContextMixin:
    """
    Inyecta el contexto del admin de Unfold (menú lateral, usuario, título) en cualquier vista.
    """
    title = 'título no definido'

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        # reutilizamos el contexto del admin site para que base de unfold pinte el menú
        context = super().get_context_data(**kwargs)
        context.update(admin.site.each_context(self.request))
        context['title'] = self.get_title()
        return context


class UnfoldLoginView(UnfoldContextMixin, LoginView):
    """
    Login con la pantalla de unfold para todos los usuarios.
    """
    template_name = 'admin/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    title = _('Iniciar sesión')

    def get_success_url(self):
        # respetamos el parámetro next si es seguro, si no decidimos por rol
        return self.get_redirect_url() or get_post_login_url(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_path'] = self.request.get_full_path()
        return context
