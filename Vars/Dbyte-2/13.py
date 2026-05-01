from ipaddress import ip_network
count = 0
net = ip_network("116.192.155.16/255.255.255.0",0)
for ip in net:
    binary_ip = f"{ip:b}"
    if binary_ip[-1] == binary_ip[-2]:
        count +=1

print(count)
