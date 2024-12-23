with open('user_input.txt', 'a', encoding='utf-8') as file:
    data = input('Введите текст для добавления в файл "user_input.txt":\n')
    file.write(data + '\n')
with open('user_input.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("Текущее содержимое файла таково:\n", content, sep="")