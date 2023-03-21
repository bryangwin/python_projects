from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True



while is_on:
    items = menu.get_items()
    order = input(f"What item would you like to order: {items}: ").lower()
    if order not in items:
        print("Sorry, this is not a valid input, please try again.")
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        print("The machine is powering down. Goodbye.")
        is_on = False
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) == True:
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
  