from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
latte = MenuItem("latte", 200, 150, 24, 2.5)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
end_of_game = False


# print(latte)
while not end_of_game:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        end_of_game = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)


