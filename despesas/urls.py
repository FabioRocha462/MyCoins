from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.formsadd, name='create'),
    path('all/',views.allDespesas, name='allDespesas'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('edit/<int:id>',views.editDespesa, name='editDespesa'),
]