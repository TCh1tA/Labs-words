def check(data):
    if type(data) == type("Строка"):
        return data + " - это определённо строка!"
    return str(data) + " - это не строка :("
