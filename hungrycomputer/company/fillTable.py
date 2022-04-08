def fill():
    o = Order(id=1, name= 'orden', status= False, attendant= 1, notes= 'nota')
    p = Product(id=1, name= 'memoria', description= 'memoria descricion', model= 'M1500', stock= 50, price= 466.50, serial_num= 'ES23456')
    op = Order_product(id=1, order_id= 1, product_id= 1, authorized_id= 1)

    o.save()
    p.save()
    op.save()
