from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    # Create objects for menu, coffee maker, and money machine
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    # Run the coffee machine program
    is_on = True
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")

        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
