class UserAccount:
    def __init__(self, name, em, pswrd):
        self.username = name
        self.email = em
        self.__password = pswrd

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        if self.__password == password:
            return True
        return False


user_one = UserAccount('Демид', "sr@mars.ru", '123')
user_one.set_password('321')
print(user_one.check_password('123'))
print(user_one.check_password('321'))
