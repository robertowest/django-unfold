import json

from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from apps.UI.forms import FormularioHorizontalForm, FormularioVerticalForm
from apps.UI.services import get_commerce_context, get_orders_context, get_spending_context, get_retention_context, get_system_context

from core.views import UnfoldContextMixin


class ButtonView(UnfoldContextMixin, TemplateView):
    template_name = 'ui/button.html'
    title = _('Botones')

class CardView(UnfoldContextMixin, TemplateView):
    template_name = 'ui/card.html'
    title = _('Tarjetas')


class ChartView(UnfoldContextMixin, TemplateView):
    template_name = 'ui/chart.html'
    title = _('Gráficos')



class RetentionView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/retention.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # el layout de unfold necesita el contexto del sitio de admin
        context.update(admin.site.each_context(self.request))
        context.update(get_retention_context())
        context.update({'title': _('Panel de control')})
        return context


class SystemView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/system.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # el layout de unfold necesita el contexto del sitio de admin
        context.update(admin.site.each_context(self.request))
        context.update(get_system_context())
        context.update({'title': _('Panel de sistema')})
        return context


class CommerceView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/commerce.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # el layout de unfold necesita el contexto del sitio de admin
        context.update(admin.site.each_context(self.request))
        context.update(get_commerce_context())
        context.update({'title': _('Commerce')})
        return context


class SpendingView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/spending.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # el layout de unfold necesita el contexto del sitio de admin
        context.update(admin.site.each_context(self.request))
        context.update(get_spending_context())
        context.update({'title': _('Spending')})
        return context


class OrdersView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # el layout de unfold necesita el contexto del sitio de admin
        context.update(admin.site.each_context(self.request))
        context.update(get_orders_context())
        context.update({'title': _('Orders')})
        return context


class FormsView(LoginRequiredMixin, TemplateView):
    """
    Página de ejemplo con los formularios horizontal y vertical.
    """

    template_name = 'ui/forms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(admin.site.each_context(self.request))
        context.update({
            'title': _('Formularios'),
            'form_horizontal': FormularioHorizontalForm(),
            'form_vertical': FormularioVerticalForm(),
        })
        return context
