class Circle:
    def __init__(self):
        self.radius = None

    def set_radius(self, rad):
        self.radius = rad

    def get_radius(self):
        return self.radius


a = Circle()
print(a.get_radius())
a.set_radius(15)
print(a.get_radius())
