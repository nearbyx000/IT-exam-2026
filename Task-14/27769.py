BASE = 22
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for x in range(BASE):
    s1 = f"12313{alphabet[x]}57"
    s2 = f"1{alphabet[x]}34561"
    total = int(s1, BASE) + int(s2, BASE)
    if total % 21 == 0:
        print(f"x={x}, ответ={total // 21}")
