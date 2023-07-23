#! 
ip_addr1 = '172.16.1.1'
ip_addr2 = '172.31.17.99'
ip_addr3 = '217.88.17.1'

octets = ip_addr1.split('.')


print('\n')
print('-' *80)
print('\n')
print(octets)
print('\n')
print('Difference with formatting')
print('\n')
print("{:10}{:^10}{:^10}{:^10}".format(*octets))
print('\n')
print('-' * 80)
print(f"My IP address is: {ip_addr1} or maybe {ip_addr2}")
print('\n')
