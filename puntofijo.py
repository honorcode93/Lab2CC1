 def PuntoFijo(aprox ini, TOL, No,f, g):
 	i = 1
 	while i <= No:
 		p = g(po) #(Donde g es la función de punto fijo)
 		if|f(p)|<TOL:
 			return p 
 		i = i+1
 		po = p
 	return False