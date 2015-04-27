#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helper import *

def Biseccion(fun,tol,a,b):
	c = 0.0
	while ((b-a)/2) > tol:
		c = (a + b)/2
		if fun(c) == 0.0:
			print c
			return c
		if fun(a)*fun(c) < 0.0:
			b = c
		else:
			a = c
	print float(c)
	return float(c)