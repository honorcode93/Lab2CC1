import re
import math as ma

input1 = "-2x^{2} +6"
input2 = "x^{5} -5x^{2} +4"
input3 = "x^{4} -6x^{3} +12x^{2} -10x +3"

def biseccion(tol,a,b):
    while ((b-a)/2) > tol:
        c = (a+b)/2
        if f1(c)==0:
            break
        if f1(a)*f1(c)<0:
            b=c
        else:
            a=c
    print c
    return c       

def feval(fun,a): #evalua la fucniona fun en a

    funcion = fun.split(" ")
    result = 0
    for i in range(0,len(funcion)):
        xs = re.match(r"(-?\+?(\d|\d+)?x\^{(-?\d+(\.\d+)?)})",funcion[i])
        xj = re.match(r"(-?\+?(\d|\d+)?x)",funcion[i])
        if xs:
            x = xs.group(0).split("x")
            if x[0] == "":
                result += a**int(xs.group(3))
            elif x[0] == "-":  
                result += -a**int(xs.group(3))
            else:
                result += int(x[0])*a**int(xs.group(3))
        elif xj:
            result += int(x[0])*a

        else:
            if len(funcion[i].split("+")) > 1:
                xsub = re.match(r"(-?\+?(\d|\d+)?x\^{(-?\d+(\.\d+)?)})",funcion[i].split("+")[1])
                if xsub:
                    x2 = xsub.group(0).split("x")
                    if x2[0] == "":
                        result += a**int(xsub.group(3))
                    elif x2[0] == "-":  
                        result += -a**int(xsub.group(3))
                    else:
                        result += int(x[0])*a**int(xsub.group())
                else:
                    result += int(funcion[i].split("+")[1])
            else:
                result += int(funcion[i])

    print result
    return result


feval(input2,2)