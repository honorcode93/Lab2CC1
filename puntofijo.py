#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math as ma
def PuntoFijo(g, guess, TOL):
	x0 = guess
	xi = g(x0)
	while(ma.fabs(xi-x0) > TOL):
		if xi == 0:
			break
		x0 = xi
		xi = g(x0)
	return xi
