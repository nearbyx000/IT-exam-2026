from ipaddress import ip_network

for m in range(9, 31):
    net = ip_network(f"84.23.84.23/{m}", 0)
    if str(net.network_address) == "84.23.84.0":
        print(net.netmask)
