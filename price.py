class Bike:
    def __init__(self,Color,Price):
        self.color = Color
        self.price = float(Price)
    def getColor(self):
        return self.color
    def getPrice(self):
        return self.price
testOne = Bike('blue',89.99)
testTwo = Bike('purple',25.0)
getOne = testOne.getColor()
print(getOne)
