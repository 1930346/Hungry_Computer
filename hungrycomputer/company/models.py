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


class Address(models.Model):
    # a = Addresses(street="Paloma Real", interior_number=None, exterior_number=2927, city="Victoria", state="Tamaulipas", postal_code=87130)
    street = models.CharField(max_length=255)
    interior_number = models.IntegerField(null=True)
    exterior_number = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.IntegerField()


class Client(models.Model):
    # c = Client(first_name="Juan", last_name="Perez", phone_number=123456789, email="1930436@upv.edu.mx", address_id=a)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
