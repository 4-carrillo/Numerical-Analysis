"""
Examen Parcial 1

Carrillo Medina Alexis Adrian (CMAA)

Nombre del programa: Matriz.py

"""

#----- Seccion de bibliotecas

import numpy as np

#----- Codigo

# Clase con la que se trabajaran las operaciones con matrices
class Matriz(object):

    def __init__(self,n,m,Zeros=True,X=[]):
        # Metodo constructor
        # Construimos nuestra matriz de nxm 
        # Con entradas dadas por X una lista

        self.n=n
        self.m=m
        self.matrix=[]
        if(len(X)!=0): # En dado caso que no queramos una matriz de 0
            Zeros=False
        if Zeros: # Caso que queramos un matriz de 0
            for i in range(n):
                    self.matrix.append([0]*m)
        else:
            count=0 # Entero auxiliar para saber que entradas agregar
            for i in range(n):
                y=[]
                for j in range(m):
                    y.append(X[count]) # Creamos los respectivos renglones
                    count+=1
                self.matrix.append(y) # Agregamos los renglones a la matriz

    def getColumn(self):
        # Nos regresa el numero de columnas

        return self.n
    
    def getRow(self):
        # Nos regresa el numero de renglones

        return self.m

    def getElement(self,i,j):
        # Nos regresa el elemenot en la entrada (i,j)

        return self.matrix[i][j]

    def esCuadrada(self):
        # Nos dice si la matriz es cuadrada

        if(self.n==self.m):
            return True
        return False

    def changeElement(self,i,j,element):
        # Cambia la entrada (i,j) por elemento

        self.matrix[i][j]=element

    def changeRow(self,i,R):
        # Cambia todo el renglon i por R

        self.matrix[i]=R
    
    def matrizMenores(self, i, j):
        # Calcula la matriz de menores con apoyo de Numpy
        # Regresa tipo Matriz

        copia = np.copy(self.matrix) # Copiamos la matriz actual
        copia = np.delete(copia, (i), axis=0) # Quitamos la columna i
        copia = np.delete(copia, (j), axis=1) # Quitamos el renglon j
        copia=np.asarray(copia).reshape(-1) # Para obtener una lista
        nMatriz=Matriz(self.n-1,self.m-1,X=copia) # Creamos la nueva matriz
        return nMatriz

    def matrizTranspuesta(self):
        # Calcula la matriz transpuesta
        # Regresa tipo Matriz

        nMatriz=Matriz(self.m,self.n,Zeros=True)  # Creamos una matriz de 0
        for i in range(nMatriz.getColumn()):
            for j in range(nMatriz.getRow()):
                nMatriz.changeElement(i,j,self.matrix[j][i]) # Usamos la definicion de matriz transpuesta
        return nMatriz 

    def determinante(self):
        # Calcula el determinante
        # Regresa un entero

        if(not self.esCuadrada()):
            return None # Si no es cuadrada no podemos calcular el determinante

        if(self.n==2 and self.m==2):
            return self.matrix[0][0]*self.matrix[1][1]-(self.matrix[1][0]*self.matrix[0][1]) # Si es de 2x2
        else: # En otro caso
            determinante = 0 
            for i in range(self.n):
                determinante += ((-1)**i)*(self.matrix[0][i])*self.matrizMenores(0,i).determinante() # Definicion recursiva de determinante
            return determinante  

    def matrizCofactores(self):
        # Calcula la matriz de cofactores
        # Regresa tipo Matriz

        cofactores=Matriz(self.n,self.m,Zeros=True) # Matriz de 0
        for i in range(self.n):
            cofactoresRen = [] # Renglones de la matriz de cofactores
            for j in range(self.m):
                cofactoresRen.append(((-1)**(i+j)) * self.matrizMenores(i,j).determinante()) # Agregamos las entradas a los renglones
                                                                                             # con la definicion de cofactores

            cofactores.changeRow(i,cofactoresRen) # Cambiamos todo el renglos de 0 por CofactoresRen
        cofactores=cofactores.matrizTranspuesta() # Calculamos la transpuesta para obtener la matriz de cofactores
        return cofactores                 

    def matrizInversa(self):
        # Calcula matriz inversa
        # Regresa tipo Matriz

        det = self.determinante() # Determinante

        if(det==0): # En dado caso que no exista
            raise Exception("La matriz no tiene inversa")  

        if(self.n==2 and self.m==2): # Para el caso 2x2, usamos la definicion
            inversa=Matriz(2,2,Zeros=True)
            inversa.changeElement(0,0,self.matrix[1][1]/det)
            inversa.changeElement(0,1,-self.matrix[0][1]/det)
            inversa.changeElement(1,0,-self.matrix[1][0]/det)
            inversa.changeElement(1,1,self.matrix[0][0]/det)
            return inversa

        # En otro caso continua desde aqui

        inversa = self.matrizCofactores() # Matriz de cofactores

        for i in range(self.n):
            for j in range(self.m):
                inversa.changeElement(i,j,inversa.getElement(i,j)/det) # Cambiamos las entradas de la matriz de cofactores
                                                                       # Por la division entre el determinante
        return inversa


    def multiplicacionDerecha(self,matriz):
        # Calcula la multiplicacion por la derecha con Matriz
        # Regresa tipo Matriz

        multi=Matriz(self.n,matriz.m,Zeros=True) # Matriz de auxiliar de 0

        for i in range(self.n):
            for j in range(matriz.m):
                cij=0 #Entrada auxiliar
                for r in range(self.m):
                    cij+=((self.getElement(i,r))*(matriz.getElement(r,j))) # Calcula por definicion las entradas
                multi.changeElement(i,j,cij) # Agrega las entradas a la nueva matriz

        return multi

    def potencia(self,n):
        # Calcula la potencia n de la matriz
        # Regresa tipo Matriz

        if(n==0): # Si la potencia es 0 regresa la identidad
            A=Matriz(self.n,self.m,Zeros=True)
            for i in range(self.n):
                for j in range(self.m):
                    if(i==j):
                        A.changeElement(i,j,1)
            return A

        A=self
        for i in range(n-1):
            A=A.multiplicacionDerecha(self) # Aplica n veces la multiplicacion
                                            # que es la definicion de potencia n
        return A


    def toString(self):
        # Convierte a cadena

        for  i in range(self.n):
            print("[ ",end='')
            for j in range(self.m):
                print(self.matrix[i][j],end=' ')
            print("]")
