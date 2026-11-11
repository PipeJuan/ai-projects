

def valid_orders(orders):

    """totals_orders = []
    
    for a in orders:
        if a["amount"] > 0 :
            totals_orders.append(a)
        else:
            pass

    return totals_orders"""

    return[ a for a in orders if a["amount"] > 0]
    