import math as m
def secante(fun,a,b,tol):
	print "Método de la secante\n\n"
	i = 1
	fa = feval(fun, a)
	fb = feval(fun, b)
	xs = b - ((b - a) / (fb - fa))*fb
	error = m.fabs(b - a)
	 
	print "Iter. \t a \t \t b \t \t Xs \n"
	print i, a, b, xs
	 
	while (error >= tol):
	    b = a
	    a = xs
	    fb = feval(fun,b)
	    fa = feval(fun,a)
	    xs = b - ((b - a)/(fb - fa))*fb
	    error = abs(b - a)
	    i = i + 1
	    fprintf('%2i \t %f \t %f \t %f \n', i, a, b, xs)
	w = feval(fun,xs)
	print "La mejor aproximación a la raiz tomando una tolerancia de " + tol + "es \n x = " + xs +"con \n f(x) ="+
	w +"\n y se realizaron " + i + "iteraciones"
	

def feval(fun,a):

	funcion = fun.split(" ")
	result = 0

	for i in range(0,len(funcion)):

		if( funcion[i] == "(x|X)\^{\d}"):

			result += a**d #reemplazar a y elevarlo
		else:
			result += funcion[i]

	return result