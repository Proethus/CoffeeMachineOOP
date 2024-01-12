from CoffeeClass import Coffee
import math


class CoffeeMachine:
    def __init__(self):
        self.resources = {"Water": 300, "Milk": 200, "Coffee": 100, "Coins": {1: 0, 5: 0, 10: 0, 25: 0}}
        self.coffee_types = {
            "Espresso": Coffee("Espresso", 50, 18, 0, 1.50),
            "Latte": Coffee("Latte", 200, 24, 150, 2.50),
            "Cappuccino": Coffee("Cappuccino", 50, 24, 100, 3.00)
        }

    def refill_resources(self):
        for item in ["Water", "Coffee", "Milk"]:
            self.resources[item] += int(input(f"How much {item.lower()} would you like to add? "))
        for coin in [1, 5, 10, 25]:
            self.resources["Coins"][coin] += int(input(f"How many {coin}-cent coins would you like to add? "))

    def calculate_coins_value(self, coins):
        return sum(coin * coins[coin] for coin in coins) * 0.01

    def report(self):
        print("Current resources:")
        for item, amount in self.resources.items():
            if item == "Coins":
                print(f"Money: ${self.calculate_coins_value(amount)}")
                for coin, coin_amount in amount.items():
                    print(f"You have {coin_amount} pcs of ${coin * 0.01}")
            else:
                print(f"{item}: {amount} {'ml' if item in ['Water', 'Milk'] else 'g'}")

    def check_coffee_resources(self, coffee):
        return all(self.resources[item.capitalize()] >= getattr(coffee, item) for item in ["water", "coffee", "milk"])

    def make_coffee(self, coffee):
        for item in ["water", "coffee", "milk"]:
            self.resources[item.capitalize()] -= getattr(coffee, item)

    def process_order(self, order):
        money_paid = self.calculate_coins_value(order["Coins"])
        if money_paid < order["Item"].price:
            print("Insufficient funds! Abort transaction")
        else:
            if not self.check_coffee_resources(order["Item"]):
                print("Insufficient materials! Aborting transaction!")
            else:
                for coin, amount in order["Coins"].items():
                    self.resources["Coins"][coin] += amount
                self.make_coffee(order["Item"])
                change = money_paid - order["Item"].price
                for coin in [25, 10, 5, 1]:
                    if change > coin * 0.01:
                        removable_coin_amount = math.floor(change / (coin * 0.01))
                        if self.resources["Coins"][coin] > removable_coin_amount:
                            change -= removable_coin_amount * coin
                            self.resources["Coins"][coin] -= removable_coin_amount
                if change > 0:
                    print("The machine ran out of change. Sorry for the inconvenience!")
                print("Enjoy your coffee!")

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
