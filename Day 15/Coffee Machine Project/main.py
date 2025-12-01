MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resources_sufficient(order_ingredients):
    """Returns True if drink can be made, False otherwise."""
    for item, required in order_ingredients.items():
        if required > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins(drink_cost):
    """Return total money inserted, showing remaining balance each step."""
    print(f"The drink costs ${drink_cost}. Please insert coins.")
    total = 0

    coins = [
        ("quarters", 0.25),
        ("dimes", 0.10),
        ("nickles", 0.05),
        ("pennies", 0.01),
    ]

    for coin_name, value in coins:
        count = int(input(f"How many {coin_name}? "))
        total += count * value
        total = round(total, 2)

        if total < drink_cost:
            remaining = round(drink_cost - total, 2)
            print(f"Total inserted: ${total} — still need ${remaining}...")
        else:
            break

    return total


def is_transaction_successful(payment, drink_cost):
    """Returns True if enough money was paid, handles refund/change."""
    global profit

    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(payment - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")

    profit += drink_cost
    return True


def make_coffee(drink_name, ingredients):
    """Deduct resources & serve the drink."""
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")


# ---------------------------- MAIN LOOP ------------------------------- #

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources.get('milk', 0)}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins(drink["cost"])
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

    else:
        print("Invalid option. Please choose espresso/latte/cappuccino.")
