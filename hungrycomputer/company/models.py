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

