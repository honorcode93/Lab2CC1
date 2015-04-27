clear;
clc; 
 fprintf('\n metodo de Newton Rapson Modificado\n\n');
   funcion=input('Dame la funcion f(x) : ','s');
   dfuncion=input('Dame la derivada de funcion f(x) : ','s');
     d2funcion=input('Dame la segunda derivada de funcion f(x) : ','s');
        xi=input('Dame el valor inicial de x : ');
     e=input('Dame el porciento del error : ');
   ea=1000;
  c=1;
 x=xi;
while ea>e 
 g=eval(funcion);
  h=eval(dfuncion);
   k=eval(d2funcion);
     j=x-(g*h)/(h^(2)-(g*k));
   ea=abs((j-x)/j*100);
  x=j;
 c=c+1;
end
 fprintf('\n\n\n\nLa raiz exacta es: %d',j)
  fprintf('\n\nNumero de iteraciones: %d',c);