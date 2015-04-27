def newtown(m):
	n=0
	x=1

	while n<=100: #100 iteraciones
 	    y=x-(((x**2)-m)/(2*x))
        x=y
        n=n+1
	return x