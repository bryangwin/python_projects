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
    "money": 0
}

coins = {
    "quarter": 0.25,
    "dime": 0.01,
    "nickle": 0.05,
    "penny": 0.01,
}


def check_resources(choice):
    for item in MENU[choice]["ingredients"]:
        if (MENU[choice]["ingredients"][item]) > resources[item]:
            return "Sorry, we do no have that available currently."


def check_money_amount(choice, money_inserted):
    if MENU[choice]["cost"] > money_inserted:
        print("You have insufficient funds. Here is your money back.")
        return False
    elif MENU[choice]["cost"] <= money_inserted:
        change = money_inserted - MENU[choice]["cost"]
        resources["money"] += MENU[choice]["cost"]
        print(f"Your change is: ${round(change, 2)}")
        return True


def make_drink(choice):
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]
    return f"Here is your {choice}. Enjoy!"


while True:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("The machine is powering down. Goodbye")
        break

    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Mile: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${resources['money']}")
    else:
        check_resources(choice)

    money_inserted = 0.0
    print("Please insert coins.")
    hm_quarters = int(input("How many quarters? "))
    money_inserted += hm_quarters * .25
    hm_dimes = int(input("How many dimes? "))
    money_inserted += hm_dimes * .1
    hm_nickles = int(input("How many nickles? "))
    money_inserted += hm_nickles * .05
    hm_pennies = int(input("How many pennies? "))
    money_inserted += hm_pennies * .01

    money = check_money_amount(choice, money_inserted)
    if money == True:
        drink_made = make_drink(choice)
        print(drink_made)
