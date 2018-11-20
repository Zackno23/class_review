class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        print(self.first_name + self.family_name)


ken = Customer('Ken', 'Tanaka')
ken.full_name()
tom = Customer('Tom', 'Ford')
tom.full_name()
