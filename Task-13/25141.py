from ipaddress import ip_network

net = ip_network("46.29.170.214/255.255.128.0", 0)
for ip in net.hosts():
    oktet_list = [int(oktet) for oktet in str(ip).split(".")]
    oktet_list.sort()
    if sum(oktet_list[:3]) == oktet_list[3]:
        print(ip)
