from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.formsadd, name='create'),
    path('all/',views.allDespesas, name='allDespesas'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('edit/<int:id>',views.editDespesa, name='editDespesa'),
    path('despesasanuais', views.despesasanuais, name='despesasanuais'),
    path('receitasanuais', views.receitasanuais, name='receitasanuais'),
    path('receitasvsdespesas', views.receitasvsdespesas, name='receitasvsdespesas'),
    path('categoriadespesa', views.categoriadespesa, name='categoriadespesa'),
    path('categoriareceita', views.categoriareceita, name='categoriareceita'),
]