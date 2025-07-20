from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# def


def clr():
    print('\n' * 20)


# code


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_working = True


clr()


while machine_working:
    order = input(f"What would you like? {menu.get_items()}: ")
    clr()

    if order != "report" and order != "off":
        drink = menu.find_drink(order)
        if drink is not None:
            ingredients_str = " | ".join([f"{key}: {value}" for key, value in drink.ingredients.items()])
            print(f"\n{drink.name} costs ${drink.cost:.2f} ({ingredients_str})\n")

            drink_possible = coffee_maker.is_resource_sufficient(drink)
            if drink_possible and money_machine.make_payment(drink.cost):
                print(f"Payment was success. Thank you and enjoy your {drink.name}.")
                coffee_maker.make_coffee(drink)

    if order == "off":
        clr()
        print("Machine is off.\n")
        machine_working = False

    if order == "report":
        clr()
        print("Machine current state:\n")
        coffee_maker.report()
        money_machine.report()
        input("\nPress any key to continue.")
        print()
