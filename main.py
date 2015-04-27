import math as ma
from biseccion import *
from newton import *
#import newton2.py
from puntofijo import *
from secante import *
from helper import *

def f1(x):
	return x**2-6

def f2(x):
	return x**5-5*x**2+4

def f3(x):
	return x**4 - 6*x**3 + 12*x**2 - 10*x + 3

def f4(x):
	return ma.e**(x**2)*x

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
#PuntoFijo(g1,0.0,10**(-3))
#PuntoFijo(g2,2.0,10**(-3))
#PuntoFijo(g3,2.5,10**(-3))
#PuntoFijo(g4,1, 10**(-3))