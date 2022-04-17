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

        # check for none in the fields
        if p_id is None or name is None or price is None or stock is None or description is None or serial_num is None or brand is None or model is None:
            return redirect(almacen_view)

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

# distribucion
def distribucion_view(request):
    context = {"Orders": Order.objects.all(), "Order Details": Order_product.objects.all()}
    return render(request, "distribucion.html", context)

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

        #Check if the fields are empty
        if employee_id is None or first_name is None or last_name is None or email is None or date_of_birth is None or hire_date is None or monthly_salary is None or bonus is None or contract_id is None or department_id is None or job_id is None:
            return redirect(recursos_humanos_view)


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


#Soporte
def soporte_view(request):
    context = {"problemas": Problem.objects.all()}
    print(context)
    return render(request, "soporte.html", context)

def delete_problem(request, id):
    if request.method == "POST":
        problem = Problem.objects.get(id=id)
        problem.delete()
    return redirect(soporte_view)

def update_problem(request):
    if request.method == "POST":
        problem_id = request.POST.get("problem_id")
        employee_id = request.POST.get("employee_id")
        type = request.POST.get("type")
        description = request.POST.get("description")
        print(problem_id, employee_id, type, description)
        if problem_id is None or employee_id is None or type is None or description is None:
            return redirect(soporte_view)
        
        try:
            problem = Problem.objects.get(id=problem_id)
            problem.employee_id = employee_id
            problem.type = type
            problem.description = description
            problem.date = problem.date
            problem.save()
        except Problem.DoesNotExist:
            print("El problema no existe")
    return redirect(soporte_view)