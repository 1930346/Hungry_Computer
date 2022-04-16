from django.db import models

# Create your models here.


class Problem(models.Model):
    # id omitted
    problem_type = [
        # Ser+am como los id del problema dude
        ("1", "Reparación"),
        ("2", "Mantenimiento"),
        ("3", "Instalación de software"),
        ("4", "Otro"),
    ]

    type = models.CharField(max_length=1, choices=problem_type, default="1")
    employee_id = models.IntegerField(default=0)
    description = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)



class Client(models.Model):
    # c = Client(first_name="Juan", last_name="Perez", phone_number=123456789, email="1930436@upv.edu.mx", address_id=a)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)


#Remember, no russian, na broma, el client_id debe ir en addresses, no viceversa
class Address(models.Model):
    # a = Addresses(street="Paloma Real", interior_number=None, exterior_number=2927, city="Victoria", state="Tamaulipas", postal_code=87130)
    client_id = models.ForeignKey(Client)
    street = models.CharField(max_length=255)
    interior_number = models.IntegerField(null=True)
    exterior_number = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.IntegerField()


class Job(models.Model):
    title = models.TextField(max_length=100 )
    min_salary = models.FloatField(default = 0.0)
    max_salary = models.FloatField(default = 0.0)
    

class Department(models.Model):
    departments_list = [
        ("RH", "Recursos Humanos"),
        ("ST", "Soporte Técnico"),
        ("MT", "Mercadotecnia"),
        ("EB", "Ensamblaje"),
        ("DT", "Distribución"),
        ("AL", "Almacén"),
        ("FN", "Finanzas")
    ]
    name = models.TextField(max_length=100, choices=departments_list, default = "RH")
    description = models.TextField(max_length=255)


class Employee(models.Model):
    sexes=[
        ("M","Masculino"),
        ("F","Femenino"),
        ("O","Otro")
    ]

    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    sex = models.CharField(max_length=1, choices=sexes,default="O")
    email = models.EmailField(max_length=200)
    date_of_birth = models.DateField()
    hire_date = models.DateField()
    monthly_salary  = models.FloatField(default=0.0)
    bonus = models.FloatField(default=0.0)
    contract_id = models.IntegerField(max_length = 10)
    department_id = models.ForeignKey(Department)  
    job_id = models.ForeignKey(Job)

class Order(models.Model):
    # id = models.IntegerField(default = 0, primary_key=True)
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    attendant = models.ForeignKey(Employee)
    notes = models.TextField(max_length=255)

class Product(models.Model):
    # id = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    model = models.TextField(max_length=255)
    stock = models.IntegerField()
    price = models.FloatField()
    serial_num = models.TextField(max_length=255)

class Order_product(models.Model):
    # id = models.IntegerField(default = 0, primary_key=True)
    order_id = models.ForeignKey(Order)
    product_id = models.ForeignKey(Product)
    authorized_by = models.ForeignKey(Employee)
    # authorized_id = models.IntegerField(default = 0, primary_key=True)
    pickup_date = models.DateTimeField()


class Assembly_order(models.Model):
    attendant = models.ForeignKey(Employee) #ForeignKey with Employee_id
    finish_date = models.DateTimeField()
    description = models.TextField(max_length=255)
    notes = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
    client_id = models.ForeignKey(Client)

#Para activos y pasivos
class Good(models.Model):
    description = models.TextField(max_length=255)
    value = models.FloatField(default = 0.0)
    quantity = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)
