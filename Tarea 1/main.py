import funciones
import numpy as np
import matplotlib.pylab as plt

def main():#son las pruebas de cada funcion

  print("PRUEBA SUCESION FIBONACCI \n ")

  # prueba de sucesion de fibonacci
  r=int(input("ingrese un numero para que se le de el resultado de la funcion fibonacci \n"))
  print("Fn=%d"%(funciones.fibonacci(r)))

#-------------------------------------------------------------------------------------------------------
  print("")
  print("PRUEBA MATRIZ INVERSA METODO CHIDO \n ")

  ## prueba de inversa de una matriz por metodo chido##

  # creamos nuestra matriz 
  n=int(input('cuantas filas quieres \n'))
  m=int(input('cuantas columnas  quieres \n'))
  A = np.zeros((n,m))      

  # llenamos la matriz 1 con los datos del usuario
  print ("Ingrese los elementos de la  matriz")
  for i in range(n):
    for j in range(m):
      A[i][j] =float(input('Elemento (%2d,%2d): ' % (i, j))) 

  print( "su matriz es:")
  print(A)
  print( "La matriz inversa es:")
  print(funciones.matrizInversa(A))

  ### prueba de inversa de una matriz por metodo chafa
  print("")
  print("PRUEBA MATRIZ INVERSA METODO CHAFA \n ")
  funciones.inversachafa() 

#-------------------------------------------------------------------------------------------------------

<<<<<<< HEAD
<<<<<<< HEAD
print("PRUEBA EJERCICIO 3")
##prueba para ejercicio 3
=======
=======
>>>>>>> d02fa95a1b5ac435e014a4822a1c4a8f378a0c01
#PRUEBA FUNCION DE DISTRIBUCION

  print("")
  print("PRUEBA FUNCION DE DISTRIBUCION \n ")
  x=[100,1000,10000]
  y=[100,200,300]

  for i in range(3):
    for j in range(3):
      print("Histograma con %d numeros aleatorios y sumados %d veces \n" %(x[i],y[j]))
      P=funciones.distribucion(x[i],y[j])
      plt.hist(P,density=True)
      plt.show()
<<<<<<< HEAD
>>>>>>> dev
=======
>>>>>>> d02fa95a1b5ac435e014a4822a1c4a8f378a0c01

if __name__ == "__main__":
  main()
