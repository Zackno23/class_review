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

    def entry_fee(self):
        if self.toshi < 20:
            print(1000)
        elif 60 > self.toshi >= 20:
            print(1500)
        elif self.toshi >= 65:
            print(1200)



ken = Customer('Ken', 'Tanaka', 15)
ken.full_name()
ken.age()
ken.entry_fee()
tom = Customer('Tom', 'Ford', 57)
tom.full_name()
tom.age()
tom.entry_fee()
ieyasu = Customer('Ieyasu', 'Tokugawa', 73)
ieyasu.full_name()
ieyasu.age()
ieyasu.entry_fee()
