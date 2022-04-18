from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sform", views.simple_form, name="sform"),
    path("delete_simple_form/<int:id>", views.delete_simple_form_id, name="delete_simple_form"),
    # almacen
    path("almacen", views.almacen_view, name="almacen"),
    path("add_product", views.add_product, name="add_product"),
    path("update_product", views.update_product, name="update_product"),
    path("delete_product/<int:id>", views.delete_product, name="delete_product"),
    #Formulario Soporte
    path("formulario_soporte", views.soporte_form, name="soporte_form"),
    #ensamble
    path("ensamblaje", views.ensamble_view, name="ensamblaje"),
    path("add_assembly_order", views.add_assembly_order, name="add_assembly_order"),
    path("update_assembly_order", views.update_assembly_order, name="update_assembly_order"),
    path("delete_assembly_order/<int:id>", views.delete_assembly_order, name="delete_assembly_order"),
]
