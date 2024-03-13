from menu import products

def get_product_by_id(id) -> dict | str:
    if type(id) is not int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type_param) -> dict | str:
    if type(type_param) is not str:
        raise TypeError("product type must be a str") 
    new_product = []
    for product in products:

        if product["type"] == type_param:
            new_product.append(product)
           
    return new_product

def add_product(menu, **kwargs) -> dict: 
    new_product = kwargs
    new_id = 0
    for product in menu:
        
        if new_id < product["_id"]: 
            new_id = product["_id"]

    new_product["_id"] = new_id +1

    menu.append(new_product)

    return new_product

def menu_report():
    length =  len(products)
    sum_product = 0
    type_product = []
    type_string = ""
    type_count = 0

    for product in products:
        sum_product += product["price"]
        type_product.append(product["type"])
    
    for list_type in type_product:
        if type_count < type_product.count(list_type):
            type_count = type_product.count(list_type)
            type_string = list_type         
            
    sum_total = round(sum_product / length, 2)

    return f"Products Count: {length} - Average Price: ${sum_total} - Most Common Type: {type_string}"