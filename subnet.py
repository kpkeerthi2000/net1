import math
x = input('Hosts : ')
x = int(x) + 2 
p = math.ceil(math.log2(float(x)))
x = 2**p
if x <= 256:
	print('Subnet Mask : 255.255.255.'+str(256-x))
elif x <= 65536:
	print('Subnet Mask : 255.255.'+str(256-(x//256))+'.0')
else:
	print('Subnet Mask : 255.'+str(256-(x//65536))+'.0.0')
print('Number of Subnets : '+str(2**(32-p)))
print('Nearest Hosts per network : '+str(x-2))


