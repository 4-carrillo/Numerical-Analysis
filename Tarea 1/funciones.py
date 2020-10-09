""""
Tarea # 1: Tarea1
##COMENTARIO 

integrantes:

Almaraz Garcia Iori Alejandro(AGIA)
Carrillo Medina Alexis Adrian(CMAA)

Nombre del programa:  Tarea1

"""
# ----- seccion de bibliotecas .
import numpy as np
import matplotlib.pylab as plt

# -----

#------------------------------------------------------------------------------------------------------------------------------------------------
#AGIA
##SUCESION DE FIBONACCI
def fibonacci(n):

  #Este programa calcula el n-esimo numero de fibonacci

  if n<1: #Si la n no representa un natural se lanza un excepcion
    raise Exception("El indice es invalido") 
  
  fib_n=1 #Caso base n
  fib_n_1=0 #Numero anterior al numero actual

  for i in range(int(n-1)): #Recorremos la lista hasta n-2 (Para iniciar en 1)
    tmp=fib_n #Creamos un temporal para almacener el numero actual
    fib_n=tmp+fib_n_1 #Actualizamos el numero actual con base a la regla de la sucesion
    fib_n_1=tmp #Actualizamos el numero anterior

  return fib_n #Regresamos el numero n de fibonacci

#------------------------------------------------------------------------------------------------------------------------------------------------
#CMAA Y AGIAA
##INVERSA DE UNA MATRIZ ( PUSIMOS DOS METODOS, UNO QUE RECIBE UNA MATRIZ Y OTRO DONDE LA CREA ADENTRO DEL METODO)


# metodo "CHAFA" : NO RECIBE UNA MATRIZ Y SOLO CALCULA CUANDO ES MATRIZ 2x2
def inversachafa():
  ##PROGRAMA QUE CALCULA LA INVERSA DE UNA MATRIZ SIEMPRE Y CUANDO DET!=0
  A = np.zeros((2,2))    ##creamos nuestra matriz cuadrada  con ceros 
  #llenamos la matriz 1 con los datos del usuario entrada por entrada , por esos los 2 ciclos for 
  print ("Ingrese los elementos de la  matriz")
  for i in range(2):
    for j in range(2):
      A[i][j] =float(input('Elemento (%2d,%2d): ' % (i, j))) 
  print( "su matriz es:")
  print(A)
  determinante= float(A[0][0]*A[1][1] - A[1][0]*A[0][1]) ### Calculamos el determiante ingresando al valor que tiene en esa entrada o espacio de memoria 
  if determinante !=0: 
    inversa = np.zeros((2,2))
    factor1=1/determinante 
    inversa[0][0]=factor1*A[1][1]
    inversa[0][1]=factor1*-A[0][1]
    inversa[1][0]=factor1*-A[1][0]
    inversa[1][1]=factor1*A[0][0]  
    print(f'la  matriz  inversa de una matriz cuadrada es: \n {inversa}')
    print('comprobando que es matriz inversa \n')
    print(np.dot(A,inversa)) 
  else:
    print('LO SIENTO SOLO SE CALCULAR LA MATRIZ INVERSA  DE UNA MATRIZ 2X2 CUANDO EL DETERMINANTE ES DISTINTO DE CERO')

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
## INVERSA DE UNA MATRIZ CUADRADA (SIN NUMPY(EXCEPTO PARA LA MATRIZ DE MENORES) Y CON METODOS AUXILIARES)
### Para todos los metodos estamos suponiendo que recibimos una matriz cuadrada

## --------------------------- METODO AUXILIARES --------------------------- ##
### Estos metodos solo se ejecutan si la matriz es de mas de 2x2

def matrizMenores(m, r, c):
    copia = np.copy(m)
    copia = np.delete(copia, (r), axis=0)
    copia = np.delete(copia, (c), axis=1)
    return copia

def matrizTranspuesta(m):

  #Funcion que nos regresa la matriz transpuesta de una matriz

  nMatriz=[0]*len(m) #Definimos una matriz auxiliar con len(m) ceros

  for i in range(len(m)):
    nMatriz[i]=[0]*len(m[0]) #Creamos listas,dentro de nMatriz, con len(m[i]) ceros
    for j in range(len(m[0])):
      nMatriz[i][j]=m[j][i] #Aplicamos la definicion de matriz transpuesta

  return nMatriz #Regresamos la matriz auxiliar

def determinant(m):

  #Funcion que nos regresa el determinante de una matriz

    if len(m) == 2: #Caso base
      return m[0][0]*m[1][1]-(m[0][1]*m[1][0])
    else: # Recursividad
      determinante = 0 
      for i in range(len(m)):
        determinante += ((-1)**i)*(m[0][i])*determinant(matrizMenores(m,0,i)) #Definicion de determinante recursiva
    return determinante

def matrizCofactores(m):

  #Funcion que nos regresa la matriz de cofactores

  cofactores = [] #Creamos una matriz auxiliar
  for r in range(len(m)):
      cofactoresRen = [] #Creamos una lista auxiliar que representa los renglones de la matriz de cofactores
      for c in range(len(m)): #Definicion de matriz de cofactores
          cofactoresRen.append(((-1)**(r+c)) * determinant(matrizMenores(m,r,c))) #Calculamos el determinante en dicha entrada
      cofactores.append(cofactoresRen)
  cofactores = matrizTranspuesta(cofactores) #Obtenemos la transpuesta
  return cofactores

## --------------------------- METODO PRINCIPAL --------------------------- ##

def matrizInversa(m):

  #Funcion que nos regresa la matriz inversa

  det = determinant(m) #Calculamos el determinante de la matriz

  if(det==0): #Si el determinante es cero, no existe inversa
    raise Exception("La matriz no tiene inversa") 


  if(len(m)==2):
    inversa=[[0,0],[0,0]]
    inversa[0][0]=m[1][1]/det
    inversa[0][1]=-m[0][1]/det
    inversa[1][0]=-m[1][0]/det
    inversa[1][1]=m[0][0]/det
    return np.array(inversa)

  inversa = matrizCofactores(m) #Calculamos la matriz de cofactores y la llamamos inversa

  for i in range(len(inversa)):
    for j in range(len(inversa[0])):
      inversa[i][j]=inversa[i][j]/det #Definicion de inversa
  return np.array(inversa)

#----------------------------------------------------------------------------------------------------------------------------------------------------
###DISTRIBUCION UNIFORME

def distribucion (N,M):

  #FUNCIONALIDAD

  #Semilla
  np.random.seed(2)

  ##Codigo
  lGNumeros=np.zeros(N)

  for i in range(M):
    uniforme=np.random.uniform(-1,1,N)
    for j in range(N):
      lGNumeros[j]+=(uniforme[j]/M)
  
  return lGNumeros

    
###### FIN PROGRAMA
