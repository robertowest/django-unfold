from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from core.services import get_post_login_url


class LandingView(TemplateView):
    """
    Página pública de bienvenida con acceso al sistema.
    """
    template_name = 'home/landing.html'

    def dispatch(self, request, *args, **kwargs):
        # si ya inició sesión lo enviamos a su destino; si no, mostramos la landing
        if request.user.is_authenticated:
            return redirect(get_post_login_url(self.request.user))
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(admin.site.each_context(self.request))
        context.update({
            'title': _('Bienvenido'),
            # usuarios ya logueados van directos a su destino
            'destination_url': (
                get_post_login_url(self.request.user)
                if self.request.user.is_authenticated
                else None
            ),
        })
        return context


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'

    def dispatch(self, request, *args, **kwargs):
        # si ya inició sesión lo enviamos a su destino; si no, mostramos la landing
        if request.user.is_authenticated:
            return redirect(get_post_login_url(self.request.user))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # el layout de unfold necesita el contexto del sitio de admin
        context.update(admin.site.each_context(self.request))
        context.update({'title': _('Inicio')})
        return context

