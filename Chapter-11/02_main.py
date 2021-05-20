class Employee:
    company = 'Google'
    ecode = 120

class Feelencer:
    company = 'Fiverr'
    lavle = 3
    def upgrade(self):
        self.lavle = self.lavle +1

class Programmer(Employee, Feelencer):
    name = 'Shajidur Rahman'
    
p = Programmer()
p.upgrade()
print(p.lavle)
print(p.company)