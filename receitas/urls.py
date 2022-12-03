from django.urls import path
from . import views

urlpatterns = [
    path('create', views.receitaadd, name='receita create'),
    path('all',views.allreceitas, name='receita all'),
    path('delete/<int:id>',views.delete,name='receita delete'),
    path('edit/<int:id>',views.edit,name='edit Receitas'),
]