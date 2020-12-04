from data import MENU, resources


def get_total_amount():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total_amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    total_amount = round(total_amount, 2)
    return total_amount


def process_order(milk, water, coffee, price):

    resources["milk"] -= milk
    resources["water"] -= water
    resources["coffee"] -= coffee
    resources["money"] += price


def get_coffee(coffee_type):
    order_price = MENU[coffee_type]["cost"]
    order_milk = MENU[coffee_type]["ingredients"]["milk"]
    order_water = MENU[coffee_type]["ingredients"]["water"]
    order_coffee = MENU[coffee_type]["ingredients"]["coffee"]

    if order_water > resources["water"]:
        print("\tSorry there is not enough water.")
        return True
    elif order_milk > resources["milk"]:
        print("\tSorry there is not enough milk.")
        return True
    elif order_coffee > resources["coffee"]:
        print("\tSorry there is not enough coffee.")
        return True

    total_amount = get_total_amount()

    if total_amount < order_price:
        print("\tSorry that's not enough money. Money refunded.")
    else:
        change = round(total_amount - order_price, 2)
        process_order(order_milk, order_water, order_coffee, order_price)
        print(f"\tHere is {change} in change.")
        print(f"\tHere is your {coffee_type} ☕️. Enjoy!")
    return True


def get_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    return True


def shutdown():
    print("Shutting down......")
    return False


def coffee_machine():
    run_machine = True
    while run_machine:
        user_choice = input("\tWhat would you like? (espresso/latte/cappuccino): ")
        if user_choice == "espresso":
            run_machine = get_coffee(user_choice)
        elif user_choice == "latte":
            run_machine = get_coffee(user_choice)
        elif user_choice == "cappuccino":
            run_machine = get_coffee(user_choice)
        elif user_choice == "report":
            run_machine = get_report()
        elif user_choice == "off":
            run_machine = shutdown()
        else:
            print("Invalid input!!")
            break


coffee_machine()
