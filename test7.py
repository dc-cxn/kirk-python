#!/usr/bin/env python

x = int(input("Enter value for x: "))

if x == 10:
    print("jackpot, you entered 10")
elif x < 10:
    print("you entered below 10")
else:
    print("you entgered a big number")
    
ip_add_list = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']

for ip in ip_add_list:
    print('My IP is, ')
    print(ip)

#Nested for loop

ip_add_list2 = ['8.8.8.8', '8.8.4.4']

for ip in ip_add_list:
    for ip2 in ip_add_list2:
        print(ip)
        print(ip2)

# range for loop

for my_var5 in range(1,10):
    print(my_var5)

# while loop

i = 0

while i <= 5:
    print('Hello')
    i += 1

 