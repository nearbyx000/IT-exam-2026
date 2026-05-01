from ipaddress import ip_network

net = ip_network("192.168.32.160/255.255.255.240", 0)
count = 0
for ip in net:
    b_ip = f"{int(ip):032b}"
    if b_ip.count("1") % 2 == 0:
        count += 1
print(count)
# 8
