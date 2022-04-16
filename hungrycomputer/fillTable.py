from company.models import *


def fill():

    client = Client(
        first_name="Juan",
        last_name="Perez",
        email="1930436@upv.edu.mx",
        phone_number=123456789,
    )
    client.save()

    address = Address(
        client_id=client,  # this is a client
        street="Paloma Real",
        interior_number=None,
        exterior_number=2927,
        city="Victoria",
        state="Tamaulipas",
        postal_code=87130,
    )
    address.save()

    department = Department(
        name="RH",
        description="Recursos Humanos",
    )
    department.save()

    job = Job(
        title="Programador",
        min_salary=5000,
        max_salary=20000,
    )
    job.save()

    employee = Employee(
        first_name="Elsan",
        last_name="Cudo",
        sex="M",
        email="1930346@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=15500.00,
        bonus=0.15,
        contract_id=1,
        department_id=department,
        job_id=job,
    )
    employee.save()

    order = Order(
        name="orden_numero1",
        status=True,
        order_date="2020-01-01",
        delivery_date="2020-01-02",
        attendant=employee,
        notes="nota",
    )
    order.save()

    product = Product(
        # id= 1,
        name="memoria",
        description="memoria descricion",
        brand="Asus",
        model="M1500",
        stock=50,
        price=466.50,
        serial_num="ES23456",
    )
    product.save()

    order_product = Order_product(
        # id= 1,
        order_id=order,
        product_id=product,
        authorized_by=employee,
        pickup_date="2022-04-15",
    )
    order_product.save()

    assembly_order = Assembly_order(
        attendant=employee,
        finish_date="2020-01-01",
        description="Detalles de una pc",
        notes="El usuario le tiró agua lol",
        status=True,
        client_id=client,
    )
    assembly_order.save()

    good = Good(description="Muebles", value=12500.00, quantity=10, is_active=True)
    good.save()

    problem = Problem(
        type="1",
        employee_id=1,  # Este campo no tiene una relación de llave foránea
        description="No funciona la pc",
        date="2022-04-15",
    )
    problem.save()
