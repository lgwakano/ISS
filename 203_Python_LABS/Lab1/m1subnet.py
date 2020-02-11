# @filename: [m1subnet]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources: https://www.aelius.com/njh/subnet_sheet.html --subnet
# https://www.w3schools.com/python/ref_func_range.asp --range
# https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists --unpacking list
# https://stackoverflow.com/questions/58013274/python-remove-leading-zeros-from-ip-addresses
# https://www.debuggex.com/cheatsheet/regex/python

network = "10.100.16.0/20"

# subnet /20 
# 4 sets of octets -> 8 + 8 + 4 + 0 = 20
# subnet bits = 4 as shown above (1111 0000)
# subnet is equal to 128 + 64 + 32 + 16 = 240
# N# of subnets = 2 ^ subnet bits
# N# of subnets = 2 ^ 4
# N# of subnets = 16 
# Range of subnets: 10.100.0.0 until 10.100.240.0 growing 16 at a time
# example: 
# 1st: 10.100.0.0
# 2nd: 10.100.16.0
# 3rd: 10.100.32.0
# 4th: 10.100.48.0
# .
# .
# .
# 16th: 10.100.240.0

networkIP = network.split('/').pop(0)
subNet = "255.255.240.0"

# iterate all possible range of subnet 0 until 15 (16 not included)
allNetworks = [netIP * 16 for netIP in range(0,16)]

#in order to iterate the list I unpack the list with the splat operator (*)

# #1st way to do it:
# #position {0} is the index
# #position {1} is the list item
# print('\n'.join('10.100.{1}.0'.format(*k) for k in enumerate(allNetworks)))

lastHost = 255
specificSubnet = 16

import re

firstSub = re.sub('\d{1,3}\.\d{1,3}\.(\d{1,3})\.\d{1,3}', str(allNetworks[0]), networkIP)
lastSub = re.sub('\d{1,3}\.\d{1,3}\.(\d{1,3})\.\d{1,3}', str(allNetworks[-1]), networkIP)

print("Subnet Network Address: {}".format(networkIP))
print("Subnet First Address: 10.100.{}.0".format(firstSub))
print("Subnet Last Address: 10.100.{}.0".format(lastSub))

broadList = networkIP.split(".")
broadList.pop()
broadList.append("255")

print("Subnet Broadcast Address: {}".format(".".join(broadList)))

print("\nAll network IPs:\n")

for net in allNetworks:
    if net == specificSubnet:
        print("\nRange of IP Address to be scanned: ")
        
    print("[", end="")
    for host in range(0,lastHost + 1):
        print("10.100.{0}.{1}".format(net, host), end="")
        if net != specificSubnet:
            print("]")
            break
        print("]") if host == lastHost else print(", ", end="")



#2nd way
#print(*("10.100.{0}.{1}".format(x, host) for x in allNetworks for host in range(0,256)), sep='\n')