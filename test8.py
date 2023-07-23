#!/usr/bin/env python
 
ip_add_list = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']

ip_add_list2 = ['8.8.8.8', '8.8.4.4']

net_device = {'ip_addr': '192.168.1.1'}

var1 = 'vendor'
device = 'device_type'

print(net_device)

net_device[var1] = 'Cisco'
net_device[device] = 'ios'

print(net_device)

print(net_device['device_type'])

for key in net_device:
    print(key)
for value in net_device.values():
    print(value)
for k, v in net_device.items():
    print(k)
    print(v)   

