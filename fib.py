#!/usr/bin/python
print("Please put n:")
n = input()

f1 =1
f2 =1
fn =0

if n==1 :
	print(f1)
elif n==2:
	print(f2)
else :
	for i in range(0,n-2) :
		fn = f1 + f2
		f1=f2
		f2=fn

	print "F(n): %d" %fn



