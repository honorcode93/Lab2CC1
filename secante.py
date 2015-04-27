#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as m
def secante(fun,a,b,tol):
	print "Método de la secante\n\n"
	i = 1
	fa = fun(a)
	fb = fun(b)
	xs = b - ((b - a) / (fb - fa))*fb
	error = m.fabs(b - a)
	 
	print "Iter. \t a \t \t b \t \t Xs \n"
	print i, a, b, xs
	 
	while (error >= tol):
	    b = a
	    a = xs
	    fb = fun(a)
	    fa = fun(b)
	    xs = b - ((b - a)/(fb - fa))*fb
	    error = m.fabs(b - a)
	    i = i + 1
	w = fun(xs)
	print "La mejor aproximación a la raiz tomando una tolerancia de " + tol + "es \n x = " + xs +"con \n f(x) ="+w+"\n y se realizaron " + i + "iteraciones"