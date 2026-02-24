from ipaddress import ip_network

net = ip_network("172.45.129.10/255.240.0.0",0)

for ip in net:
    print((net)[-2])

