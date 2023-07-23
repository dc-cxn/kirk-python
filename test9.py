def print_ip():
    print('My IP is 10.1.1.1')
    
print_ip()

def print_ip2(ip_addr):
    print('My IP is:  {}'.format(ip_addr))

print_ip2('10.10.10.10')

def print_ip3(ip_addr, user, password):
    print('My IP is:  {}'.format(ip_addr))
    print(user)
    print(password)

print_ip3(ip_addr ='10.10.10.10',user = 'admin', password ='test123')

my_list = ['120.2.2.2', 'admin', 'test2345']

print_ip3(*my_list)

my_dict = {
    'ip_addr' : '30.30.30.30',
    'user': 'amin30',
    'password': 'test9876'
}

print_ip3(**my_dict)