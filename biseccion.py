import re
import math as ma

input1 = "x^{2} -6"
g1 = ma.sqrt(6)
input2 = "x^{5} -5x^{2} +4"
g2 = "5x^{2} -4"
input3 = "x^{4} -6x^{3} +12x^{2} -10x +3"
g3 = "6x^{3} -12x^{2} +10x -3"

def feval(fun,a): #evalua la fucniona fun en a

    funcion = fun.split(" ")
    result = 0
    for i in range(0,len(funcion)):
        xs = re.match(r"(-?\+?(\d|\d+)?x\^{(-?\d+(\.\d+)?)})",funcion[i])
        xj = re.match(r"(-?\+?(\d|\d+)?x)",funcion[i])
        if xs:
            x = xs.group(0).split("x")
            if x[0] == "":
                result += a**float(xs.group(3))
            elif x[0] == "-":  
                result += -a**float(xs.group(3))
            else:
                result += float(x[0])*a**float(xs.group(3))
        elif xj:
            result += float(x[0])*a

        else:
            if len(funcion[i].split("+")) > 1:
                xsub = re.match(r"(-?\+?(\d|\d+)?x\^{(-?\d+(\.\d+)?)})",funcion[i].split("+")[1])
                if xsub:
                    x2 = xsub.group(0).split("x")
                    if x2[0] == "":
                        result += a**float(xsub.group(3))
                    elif x2[0] == "-":  
                        result += -a**float(xsub.group(3))
                    else:
                        result += float(x[0])*a**float(xsub.group())
                else:
                    result += float(funcion[i].split("+")[1])
            else:
                result += float(funcion[i])
    # print result
    return result

def biseccion(fun,tol,a,b):
    while ((b-a)/2) > tol:
        c = (a+b)/2
        if feval(fun,c)==0:
            print c
            return c
        if feval(fun,a)*feval(fun,c)<0:
            b=c
        else:
            a=c
    print float(c)
    return float(c)       

def PuntoFijo(gx,x0,TOL):
    i = 1
    ini = x0
    xi = 0
    exp = 1
    if isinstance(gx,float):
        xi = gx
    elif len(gx.split(" ")) == 2:
        xi = feval(gx,ini)**(1/5)
        exp = 1/5
    elif len(gx.split(" ")) > 2:
        xi = feval(gx,ini)**(1/4)
        exp = 1/4
    while i <= 100:
        if exp == 1:
            print gx
            return gx
        else:
            xi = feval(gx,ini)**exp
        dif = ma.fabs(ini-xi)
        if dif<TOL:
            print xi
            return xi 
        i = i+1
        ini = xi
    return False

biseccion(input1,10**(-5),-2,3)
biseccion(input2,10**(-5),0.5,1.5)
biseccion(input3,10**(-5),0,4)
PuntoFijo(g1,0.0,10**(-3))
PuntoFijo(g2,2.0,10**(-3))
PuntoFijo(g3,2.5,10**(-3))
