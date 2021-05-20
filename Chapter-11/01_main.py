class Company:
    company = 'Google'
    def person(self, name, age):
        self.name = name
        self.age = age
        print(f'The Company {self.company}\nPerson {self.name}\nAge {self.age}')
shajidur = Company()
shajidur.person('shaidur', 12)

class Programmer(Company):
    lan = 'python'
    def getlan(self):
        print(f"the language is {self.lan}")
p = Programmer()
p.person('programmer', 23)
