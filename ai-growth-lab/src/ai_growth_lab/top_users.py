
from collections import Counter

def top_users(orders):

    totals = Counter()
    
    for o in orders:
        totals[o["user_id"]] += o["amount"]

    
    return [users for users, total in totals.most_common(5)]
    