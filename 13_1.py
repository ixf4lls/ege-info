from ipaddress import *

net = ip_network('10.48.96.0/255.255.240.0', 0)
cnt = 0

for ip in net:
    ipb = f'{ip:b}'
    if ipb.count('1') > ipb.count('0'):
        cnt +=1 

print(cnt)