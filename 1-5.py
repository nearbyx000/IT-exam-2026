# Задача 1: Максимальное R при N ≤ 1234567 (двоичная система)
def task1():
    max_n = 1234567
    n_binary = bin(max_n)[2:]  # Убираем '0b'

    if max_n % 2 == 0:
        r_binary = '10' + n_binary
    else:
        r_binary = n_binary + '01'

    r = int(r_binary, 2)
    print(f"Задача 1:")
    print(f"N = {max_n}")
    print(f"N в двоичной: {n_binary}")
    print(f"R в двоичной: {r_binary}")
    print(f"R = {r}")
    print()
    return r


# Задача 2: Максимальное N, при котором R < 35
def task2():
    limit = 35
    max_n = 0

    for n in range(1, 100):
        n_binary = bin(n)[2:]
        digit_sum = n_binary.count('1')

        if digit_sum % 2 == 0:  # Сумма чётная
            r_binary = '10' + n_binary[2:] + '0'
        else:  # Сумма нечётная
            r_binary = '11' + n_binary[2:] + '1'

        r = int(r_binary, 2)

        if r < limit:
            max_n = n
            print(f"N = {n}, двоичная: {n_binary}, сумма цифр: {digit_sum}, R = {r}")

    print(f"\nЗадача 2:")
    print(f"Максимальное N = {max_n}")
    print()
    return max_n


# Задача 3: Минимальное N, при котором R = 123
def task3():
    target = 123
    target_binary = bin(target)[2:]
    print(f"Задача 3:")
    print(f"R = {target}, R в двоичной: {target_binary}")

    # Разбираем двоичную запись R
    # Находим где заканчиваются единицы и начинаются нули
    ones_count_binary = ""
    zeros_count_binary = ""

    i = 0
    while i < len(target_binary) and target_binary[i] == '1':
        ones_count_binary += '1'
        i += 1

    zeros_count_binary = target_binary[i:]

    ones_count = int(ones_count_binary, 2) if ones_count_binary else 0
    zeros_count = int(zeros_count_binary, 2) if zeros_count_binary else 0

    print(f"Количество единиц: {ones_count} (в двоичной: {ones_count_binary})")
    print(f"Количество нулей: {zeros_count} (в двоичной: {zeros_count_binary})")

    # Минимальное N с ones_count единицами и zeros_count нулями
    # Минимум достигается когда все единицы слева, все нули справа
    n_binary = '1' * ones_count + '0' * zeros_count
    n = int(n_binary, 2)

    print(f"Минимальное N в двоичной: {n_binary}")
    print(f"Минимальное N = {n}")
    print()
    return n


# Задача 4: Максимальное N, при котором R < 1100 (восьмеричная система)
def task4():
    limit = 1100
    max_n = 0
    max_r = 0

    for n in range(1, 500):
        n_octal = oct(n)[2:]  # Убираем '0o'
        digit_sum = sum(int(d) for d in n_octal)

        if digit_sum % 2 == 0:  # Сумма чётная
            first_digit = n_octal[0]
            r_octal = first_digit + n_octal + first_digit
        else:  # Сумма нечётная
            last_digit = n_octal[-1]
            r_octal = n_octal + last_digit

        r = int(r_octal, 8)

        if r < limit:
            max_n = n
            max_r = r

    print(f"Задача 4:")
    print(f"Максимальное N = {max_n}")
    print(f"N в восьмеричной: {oct(max_n)[2:]}")
    print(f"R = {max_r}")
    print()
    return max_n


# Задача 5: Минимальное N, при котором R > 168 (троичная система)
def to_ternary(n):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return ''.join(reversed(digits))


def from_ternary(s):
    return int(s, 3)


def task5():
    limit = 168

    for n in range(1, 100):
        n_ternary = to_ternary(n)

        if n % 2 == 0:  # N чётное
            r_ternary = '1' + n_ternary + '00'
        else:  # N нечётное
            digit_sum = sum(int(d) for d in n_ternary)
            digit_sum_ternary = to_ternary(digit_sum)
            r_ternary = n_ternary + digit_sum_ternary

        r = from_ternary(r_ternary)

        if r > limit:
            print(f"Задача 5:")
            print(f"Минимальное N = {n}")
            print(f"N в троичной: {n_ternary}")
            print(f"R в троичной: {r_ternary}")
            print(f"R = {r}")
            print()
            return n

    return None


# Задача 6 (автомат): Минимальное число при обработке которого автомат выдаст 12116
def task6():
    target = 12116

    for n in range(1, 100000):
        # Вычисляем квадрат суммы наибольшей и наименьшей цифры
        digits = [int(d) for d in str(n)]
        max_digit = max(digits)
        min_digit = min(digits)
        result = (max_digit + min_digit) ** 2

        # Производим цифр = 8 * 2^2 + 4 = 64
        product = 1
        for d in digits:
            product *= d

        calculation = 8 * (2 ** 2) + product

        if calculation == target:
            print(f"Задача 6:")
            print(f"Минимальное N = {n}")
            print(f"Произведение цифр: {product}")
            print(f"Результат: {calculation}")
            print()
            return n

    return None


# Запуск всех задач
if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    # task6()  # Если нужна задача 6