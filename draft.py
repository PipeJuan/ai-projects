#result de dic vacio 
orders = []
totals = {}
for o in orders:
    totals[o["user_id"]] = totals.get("user_id",0)
    totals[o["user_id"]] += o["amount"]
