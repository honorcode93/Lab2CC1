#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as m
def Secante(fun,a,b,tol):
	x0 = a
	x1 = b
	if(fun(x1) - fun(x0) == 0.0):
		return 0.0
	xn = x1 - (fun(x1)*(x1-x0)/(fun(x1)-fun(x0)))
	while (m.fabs(b - a) >= tol):
		if(fun(xn) == 0.0):
			break
		x0 = x1
		x1 = xn
		if(fun(x1) - fun(x0) == 0.0):
			return 0.0
		xn = x1 - (fun(x1)* (x1-x0)/(fun(x1)-fun(x0)))
	return xn