from ai_growth_lab.valid_orders import valid_orders



def test_valid_orders():
    #preparar los datos 
    orders = [{"user_id" : "1", "amount" : 200},{"user_id" : "2", "amount" : 0}
              ,{"user_id" : "3", "amount" : 100},{"user_id" : "4", "amount" : -5}]

    #Ejecutar la función a testear 
    valid = valid_orders(orders)

    #Comprobar
    assert valid == [{"user_id" : "1", "amount" : 200},{"user_id" : "3", "amount" : 100}]