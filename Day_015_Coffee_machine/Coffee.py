import coffee_data

resources = coffee_data.resources

def drink_selection():
    valid_choices = ["espresso", "latte", "cappuccino", "off", "report"]
    drink = ""

    while drink not in valid_choices:
        drink = input("What would you like? (espresso/latte/cappuccino): ")

        if drink not in valid_choices:
            print("Invalid choice. Please try again.")

    print(f"you selected: {drink}")
    return drink


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Drink cost: {round(drink_cost, 2)}. You inserted {round(money_received, 2)}."
              f"You are short {round(drink_cost - money_received, 2)}. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ️. Enjoy!")


is_on = True

while is_on:
    drink_choice = drink_selection()

    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = coffee_data.MENU[drink_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink_choice, drink["ingredients"])








