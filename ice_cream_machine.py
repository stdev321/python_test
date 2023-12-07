class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        if not self.ingredients or not self.toppings:
            return []
        return [[ingredient, topping] for ingredient in self.ingredients for topping in self.toppings]


result = IceCreamMachine(['vanilla', 'chocolate'], ['chocolate sauce']).scoops()
print(result)