from django.db import models

# Create your models here.

class Problems(models.Model):
    #id omitted
    problem_type = [
        #Ser+am como los id del problema dude
        ('1', "Reparación"),
        ('2', "Mantenimiento"),
        ('3', "Instalación de software"),
        ('4', "Otro"),
    ]

    type = models.CharField(max_length=1, choices=problem_type, default='1')
    employee_id = models.IntegerField(default = 0)
    description = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)



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

class Employee(models.Models):
    sexes=[
        ("M","Masculino"),
        ("F","Femenino"),
        ("O","Otro")
    ]

    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    sex = models.CharField(max_length=1, choices=sexes,default="O")
    email = models.EmailField(max_length=200)
    birthdate = models.DateField()
    hire_date = models.DateField()
    monthly_salary  = models.FloatField(default=0.0)
    bonus = models.FloatField(default=0.0)
    contract_id = models.IntegerField(max_length = 10)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)  
    job_id = models.ForeignKey(Job,on_delete=models.CASCADE)
