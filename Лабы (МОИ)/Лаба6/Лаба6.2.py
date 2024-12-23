class Vehicle:
    def __init__(self, mk, mo):
        self.make = mk
        self.model = mo

    def get_info(self):
        return f"Марка: {self.make}; модель: {self.model}."


class Car(Vehicle):
    def __init__(self, mk, mo, fl):
        super().__init__(mk, mo)
        self.fuel_type = fl

    def get_info(self):
        return f"Марка: {self.make}; модель: {self.model}; тип топлива: {self.fuel_type}."


a = Vehicle("Крутая", "Cамая новая")
b = Car("Похуже", "Самая новая", "Экологичный")
print(a.get_info())
print(b.get_info())
