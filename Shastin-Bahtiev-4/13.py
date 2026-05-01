net = ("192.168.32.48/255.255.255.192", 0)

count = 0
for ip in net:
    b_ip = f"{int(ip):032b}"
    if b_ip.count("1") % 2 == 0:
        if b_ip.count("1") % 4 != 0:
            count += 1


print(count)
