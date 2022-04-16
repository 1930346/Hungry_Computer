from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from company.models import Problem, Product


def index(request):
    # return HttpResponse("Hello, world. DUDE .")
    registro = Problem.objects.get(id=1)
    print(registro)
    context = {"registro": registro}
    return render(request, "index.html", context)


def simple_form(request):
    if request.method == "POST":
        description = request.POST.get("description")
        inputO = request.POST.get("inputO")
        print(description, inputO)

    return render(request, "simple_form.html")


def delete_simple_form_id(request, id):
    if request.method == "POST":
        print(f"example of deleting some id: {id}")
    return redirect(simple_form)


# ALMACEN
def almacen_view(request):
    context = {"products": Product.objects.all()}
    return render(request, "almacen.html", context)


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        print(name, price, quantity)
        product = Product(name=name, price=price, quantity=quantity)
        product.save()
    return redirect(almacen_view)


def update_product(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        print(name, price, quantity)
        product = Product.objects.get(id=id)
        product.name = name
        product.price = price
        product.quantity = quantity
        product.save()
    return redirect(almacen_view)


def delete_product(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        product.delete()
    return redirect(almacen_view)
