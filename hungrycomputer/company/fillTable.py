def fill():
    o = Order(id=1, name= 'orden', status= False, attendant= 1, notes= 'nota')
    p = Product(id=1, name= 'memoria', description= 'memoria descricion', model= 'M1500', stock= 50, price= 466.50, serial_num= 'ES23456')
    op = Order_product(id=1, order_id= 1, product_id= 1, authorized_id= 1)
    a = Addresses(street="Paloma Real", interior_number=None, exterior_number=2927, city="Victoria", state="Tamaulipas", postal_code=87130)
    c = Client(first_name="Juan", last_name="Perez", phone_number=123456789, email="1930436@upv.edu.mx", address_id=a)

    a.save()
    c.save()
    o.save()
    p.save()
    op.save()
