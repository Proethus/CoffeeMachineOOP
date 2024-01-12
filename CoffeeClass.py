class Coffee:
    def __init__(self, name, water, coffee, milk, price):
        self.name = name
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.price = price

    def to_string(self):
        print(f"Name: {self.name}")
        print(f"Water: {self.water}")
        print(f"Milk: {self.milk}")
        print(f"Coffee: {self.coffee}")
        print(f"Price: {self.price}")
