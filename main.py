MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def track(quantity):
    """Checks whether the resources are sufficient or not."""
    global resources
    if resources["water"] >= MENU[quantity]["ingredients"]["water"]:
        resources["water"] -= MENU[quantity]["ingredients"]["water"]
        if not quantity == "espresso":
            resources["milk"] -= MENU[quantity]["ingredients"]["milk"]
        resources["coffee"] -= MENU[quantity]["ingredients"]["coffee"]
        return
    else:
        return "Sorry there is not enough water."


def reverse(quantity):
    """Returns the resources back."""
    global resources
    resources["water"] += MENU[quantity]["ingredients"]["water"]
    if not quantity == "espresso":
        resources["milk"] += MENU[quantity]["ingredients"]["milk"]
    resources["coffee"] += MENU[quantity]["ingredients"]["coffee"]
    return


def edit():
    """Format the values into printable format"""
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"


def cost(item):
    """Checks whether sufficient money is given by user."""
    global money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = round((0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies), 2)
    if total >= MENU[item]["cost"]:
        money += MENU[item]["cost"]
        return f"Here is ${total - MENU[item]['cost']} in change.\nHere is your {item}. Enjoy!"
    else:
        return "Sorry that's not enough money. Money refunded."


money = 0


def machine():
    """Makes the desired drink for the user."""
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == "report":
        print(edit())
    elif coffee_type == "off":
        print("The Machine is turned off.")
    else:
        if not track(coffee_type) == "Sorry there is not enough water.":
            result = cost(coffee_type)
            if result == "Sorry that's not enough money. Money refunded.":
                reverse(coffee_type)
                print(result)
            else:
                print(result)
        else:
            print(track(coffee_type))
    if not coffee_type == "off":
        machine()


machine()

