class Employee:
    company = 'Google'
    selary = 1000
    def bonus(self, bonus):
        self.bonus = bonus
        print(f"The total selary is {self.selary + self.bonus}")
e = Employee()
e.bonus(23)