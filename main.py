from pyscript import document, display

def generate_sku(e):

    document.getElementById("output").innerHTML = " "

    category_variable = document.getElementById("category").value
    product_name_variable = document.getElementById("product").value
    stock_qty = document.getElementById("stock").value

    SKU_name_here = category_variable[:3].upper() + "-" + product_name_variable[:4].upper() + "-" + str(stock_qty)

    display("Your SKU: " + SKU_name_here, target="output")