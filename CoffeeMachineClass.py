from CoffeeClass import Coffee
import math


class CoffeeMachine:
    def refill_resources(self):
        for item in ["Water", "Coffee", "Milk"]:
            self.resources[item] += int(input(f"How much {item.lower()} would you like to add? "))
        for a_coin in [1, 5, 10, 25]:
            self.resources["Coins"][a_coin] += int(input(f"How many {a_coin}-cent coins would you like to add? "))

    def calculate_coins_value(self, coins):
        return sum(a_coin * coins[a_coin] for a_coin in coins) * 0.01

    def report(self):
        print("Current resources:")
        for item, amount in self.resources.items():
            if item == "Coins":
                print(f"Money: ${self.calculate_coins_value(amount)}")
                for a_coin, a_amount in self.resources["Coins"].items():
                    print(f"You have {a_amount} pcs of ${a_coin * 0.01}")
            else:
                print(f"{item}: {amount} {'ml' if item in ['Water', 'Milk'] else 'g'}")

    def check_coffee_resources(self, coffee):
        return all(self.resources[item.capitalize()] >= coffee.__getattribute__(item) for item in ["water", "coffee", "milk"])

    def make_coffee(self, coffee):
        for item in ["water", "coffee", "milk"]:
            self.resources[item.capitalize()] -= coffee.__getattribute__(item)

    def process_order(self, order):
        money_paid = self.calculate_coins_value(order["Coins"])
        if money_paid < order["Item"].price:
            print("Insufficient funds! Abort transaction")
        else:
            if not self.check_coffee_resources(order["Item"]):
                print("Insufficient materials! Aborting transaction!")
            else:
                for a_coin, amount in order["Coins"].items():
                    self.resources["Coins"][a_coin] += amount
                self.make_coffee(order["Item"])
                change = money_paid - order["Item"].price
                for a_coin in [25, 10, 5, 1]:
                    if change > a_coin * 0.01:
                        removable_coin_amount = math.floor(change / (a_coin * 0.01))
                        if self.resources["Coins"][a_coin] > removable_coin_amount:
                            change -= removable_coin_amount * a_coin
                            self.resources["Coins"][a_coin] -= removable_coin_amount
                if change > 0:
                    print("The machine ran out of change. Sorry for the inconvenience!")
                print(f"Enjoy your coffee!")

    resources = {"Water": 300, "Milk": 200, "Coffee": 100, "Coins": {1: 0, 5: 0, 10: 0, 25: 0}}
    coffee_types = {"Espresso": Coffee.initialize(Coffee(), "Espresso", 50, 18, 0, 1.50),
                    "Latte": Coffee.initialize(Coffee(), "Latte", 200, 24, 150, 2.50),
                    "Cappuccino": Coffee.initialize(Coffee(), "Cappuccino", 50, 24, 100, 3.00)}

    def start(self):
        finished = False
        while not finished:
            order_name = input("Please select a product: Espresso, Latte, Cappuccino: ")
            order = {"Coins": {25: 0, 10: 0, 5: 0, 1: 0}}
            if order_name == "report":
                self.report()
            elif order_name == "refill":
                self.refill_resources()
            elif order_name in self.coffee_types:
                order["Item"] = self.coffee_types[order_name]
                order["Coins"] = {25: 0, 10: 0, 5: 0, 1: 0}
                done = False
                while not done:
                    for coin in order["Coins"]:
                        order["Coins"][coin] = int(input(f"How many ${coin * 0.01} would you like to insert?"))
                    done = input("Would you like to insert more coins? yes or no?") == "no"

                self.process_order(order)
            else:
                print("Incorrect order! Please try again!")
            finished = input("Would you like another coffee? yes or no") == "no"
