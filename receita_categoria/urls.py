from django.urls import path
from . import views

urlpatterns = [
    path('',views.formadd, name="create category receita"),
    path('delete/<int:id>',views.delete, name="edit categoria receita"),
    path('edit/<int:id>', views.edit, name = "edit categoria receita"),
    path('all',views.index, name="all categoria receita")

]