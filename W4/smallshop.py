inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}


def process_order(inventory, cart):

    total_bill = 0

    print("---- Bill ----")

    for item in cart:

        quantity = cart[item]

        if item in inventory:

            if inventory[item]["stock"] >= quantity:

                cost = inventory[item]["price"] * quantity
                total_bill = total_bill + cost

                inventory[item]["stock"] = inventory[item]["stock"] - quantity

                print(item, "x" + str(quantity), "= NPR", cost)

            else:
                print("Sorry, not enough stock for", item)

    print("----------------")
    print("Grand Total: NPR", total_bill)

    print("\nUpdated Inventory:")
    for item in inventory:
        print(item, "=", inventory[item]["stock"])


process_order(inventory, cart)