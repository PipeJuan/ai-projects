def top_users(orders):
    totals = {}

    for o in orders:
        totals[o["user_id"]] = totals.get("user_id",0)
        totals[o["user_id"]] += o["amount"]
    
    return sorted(totals, key=totals.get, reverse=True)[:5]
   