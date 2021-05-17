class Programmer:
    company = 'Microsoft'

    def __init__(self, name, product) -> None:
        self.name = name
        self.product = product

    def getinfo(self):
        print(
            f"The name of the programmer is {self.name} and he is working with {self.product}")


shajidur = Programmer('Shaidur Rahman', 'windows 10')
harry = Programmer('harris khan', 'skype')

shajidur.getinfo()
harry.getinfo()
