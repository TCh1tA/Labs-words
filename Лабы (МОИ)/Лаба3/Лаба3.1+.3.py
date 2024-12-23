par = input("Введите 'L', чтобы прочитать построчно\nВведите 'F', чтобы прочитать целиком\n")
fl = input("Введите название файла (с его типом через точку):\n")
try:
    if par == "L":
        with open(fl, 'r', encoding='utf-8') as file:
            for line in file:
                print(line) # Можно убрать "/n" в конце строки, тогда текст выведется без пропусков
    elif par == "F":
        with open(fl, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    else:
        print("НЕ ПОНИМАЮ! БЛОКИРУЮ! (неправильно выбран формат чтения)")
except(FileNotFoundError):
    print("Дорогой пользователь, такой файл не найден! Выключаюсь")
