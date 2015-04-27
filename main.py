import math as ma
import numpy as np
from biseccion import *
from newton import *
#import newton2.py
from puntofijo import *
from secante import *
from helper import *
import matplotlib.pyplot as plt
import scipy as s
import scipy.special as ss
# from sympy import *

#Funciones
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

# print "Resultado biseccion: "+str(Biseccion(f1, 10**(-5),-2,3))
# print "Resultado biseccion: "+str(Biseccion(f2, 10**(-5),0.5,1.5))
# print "Resultado biseccion: "+str(Biseccion(f3, 10**(-5),0,4))
# print "Resultado biseccion: "+str(Biseccion(f4, 10**(-5), 1.0, 2.0))
# print "Resultado C Taylor: " +str(Taylor(f5,ma.pi,ma.pi/2))
# print Taylor2()
#PuntoFijo(g1,0.0,10**(-3))
#PuntoFijo(g2,2.0,10**(-3))
#PuntoFijo(g3,2.5,10**(-3))
#PuntoFijo(g4,1, 10**(-3))
#=======
#Derivadas
def f1_(x):
	return 2*x

def f2_(x):
	return 5*x**4-10*x

def f3_(x):
	return 4*x**3-18*x**2+24*x-10

def f4_(x):
	return ma.e**(x**2)+(2*x**2)*ma.e**(x**2)

#x - g = 0
def g1(x):
	return ma.sqrt(6)

def g2(x):
	return (5*x**2-4)**(1/5)

def g3(x):
	return (6*x**3-12*x**2+10*x-3)**(1/4)

def g4(x):
	return ma.sqrt(ma.log1p(x))	

print "Resultado biseccion: "+str(Biseccion(f1, 10**(-5),-2.0, 3.0))
print "Resultado biseccion: "+str(Biseccion(f2, 10**(-5), 0.5, 1.5))
print "Resultado biseccion: "+str(Biseccion(f3, 10**(-5), 0.0 , 4.0))
print "Resultado biseccion: "+str(Biseccion(f4, 10**(-5), 1.0, 2.0))
print "================================================="
print "Resultado newton: "+str(Newton(f1, f1_, 0.0, 10**(-5)))
print "Resultado newton: "+str(Newton(f2, f2_, 2.0, 10**(-5)))
print "Resultado newton: "+str(Newton(f3, f3_, 2.5, 10**(-5)))
print "Resultado newton: "+str(Newton(f4, f4_, 1.0, 10**(-5)))
print "================================================="
print "Resultado punto fijo: "+str(PuntoFijo(g1, 0.0,10**(-5)))
print "Resultado punto fijo: "+str(PuntoFijo(g2, 2.0,10**(-5)))
print "Resultado punto fijo: "+str(PuntoFijo(g3, 2.5,10**(-5)))
print "Resultado punto fijo: "+str(PuntoFijo(g4, 1.0, 10**(-5)))
print "================================================="
print "Resultado punto fijo modificado: "+str(PuntoFijoModificado(g1, 0.0,10**(-5),1/2))
print "Resultado punto fijo modificado: "+str(PuntoFijoModificado(g2, 2.0,10**(-5),1/2))
print "Resultado punto fijo modificado: "+str(PuntoFijoModificado(g3, 2.5,10**(-5),1/2))
print "Resultado punto fijo modificado: "+str(PuntoFijoModificado(g4, 1.0, 10**(-5),1/2))# con 4 caga el logaritmo
print "Mejor Valor Posible Para M : 1/2"	
print "================================================="
print "|g*(x)|: "+str(ma.fabs(f1(PuntoFijoModificado(g1, 0.0,10**(-5),1/2)))) + " < 1 => Converge"
print "|g*(x)|: "+str(ma.fabs(f2(PuntoFijoModificado(g2, 2.0,10**(-5),1/2)))) + " < 1 => Converge"
print "|g*(x)|: "+str(ma.fabs(f3(PuntoFijoModificado(g3, 2.5,10**(-5),1/2)))) + " < 1 => Converge"
print "|g*(x)|: "+str(ma.fabs(f4(PuntoFijoModificado(g4, 1.0, 10**(-5),1/2)))) + " > 1 => Diverge"
print "================================================="
print "Resultado secante: "+str(Secante(f1, -2.0, 3.0, 10**(-8)))
print "Resultado secante: "+str(Secante(f2, 0.5, 1.5, 10**(-8)))
print "Resultado secante: "+str(Secante(f3, 0.0, 4.0, 10**(-8)))
print "Resultado secante: "+str(Secante(f4, 1.0, 2.0, 10**(-8)))
print "================================================="
print "Resultado C Taylor: " +str(Taylor(f5,ma.pi,ma.pi/2))
Taylor2()
# print ss.ellipk(((2*(1-16*x**2)**(1/2))/((1-16*x**2)**(1/2)-1-8*x**2))**(1/2))	
