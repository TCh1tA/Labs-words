class Employee:
    def __init__(self, name, idd):
        # super().__init__()
        self.name = name
        self.id = idd

    def get_info(self):
        return f'Имя сотрудника: {self.name}, ID сотрудника: {self.id}'


class Manager(Employee):
    def __init__(self, name='', idd='', dep=''):
        super().__init__(name, idd)
        self.department = dep

    def manage_projects(self):
        return "Проекты проверены!"

    def get_info(self):
        return f'Имя сотрудника: {self.name}, ID сотрудника: {self.id}, его специализация: {self.department}'


class Technician(Employee):
    def __init__(self, name='', idd='', spec=''):
        super().__init__(name, idd)
        self.specialization = spec

    def perform_maintenance(self):
        return "Тех. обслуживание выполнено!"

    def get_info(self):
        return f'Имя сотрудника: {self.name}, ID сотрудника: {self.id}, его специализация: {self.specialization}'


class TechManager(Manager, Technician):
    def __init__(self, name, idd, spec, dep):
        super().__init__(name, idd, dep)
        super().__init__(name, idd, spec)
        self.workers = []

    def add_employee(self, pers):
        if type(pers) in [Manager, Employee, Technician]:
            self.workers.append(pers)
            return 'Success'
        return f'Error! {pers} is not a worker'

    def get_team_info(self):
        i = 1
        for el in self.workers:
            print(i, el.get_info())
            i += 1


a1 = TechManager('Андрей', '1', 'Главный', 'Высокий')
a2 = Manager('Анатоль', '2', 'Высокий')
a3 = Technician('Оммлет', '3', 'Ком. мастер')
a4 = Employee('Дудс', '256')
# print(type(a2) == Manager)
print(a2.manage_projects())
print(a3.perform_maintenance())
print(a1.manage_projects())
print(a1.get_info())
print(a4.get_info())
print(a2.get_info())
print(a1.add_employee(a2))
print(a1.add_employee(a3))
print(a1.add_employee(a4))
print(a1.add_employee('Абоба'))
a1.get_team_info()
