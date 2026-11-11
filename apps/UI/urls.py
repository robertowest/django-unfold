from django.urls import path

from apps.UI import views

app_name = 'ui'

urlpatterns = [
    # componentes UI
    path('button/', views.ButtonView.as_view(), name='button'),
    path('card/',   views.CardView.as_view(),   name='card'),
    path('chart/',  views.ChartView.as_view(),  name='chart'),

    path('panel/',     views.RetentionView.as_view(), name='dashboard'),
    # path('sistema/',  views.SystemView.as_view(),    name='system'),
    # path('comercio/', views.CommerceView.as_view(),  name='commerce'),
    # path('gastos/',   views.SpendingView.as_view(),  name='spending'),
    # path('pedidos/',  views.OrdersView.as_view(),    name='orders'),
    # path('form/',     views.FormsView.as_view(),     name='forms'),
]
