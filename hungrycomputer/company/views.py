from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from company.models import *


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
    print(context)
    return render(request, "almacen.html", context)


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("NombreProd")
        price = request.POST.get("PrecioProd")
        stock = request.POST.get("StockProd")
        description = request.POST.get("exampleInputNota")
        serial_num = request.POST.get("IdProd")
        model = request.POST.get("ModeloProd")
        brand = request.POST.get("MarcaProd")
        print(name, price, stock)
        product = Product(
            name=name,
            price=price,
            stock=stock,
            description=description,
            serial_num=serial_num,
            brand=brand,
            model=model,
        )
        product.save()
    return redirect(almacen_view)


def update_product(request):
    if request.method == "POST":
        p_id = request.POST.get("IdProd")
        name = request.POST.get("NombreProd")
        price = request.POST.get("PrecioProd")
        stock = request.POST.get("StockProd")
        description = request.POST.get("exampleInputNota")
        serial_num = request.POST.get("IdProd")
        brand = request.POST.get("MarcaProd")
        model = request.POST.get("ModeloProd")
        print(name, price, stock)

        try:
            product = Product.objects.get(id=p_id)
            product.name = name
            product.price = price
            product.stock = stock
            product.description = description
            product.serial_num = serial_num
            product.brand = brand
            product.model = model
            product.save()
        except Product.DoesNotExist:
            print("El producto no existe")
    return redirect(almacen_view)


def delete_product(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        product.delete()
    return redirect(almacen_view)


#Soporte Formulario
def soporte_form(request):
    print(Problem.objects.all())
    if request.method == "POST":
        id = request.POST.get("id")
        problema = request.POST.get("problema")
        descripcion = request.POST.get("descripcion")
        print(id, problema, descripcion)
        problem = Problem(employee_id= id, type= problema, description= descripcion)
    return render(request, "fromEmpleado.html")

#Finanzas
def finanzas_view(request):
    context = {"goods": Good.objects.all(),
                "employees": Employee.objects.all(),
                "departments": Department.objects.all()}

    return render(request, "finanzas.html", context)


#Recursos Humanos
def recursos_humanos_view(request):
    context = {"empleados": Employee.objects.all()}
    print(context)
    return render(request, "recursos humanos.html", context) 

def delete_employee(request, id):
    if request.method == "POST":
        employee = Employee.objects.get(id=id)
        employee.delete()
    return redirect(recursos_humanos_view)

def update_employee(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        date_of_birth = request.POST.get("date_of_birth")
        hire_date = request.POST.get("hire_date")
        monthly_salary = request.POST.get("monthly_salary")
        bonus = request.POST.get("bonus")
        contract_id = request.POST.get("contract_id")
        department_id = request.POST.get("department_id")
        job_id = request.POST.get("job_id")
        print(first_name, last_name, monthly_salary)
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.first_name = first_name
            employee.last_name = last_name
            employee.email = email
            employee.date_of_birth = date_of_birth
            employee.hire_date = hire_date
            employee.monthly_salary = monthly_salary
            employee.bonus = bonus
            employee.contract_id = contract_id
            employee.department_id = Department.objects.get(id=department_id)
            employee.job_id = job_id = Job.objects.get(id=job_id)
            employee.save()
        except Employee.DoesNotExist:
            print("El empleado no existe")
    return redirect(recursos_humanos_view)