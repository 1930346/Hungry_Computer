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
    #distribucion
    path("distribucion", views.distribucion_view, name="distribucion"),
    path("add_order", views.add_order, name="add_order"),
    path("update_order", views.update_order, name="update_order"),
    path("delete_order/<int:id>", views.delete_order, name="delete_order"),
    path("add_order_product", views.add_order_product, name="add_order_product"),
    path("update_order_product", views.update_order_product, name="update_order_product"),
    path("delete_order_product/<int:id>", views.delete_order_product, name="delete_order_product"),
    #Formulario Soporte
    path("formulario_soporte", views.soporte_form, name="soporte_form"),
    #finanzas
    path("finanzas", views.finanzas_view, name="finanzas"),
    path("update_salary",views.update_salary, name="update_salary"),
    #Recursos humanos
    path("recursos_humanos", views.recursos_humanos_view, name="recursos_humanos"),
    path("delete_employee/<int:id>", views.delete_employee, name="delete_employee"),
    path("update_employee", views.update_employee, name="update_employee"),
    #Soporte Vista tabla
    path("soporte", views.soporte_view, name="soporte"),
    path("delete_problem/<int:id>", views.delete_problem, name="delete_problem"),
    path("update_problem", views.update_problem, name="update_problem"),
    #Home
    path("home", views.home_view, name="home"),
    #Mercadotecnia
    path("mercadotecnia", views.mercadotecnia_view, name="mercadotecnia"),
]
