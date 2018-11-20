class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.toshi = age

    def full_name(self):
        print(self.first_name + self.family_name)

    def age(self):
        toshi = self.toshi
        print(toshi)


ken = Customer('Ken', 'Tanaka', 15)
ken.full_name()
ken.age()
tom = Customer('Tom', 'Ford', 57)
tom.full_name()
tom.age()
ieyasu = Customer('Ieyasu', 'Tokugawa', 73)
tom.full_name()
ieyasu.age()
