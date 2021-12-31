

from math import pow, cos,sin,log

def newton_1D(fun,fundef,val,e):
	while(fun(val)>=e):
		val=val-fun(val)/fundef(val)
	return val


a=10**6
b=10
c=1
def function_first(val):
	return val**2-1

def function_mul(val):
	return 2*val
t=1e-100

def function_second(val):
	return (val-1)**4

def function_second1(val):
	return 4*((val-1)**3)

t1=1e-60
def function_third(val):
	return (val-cos(val))

def function_third1(val):
	return 1+sin(val)



t2=1e-100

print("(i):",newton_1D(function_first,function_mul,a,t))
print("(ii):",newton_1D(function_second,function_second1,b,t1))
print("(iii):",newton_1D(function_third,function_third1,c,t2))