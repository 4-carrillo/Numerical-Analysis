""""
Tarea # 1: Tarea1

integrantes:

Almaraz Garcia Iori Alejandro(AGIA)
Carrillo Medina Alexis Adrian(CMAA)

Nombre del programa:  Tarea1

"""
# ----- seccion de bibliotecas .
import numpy as np

# -----
#------------------------------------------------------------------------------------------------------------------------------------------------
#AGIA
##SUCESION DE FIBONACCI
def fibonacci(n):
  #este programa calcula la sucesion de fibonacci de n
  n1=int(n)
  if (n1>1):
    return fibonacci(n1-1) + fibonacci(n1-2); ## ya que la sucerion de fibonacci es f(x)=f(x-1)+f(x-2) si x>1
  elif (n1==1): ##en este caso ponemos 1 ya que f(1)=0+1
    return 1
  elif (n1==0): ##en este caso ponemos 0 ya que f(0)=0
    return 0
  else:
   print("Debes ingresar un tamaño mayor o igual a 1")
#_-----------------------------------------------------------------------------------------------------------------------------------------------
#CMAA Y AGIAA
##INVERSA DE UNA MATRIZ ( PUSIMOS DOS METODOS, UNO QUE RECIBE UNA MATRIZ Y OTRO DONDE LA CREA ADENTRO DEL METODO)


# metodo "CAFHA" : NO RECIBE UNA MATRIZ Y SOLO CALCULA CUANDO DET!=0
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
##METODO "CHIDO" : SI RECIBE UNA MATRIZ Y NO LE IMPORTA QUE EL DET!=0

def inversa(B):  ### este si recibe una matriz y no le importa que el det!=0
  if (2,2)==B.shape: ##ve si la matriz es de tamaño 2x2 
    determinante= float(B[0][0]*B[1][1] - B[1][0]*B[0][1]) ##calcula el determinante de una manera tradicional jeje
    if determinante!= 0: ##hay dos formas de calcular la matriz inversa , una es cuando determinante!=0 y otra cuando determinante=0
      inversa = np.zeros((2,2)) ##creo una matriz vacia con ceros para poder llenarla despues 
      factor=1/determinante  ## por definicion de la matriz inversa de 2x2 cuando det!=0
      inversa[0][0]=factor*B[1][1] #multiplico a cada entrada por 1/det como lo indica la definicion
      inversa[0][1]=factor*-B[0][1]
      inversa[1][0]=factor*-B[1][0]
      inversa[1][1]=factor*B[0][0]  
      print(f'la  matriz  inversa de una matriz cuadrada es: \n {inversa}')
      print('comprobando que es matriz inversa \n')
      print(np.dot(B,inversa)) ## me tiene que salir la indentidad 
    else: ##metodo cuando det=0
      print(f'Lo siento, no puedo calcular la matriz inversa, ya que el determinante de su matriz es: {determinante}')
  else:  ##es el else del primer if
    print('no es una matriz 2x2')

#----------------------------------------------------------------------------------------------------------------------------------------------------



######FIN PROGRAMA