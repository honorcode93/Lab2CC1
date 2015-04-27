#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helper import *

def Biseccion(fun, tol, a, b):
	c = 0.0
	while ((b - a)/2) > tol:
		c = (a + b)/2
		#print "[%f, %f] f(%lf) = %lf (tol_so_far: %lf)" % (a, b, c, fun(c), (b - a)/2)

		#Esta comparacion no es muy buena parece
		if fun(c) == 0.0:
			return c
		if fun(a)*fun(c) < 0.0:
			b = c
		else:
			a = c
	#print "[%f, %f] f(%lf) = %lf (tol_so_far: %lf)" % (a, b, c, fun(c), (b - a)/2)
	return float(c)