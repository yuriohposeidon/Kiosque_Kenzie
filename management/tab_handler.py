from menu import products

def calculate_tab(tables):
    new_tables = 0
    for item in tables:
        for product in products:
            if item["_id"] == product["_id"]:
                new_tables += product["price"] * item["amount"]
    subtotal = {"subtotal": f"${round(new_tables, 2)}"}

    return subtotal    