# Initialize the coffee machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# Define the menu of available drinks and their ingredients and costs
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

# Define the coin denominations and their values
coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
    "pennies": 0.01,
}

# Function to check if there are enough resources to make the drink
def check_resources(drink):
    for ingredient in drink:
        if resources[ingredient] < drink[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

# Function to process coins and calculate the monetary value
def process_coins():
    print("Please insert coins.")
    total = 0.0
    for coin in coins:
        count = int(input(f"How many {coin}?: "))
        total += count * coins[coin]
    return round(total, 2)

# Function to make the drink
def make_drink(drink):
    for ingredient in drink:
        resources[ingredient] -= drink[ingredient]
    resources["money"] += drink["cost"]
    print(f"Here is your {choice}. Enjoy!")

# Main program loop
while True:
    # Prompt user for drink choice
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turn off the coffee machine if requested
    if choice == "off":
        break

    # Print report if requested
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    # Process drink order
    elif choice in MENU:
        drink = MENU[choice]
        if check_resources(drink):
            payment = process_coins()
            if payment < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(payment - drink["cost"], 2)
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
                make_drink(drink)
    
    # Invalid input
    else:
        print("Invalid input. Please try again.")
