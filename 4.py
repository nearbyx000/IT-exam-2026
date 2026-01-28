import hashlib

# Исходное слово
word = 'алгебра'

# Кодируем в байты и вычисляем хеш
hash_object = hashlib.sha256(word.encode())

# Получаем шестнадцатеричную строку
hex_dig = hash_object.hexdigest()

print(hex_dig)
