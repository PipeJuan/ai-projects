

def valid_orders(orders):

    totals_orders = []
    
    for a in orders:
        try : 
            if a["amount"] > 0 :
                totals_orders.append(a)
        except KeyError:
            print("No hay dato para: ",a)
        except TypeError:
            print("Dato equivocado para: ",a)

    return totals_orders

    #return[ a for a in orders if a["amount"] > 0]
    