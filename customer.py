class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.toshi = age

    def full_name(self):
        return self.first_name + self.family_name

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


ken = Customer('Ken', 'Tanaka', 15)
print(f'{ken.full_name()}, {ken.age()}, {ken.entry_fee()}')

tom = Customer('Tom', 'Ford', 57)
print(f'{tom.full_name()}, {tom.age()}, {tom.entry_fee()}')

ieyasu = Customer('Ieyasu', 'Tokugawa', 73)
print(f'{ieyasu.full_name()}, {ieyasu.age()}, {ieyasu.entry_fee()}')
