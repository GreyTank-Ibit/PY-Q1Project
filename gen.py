from pyscript import display, document

def confirm_info(e):

    document.getElementById("output1").innerHTML = ""

    customer_name = document.getElementById("input1").value
    requested_items = document.getElementById("input2").value

    display(f"Customer Name: {customer_name}", target="output1")
    display(f"Requested Items: {requested_items}", target="output1")


def create_order(e):

    prod1 = document.getElementById("item1")
    qty1 = document.getElementById("qty1")
    prod2 = document.getElementById("item2")
    qty2 = document.getElementById("qty2")
    prod3 = document.getElementById("item3")
    qty3 = document.getElementById("qty3")
    prod4 = document.getElementById("item4")
    qty4 = document.getElementById("qty4")
    prod5 = document.getElementById("item5")
    qty5 = document.getElementById("qty5")

    extra1 = document.getElementById("upsize")
    extra2 = document.getElementById("extra_ketchup")
    extra3 = document.getElementById("w/o_Veggies")

    subtotal = (
        float(prod1.value) * prod1.checked * int(qty1.value)
        + float(prod2.value) * prod2.checked * int(qty2.value)
        + float(prod3.value) * prod3.checked * int(qty3.value)
        + float(prod4.value) * prod4.checked * int(qty4.value)
        + float(prod5.value) * prod5.checked * int(qty5.value)
        + float(extra1.value) * extra1.checked
        + float(extra2.value) * extra2.checked
        + float(extra3.value) * extra3.checked
    )

    tax_rate = 0.12
    tax = subtotal * tax_rate
    grandtotal = subtotal + tax

    document.getElementById("output2").innerHTML = f'''
    Subtotal: Php{subtotal:.2f} <br>
    Tax: Php{tax:.2f} <br>
    Total: Php{grandtotal:.2f} <br>
    Thank you for your order!<br>
    Please come again.
    '''


def show_order(e):

    document.getElementById("output3").innerHTML = ""

    customer_name = document.getElementById("input1").value
    requested_items = document.getElementById("input2").value

    display(
        f"Order Details: Customer Name: {customer_name}, Requested Items: {requested_items}",
        target="output3"
    )
