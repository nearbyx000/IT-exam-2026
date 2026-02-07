from ipaddress import ip_network

net = ip_network("95.24.20.25/255.255.252.0", 0)
print(len(list(net.hosts())) - 11)

