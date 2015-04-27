#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
