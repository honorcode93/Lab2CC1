import math as ma
from biseccion import *
from newton import *
#import newton2.py
from puntofijo import *
from secante import *
from helper import *

#Funciones
def f1(x):
	return x**2-6

def f2(x):
	return x**5-5*x**2+4

def f3(x):
	return x**4 - 6*x**3 + 12*x**2 - 10*x + 3

def f4(x):
	return ma.e**(x**2)*x

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
print "Resultado biseccion: "+str(Biseccion(f2, 10**(-5),0.5, 1.5))
print "Resultado biseccion: "+str(Biseccion(f3, 10**(-5),0.0 , 4.0))
print "Resultado biseccion: "+str(Biseccion(f4, 10**(-5), 1.0, 2.0))
print "Resultado newton: "+str(Newton(f1, f1_, 0.0, 10**(-5)))
print "Resultado newton: "+str(Newton(f2, f2_, 2.0, 10**(-5)))
print "Resultado newton: "+str(Newton(f3, f3_, 2.5, 10**(-5)))
print "Resultado newton: "+str(Newton(f4, f4_, 1.0, 10**(-5)))
print "Resultado punto fijo: "+str(PuntoFijo(g1, 0.0,10**(-5)))
print "Resultado punto fijo: "+str(PuntoFijo(g2, 2.0,10**(-5)))
print "Resultado punto fijo: "+str(PuntoFijo(g3, 2.5,10**(-5)))
print "Resultado punto fijo: "+str(PuntoFijo(g4, 1.0, 10**(-5)))