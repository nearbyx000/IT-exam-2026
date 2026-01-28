from itertools import product
alphabet = sorted("ГРАНИТ")

number = 1


for i in product(alphabet, repeat=6):
    word = "".join(i)
    cond_number = (number % 2 != 0)
    cond_start = (word[0] not in "АИГ")

    cond_count = (word.count("А") == 1)


    if cond_number and cond_start and cond_count:
        print(f"Номер: {number}, Слово: {word}")
        break

    number += 1