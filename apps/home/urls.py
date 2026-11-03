from django.urls import path

from apps.home.views import HomeView, LandingView

app_name = 'home'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('inicio/', HomeView.as_view(), name='index'),
]
