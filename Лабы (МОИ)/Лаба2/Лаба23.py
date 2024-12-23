def is_prime(number):
    number_root = int(number ** 0.5) + 1
    for i in range(2, number_root):
        if (number % i == 0) and (number != 2):
            return False
    if number != 1:
        return True
    else:
        return False


print(4, is_prime(4))
print(13, is_prime(13))
print(2137683, is_prime(2137683))
