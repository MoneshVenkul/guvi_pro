
import math
n=int(input())
l=math.log10(n)/math.log10(2)
#print(l)

#print(math.ceil(l))
#print(math.floor(l))
if math.ceil(l)==math.floor(l):
	print(0)
else:
	a=(n-1)//2
	#print(a)
	b=a*2
	#print(b)
	print(n-b)import math
n=int(input())
l=math.log10(n)/math.log10(2)
#print(l)

#print(math.ceil(l))
#print(math.floor(l))
if math.ceil(l)==math.floor(l):
	print(0)
else:
	a=(n-1)//2
	#print(a)
	b=a*2
	#print(b)
	print(n-b)
