import math as ma
import numpy as np
from biseccion import *
from newton import *
#import newton2.py
from puntofijo import *
from secante import *
from helper import *
import matplotlib.pyplot as plt
# from sympy import *

def f1(x):
	return x**2-6

def f2(x):
	return x**5-5*x**2+4

def f3(x):
	return x**4 - 6*x**3 + 12*x**2 - 10*x + 3

def f4(x):
	return ma.e**(x**2)*x

def f5(x):
	return ma.cos(x)

def Taylor(f,x,x0):
 	return ma.acos(((f(x) - f(x0) - dercos(x0,1)*(x-x0) )*2)/((x-x0)**2))

# def derivada(f,n):
# 	return diff(cos(x),x,n) CON LIBRERIA SYMPY DERIVADA ENESIMA EN X DE COS(X)

def dercos(x,n):
	if n == 1:
		return -ma.sin(x)
	elif n == 2:
		return -ma.cos(x)

def Taylor2():
	s = np.arange(-0.75,0.8,0.1)
	x = s.tolist() 

	for i in range (0,len(x)):
		x[i] = round(x[i],2)

	x.append(0.8)
	y = [0]*len(x)

	for i in range(0,len(x)):
		y[i] = Taylor(f5,x[i],ma.pi/2)

	plt.plot(x,y)
	plt.ylabel("C(x)")
	plt.xlabel("X")
	plt.title("Expansion de Taylor C(X)")
	plt.show()

input1 = "x^{2} -6"
g1 = ma.sqrt(6)
input2 = "x^{5} -5x^{2} +4"
g2 = "5x^{2} -4"
input3 = "x^{4} -6x^{3} +12x^{2} -10x +3"
g3 = "6x^{3} -12x^{2} +10x -3"
input4 = "e^{x^{2}}x"
g4 = "e^{-x^{2}}"

print "Resultado biseccion: "+str(Biseccion(f1, 10**(-5),-2,3))
print "Resultado biseccion: "+str(Biseccion(f2, 10**(-5),0.5,1.5))
print "Resultado biseccion: "+str(Biseccion(f3, 10**(-5),0,4))
print "Resultado biseccion: "+str(Biseccion(f4, 10**(-5), 1.0, 2.0))
print "Resultado C Taylor: " +str(Taylor(f5,ma.pi,ma.pi/2))
print Taylor2()
#PuntoFijo(g1,0.0,10**(-3))
#PuntoFijo(g2,2.0,10**(-3))
#PuntoFijo(g3,2.5,10**(-3))
#PuntoFijo(g4,1, 10**(-3))