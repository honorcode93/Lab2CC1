#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import math as ma

#Regex que detecta otras cosas
#((-?\+?[\d+|e]?[x|e]?)\^\{([^\)]+)\}){1}

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
            print "x[0]: "+x[0]
        elif xj:
            print "x[0]: "+x[0]
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