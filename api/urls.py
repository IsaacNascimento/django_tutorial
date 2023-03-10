from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('previas/', views.previa, name="previa"),
]