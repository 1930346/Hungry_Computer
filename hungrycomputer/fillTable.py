from company.models import *


def fill():

    client1 = Client(
        first_name="Juan",
        last_name="Perez",
        email="1930436@upv.edu.mx",
        phone_number=121221456,
    )
    client1.save()

    client2 = Client(
        first_name="Elen",
        last_name="Fortnite",
        email="1930126@upv.edu.mx",
        phone_number=8167541521,
    )
    client2.save()
    client3 = Client(
        first_name="Jhonessy",
        last_name="Apex",
        email="1930326@upv.edu.mx",
        phone_number=123456789,
    )
    client3.save()
    client4 = Client(
        first_name="Lament",
        last_name="Carol",
        email="1939326@upv.edu.mx",
        phone_number=834151235,
    )
    client4.save()
    client5 = Client(
        first_name="Wraith",
        last_name="Apex",
        email="1930001@upv.edu.mx",
        phone_number=12341789,
    )
    client5.save()

    #Addresses fill
    address1 = Address(
        client_id=client1,  # this is a client
        street="Paloma Real",
        interior_number=2929,
        exterior_number=2927,
        city="Victoria",
        state="Tamaulipas",
        postal_code=87130,
    )
    address1.save()

    address2 = Address(
        client_id=client2,  # this is a client
        street="Calle Sin Nombre",
        interior_number=None,
        exterior_number=1231,
        city="Victoria",
        state="Tamaulipas",
        postal_code=87000,
    )
    address2.save()

    address3 = Address(
        client_id=client3,  # this is a client
        street="Calle Sexta",
        interior_number=None,
        exterior_number=4441,
        city="Victoria",
        state="Tamaulipas",
        postal_code=87001,
    )
    address3.save()

    address4 = Address(
        client_id=client4,  # this is a client
        street="Calle Tampico",
        interior_number=1121,
        exterior_number=4442,
        city="Victoria",
        state="Tamaulipas",
        postal_code=87021,
    )
    address4.save()

    address5 = Address(
        client_id=client4,  # this is a client
        street="Calle Tampico",
        interior_number=1121,
        exterior_number=4442,
        city="Victoria",
        state="Tamaulipas",
        postal_code=87022,
    )
    address5.save()

    department1 = Department(
        name="RH",
        description="Recursos Humanos",
    )
    department1.save()

    department2 = Department(
        name="ST",
        description="Soporte Técnico",
    )
    department2.save()

    department3 = Department(
        name="MT",
        description="Mercadotecnia",
    )
    department3.save()

    department4 = Department(
        name="EB",
        description="Ensamblaje",
    )
    department4.save()

    department5 = Department(
        name="DT",
        description="Distribución",
    )
    department5.save()

    department6 = Department(
        name="AL",
        description="Almacén",
    )
    department6.save()

    department7 = Department(
        name="FN",
        description="Finanzas",
    )
    department7.save()

    #JOBS
    job1 = Job(
        title="Atencion a mepleados",
        min_salary=5000,
        max_salary=20000,
    )
    job1.save()

    job2 = Job(
        title="Atención de documentación",
        min_salary=6000,
        max_salary=10000,
    )
    job2.save()

    job3 = Job(
        title="Gestión de salarios, activos y pasivos",
        min_salary=10000,
        max_salary=20000,
    )
    job3.save()

    job4 = Job(
        title="Gestión de salario",
        min_salary=10000,
        max_salary=20000,
    )
    job4.save()

    job5 = Job(
        title="Acomodo de inventario",
        min_salary=4000,
        max_salary=7500,
    )
    job5.save()

    job6 = Job(
        title="Acomdo de productos y guías",
        min_salary=4000,
        max_salary=6500,
    )
    job6.save()

    job7 = Job(
        title="Acomdo de productos y guías",
        min_salary=4000,
        max_salary=6500,
    )
    job7.save()

    job8 = Job(
        title="Paquetería",
        min_salary=3000,
        max_salary=6500,
    )
    job8.save()

    job9 = Job(
        title="Administrador de software y herramientas",
        min_salary=10000,
        max_salary=17500,
    )
    job9.save()

    job10 = Job(
        title="Atención a clientes",
        min_salary=7000,
        max_salary=12500,
    )
    job10.save()

    job11 = Job(
        title="Diagnóstico y solución de problemas",
        min_salary=8200,
        max_salary=15500,
    )
    job11.save()

    job12 = Job(
        title="Ensamblador primario",
        min_salary=10200,
        max_salary=16500,
    )
    job12.save()

    job13 = Job(
        title="Ensamblador secundario",
        min_salary=10200,
        max_salary=14500,
    )
    job13.save()

    job14 = Job(
        title="Encargado de mercadotecnia",
        min_salary=8200,
        max_salary=11500,
    )
    job14.save()

    job15 = Job(
        title="Gerente",
        min_salary=15000,
        max_salary=30000,
    )
    job15.save()



    employee1 = Employee(
        first_name="Carlixto Eduardo",
        last_name="García Martínez",
        sex="M",
        email="1930346@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=7500.00,
        bonus=0.15,
        contract_id=1,
        department_id=department1,
        job_id=job1,
    )
    employee1.save()

    employee2 = Employee(
        first_name="Hector ",
        last_name="Varela Grimaldo",
        sex="M",
        email="1931246@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=10000.00,
        bonus=0.15,
        contract_id=2,
        department_id=department5,
        job_id=job7,
    )
    employee2.save()

    employee3 = Employee(
        first_name="Carlos Alejandro",
        last_name="Reyes Puga",
        sex="M",
        email="1938346@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=15500.00,
        bonus=0.15,
        contract_id=3,
        department_id=department4,
        job_id=job11,
    )
    employee3.save()

    employee4 = Employee(
        first_name="Sandra Anel",
        last_name="Báez Guerrero",
        sex="F",
        email="1930746@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=15500.00,
        bonus=0.15,
        contract_id=4,
        department_id=department1,
        job_id=job11,
    )
    employee4.save()

    employee5 = Employee(
        first_name="Carlos Jared",
        last_name="Ulibarrí Ruiz",
        sex="M",
        email="1930546@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=11500.00,
        bonus=0.15,
        contract_id=5,
        department_id=department7,
        job_id=job3,
    )
    employee5.save()

    employee6 = Employee(
        first_name="Orlando Samuel",
        last_name="Martínez Dorantes",
        sex="M",
        email="1930546@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=4500.00,
        bonus=0.15,
        contract_id=6,
        department_id=department6,
        job_id=job5,
    )
    employee6.save()

    employee7 = Employee(
        first_name="Irving Jael",
        last_name="Martínez Aguilar",
        sex="M",
        email="1930546@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=4500.00,
        bonus=0.15,
        contract_id=7,
        department_id=department5,
        job_id=job7,
    )
    employee7.save()

    employee8 = Employee(
        first_name="Julián Arturo",
        last_name="Barrón Gutiérrez",
        sex="M",
        email="1930546@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=4500.00,
        bonus=0.15,
        contract_id=8,
        department_id=department3,
        job_id=job13,
    )
    employee8.save()

    employee9 = Employee(
        first_name="Jesus Guadalupe",
        last_name="Rangel Turrubiates",
        sex="M",
        email="1930546@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=5500.00,
        bonus=0.15,
        contract_id=9,
        department_id=department6,
        job_id=job6,
    )
    employee9.save()

    employee10 = Employee(
        first_name="Roberto Eduardo",
        last_name="Higuera Sánchez",
        sex="M",
        email="1930546@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=10500.00,
        bonus=0.15,
        contract_id=10,
        department_id=department2,
        job_id=job1,
    )
    employee10.save()

    employee11 = Employee(
        first_name="Agustín",
        last_name="Zavala Arias",
        sex="M",
        email="1930446@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=10500.00,
        bonus=0.15,
        contract_id=11,
        department_id=department2,
        job_id=job1,
    )
    employee11.save()

    employee12 = Employee(
        first_name="José Carlos",
        last_name="Ávalos Ruíz",
        sex="M",
        email="1930351@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=10500.00,
        bonus=0.15,
        contract_id=12,
        department_id=department2,
        job_id=job1,
    )
    employee12.save()

    employee13 = Employee(
        first_name="Daniel ",
        last_name="Sánchze Sánchez",
        sex="M",
        email="1931151@upv.edu.mx",
        date_of_birth="2000-01-01",
        hire_date="2022-01-02",
        monthly_salary=10500.00,
        bonus=0.15,
        contract_id=13,
        department_id=department3,
        job_id=job13,
    )
    employee13.save()



    order = Order(
        name="orden_numero1",
        status=True,
        order_date="2020-01-01",
        delivery_date="2020-01-02",
        attendant=employee1,
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
        authorized_by=employee1,
        pickup_date="2022-04-15",
    )
    order_product.save()

    assembly_order = Assembly_order(
        attendant=employee1,
        finish_date="2020-01-01",
        description="Detalles de una pc",
        notes="El usuario le tiró agua lol",
        status=True,
        client_id=client1,
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
