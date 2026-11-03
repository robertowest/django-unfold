from django.urls import path

from apps.UI.views import CommerceView, FormsView,RetentionView, OrdersView, SpendingView, SystemView

app_name = 'ui'

urlpatterns = [
    path('panel',     RetentionView.as_view(), name='dashboard'),
    path('sistema/',  SystemView.as_view(),    name='system'),
    path('comercio/', CommerceView.as_view(),  name='commerce'),
    path('gastos/',   SpendingView.as_view(),  name='spending'),
    path('pedidos/',  OrdersView.as_view(),    name='orders'),
    path('form/',     FormsView.as_view(),     name='forms'),
]
