from django.urls import path
from . import views

urlpatterns = [
    path('',views.formadd, name="create category despesa"),
    path('all', views.index, name="categoria despesas"),
    path('delete/<int:id>',views.delete, name='delete despesa categoria'),
    path('edit/<int:id>',views.edit, name="edite categoria despesa"),
]