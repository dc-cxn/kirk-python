ip_addr1 = '172.16.1.1'
ip_addr2 = '172.31.17.99'
ip_addr3 = '217.88.17.1'

print('\n')
print('-' *80)
print(ip_addr1, ip_addr2, ip_addr3)
print('\n')
print('Difference with formatting')
print('\n')
print("{:20}{:^20}{:>20}".format(ip_addr1,ip_addr2,ip_addr3))
print('\n')
print('-' * 80)

