class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.years_old = age

    def full_name(self):
        return self.first_name + ' ' + self.family_name

    def age(self):
        years_old = self.years_old
        return years_old

    def entry_fee(self):
        if self.years_old <= 3:
            return 0
        elif self.years_old >= 75:
            return 500
        elif self.years_old < 20:
            return 1000
        elif 60 > self.years_old >= 20:
            return 1500
        elif self.years_old >= 65:
            return 1200

    def print(self):
        print(self.full_name(), self.age(), self.entry_fee(), sep=' ')


ken = Customer('Ken', 'Tanaka', 15)
ken.print()

tom = Customer('Tom', 'Ford', 57)
tom.print()

ieyasu = Customer('Ieyasu', 'Tokugawa', 73)
ieyasu.print()
