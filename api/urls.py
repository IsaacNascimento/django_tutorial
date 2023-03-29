from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('previas/', views.previa, name="previa"),
    path('previa-detalhe/<str:idPrevia>', views.previaDetalhe, name="previaDetalhe"),
    path('previa-detalhe/inventario/item-configuracao/<str:idConfig>', views.itemConfiguracoesDetalhe, name="itemConfiguracoesDetalhe"),
]