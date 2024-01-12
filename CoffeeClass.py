class Coffee:
    def initialize(self, a_name, a_water, a_coffee, a_milk, a_price):
        self.name = a_name
        self.water = a_water
        self.coffee = a_coffee
        self.milk = a_milk
        self.price = a_price
        return self

    def to_string(self):
        print(f"Name: {self.name}")
        print(f"Water: {self.water}")
        print(f"Milk: {self.milk}")
        print(f"Coffee: {self.coffee}")
        print(f"Price: {self.price}")

    name = ""
    water = 0
    coffee = 0
    milk = 0
    price = 0
