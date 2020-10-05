import funciones
import numpy as np

def main():##son las pruebas de cada funcion
  #print("PRUEBA SUCESION FIBONACCI \n ")
  ##prueba de sucesion de fibonacci
  #r=int(input("ingrese un numero para que se le de el resultado de la funcion fibonacci \n"))
  #print(funciones.fibonacci(r))
#-------------------------------------------------------------------------------------------------
  print("PRUEBA MATRIZ INVERSA METODO CHIDO \n ")
  ##prueba de inversa de una matriz por metodo chido
  ##creamos nuestra matriz 
  n=int(input('cuantas filas quieres \n'))
  m=int(input('cuantas columnas  quieres \n'))
  A = np.zeros((n,m))      
  #llenamos la matriz 1 con los datos del usuario
  print ("Ingrese los elementos de la  matriz")
  for i in range(n):
    for j in range(m):
      A[i][j] =float(input('Elemento (%2d,%2d): ' % (i, j))) 
  print( "su matriz es:")
  print(A)
  print( "La matriz de menores es:")
  print(funciones.matrizMenores(A,0,0))
  print( "La matriz transpuesta es:")
  print(funciones.matrizTranspuesta(A))
  print( "El determinante de la matriz es:")
  print(funciones.determinant(A))
  print( "La matriz de cofactores es:")
  print(funciones.matrizCofactores(A))
  print( "La matriz inversa es:")
  print(funciones.matrizInversa(A))
  ##prueba de inversa de una matriz por metodo chafa
  #print("PRUEBA MATRIZ INVERSA METODO CHAFA \n ")
  #funciones.inversachafa()

#-------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
  main()
