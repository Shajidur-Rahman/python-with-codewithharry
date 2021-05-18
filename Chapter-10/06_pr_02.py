class Calculator:
    def __init__(self, number) -> None:
        self.number = number
    def squre(self):
        print(f"The value of {self.number} saqure is {self.number ** 2}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number ** 3}")
    def root(self):
        print(f"the value of {self.number} root is {self.number ** 0.5}")


a = Calculator(4)
a.squre()
a.cube()
a.root()