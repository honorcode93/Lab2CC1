#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math as ma
def Newton(f, f_, guess, tol):
	x0 = guess
	if(f_(x0) == 0):
		return x0
	xi = x0 - f(x0)/f_(x0)
	while ma.fabs(x0-xi) > tol: #100 iteraciones
 	    if(xi == 0.0):
 	    	break
 	    x0 = xi
 	    if(f_(x0) == 0):
 	    	return x0
 	    xi = x0 - f(x0)/f_(x0)
	return xi