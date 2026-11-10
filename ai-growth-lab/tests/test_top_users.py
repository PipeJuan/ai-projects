from ai_growth_lab.top_users import top_users

def test_usuario_repetido_suma_sus_montos():
    # 1. Preparar: lista de dicts con "user_id" y "amount".
    #    Haz que un usuario aparezca 2 veces.
    orders = [{"user_id" : "MX_1", "amount" : 200},{"user_id" : "MX_2", "amount" : 50},{"user_id" : "MX_1", "amount" : 200},{"user_id" : "MX_3", "amount" : 10}]

    # 2. Ejecutar
    resultado = top_users(orders)

    # 3. Verificar: ¿qué lista de user_id esperas, en qué orden?
    #    Calcúlalo a mano antes de correr el test.
    assert resultado == ["MX_1", "MX_2","MX_3"]



def test_usuario_lista_vacia():
    #preparar
    orders = []
    
    #ejecutar
    resultado = top_users(orders)

    #probar
    assert resultado == []


def test_top_five():
    #preparar
    orders = [{"user_id" : "MX_1", "amount" : 200},{"user_id" : "MX_2", "amount" : 50},{"user_id" : "MX_1", "amount" : 200},{"user_id" : "MX_3", "amount" : 10}
              ,{"user_id" : "MX_4", "amount" : 15},{"user_id" : "MX_5", "amount" : 12},{"user_id" : "MX_6", "amount" : 2}]
    
    
    #ejecutar
    resultado = top_users(orders)

    #probar
    assert resultado == ["MX_1","MX_2","MX_4","MX_5","MX_3"]