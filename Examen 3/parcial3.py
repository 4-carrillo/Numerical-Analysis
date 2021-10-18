"""
Examen Parcial 3

Carrillo Medina Alexis Adrian (CMAA)

Nombre del programa: Parcial3.py

"""

#----- Seccion de bibliotecas

import numpy as np
import matplotlib.pyplot as plt

#----- Codigo
# La validacion se encuentra en el metodo main

#---------- Metodos auxiliares -----------

def sustDelante(A,b):
    # Vector auxiliar para la solucion
    sol=np.zeros([b.shape[0],b.shape[1]])
    
    # Definicion de substitucion hacia adelante
    for i in range(b.shape[1]):
        # sol=bi
        sol[0,i]=b[0,i]
        for j in range(0,i):
            # bi - sum_0^i lij*yj = x
            sol[0,i]-=A[i,j]*sol[0,j]
        # x/lii
        sol[0,i]/=A[i,i]
    return sol
    
def sustAtras(A,b):
    # Vector auxiliar para la solucion
    sol=np.zeros((b.shape[0],b.shape[1]))

    # Definicion de substitucion hacia atras
    for i in range(b.shape[1]-1,-1,-1):
        # sol=bi
        sol[0,i]=b[0,i]
        for j in range(i+1,b.shape[1]):
            # yi - sum_i+1^n-1 = x
            sol[0,i]-=A[i,j]*sol[0,j]
        # x/uii
        sol[0,i]/=A[i,i]

    return sol

#---------- 1.1 --------------------------

# Funcion Auxiliar para transponer un vector
def TransposeVector(A):
    New=[]
    
    for i in range(A.shape[0]):
        New.append(A[i,0])

    New=np.array(New)
    return New

def factQR(A):
    # Dimension de A
    ren,col=A.shape

    # Matriz auxiliar de 0
    Q=np.matrix(np.zeros((ren,col)))
    R=np.matrix(np.zeros((col,col)))

    for i in range(col):
        # Primera columna
        Q[:,i]=A[:,i]

        for j in range(i):
            # Substraemos del vector Ai su coeficiente en la direccion Qi
            R[j,i]=TransposeVector(Q[:,j]) * A[:,i]
            Q[:,i]-=R[j,i] * Q[:,j]

        # Normalizamos
        R[i,i]=np.linalg.norm(Q[:,i],2)
        Q[:,i]=Q[:,i]/R[i,i]

    return Q,R

#---------- 1.2 --------------------------

def cholesky(A):
    # Dimension de A
    ren,col=A.shape

    # Matriz auxiliar de 0
    L=np.matrix(np.zeros((ren,col)))

    for k in range(ren):
        for i in range(k+1):
            # Suma auxiliar 1
            sum1=0

            if(k==i):
                # Suma auxiliar 2
                sum2=0
                for j in range(k):
                    sum2+=L[k,j]**2

                # Primera formula para diagonales
                L[k,k]=np.sqrt(A[k,k]-sum2)
            else:
                for j in range(i):
                    sum1=L[i,j]*L[k,j]
                
                # Segunda formula para entradas debajo de la diagonal
                L[k,i]=(A[k,i]-sum1)/L[i,i]
    
    # Metodo auxiliar para guardar la transpuesta de L en L
    for k in range(1,ren):
        for i in range(col):
            if(i!=k):
                if (L[k,i]!=0):
                    L[i,k]=L[k,i]


    return L

#---------- 2.1 --------------------------
def minimos (A,b):
    # Definimos el sistema solucionar
    NewA=np.matmul(A.T,A)
    Newb=np.matmul(A.T,b)

    # Cholesky para obtener la solucion
    L=cholesky(NewA)

    # Solucion 1
    y=sustDelante(L,Newb)

    # Solucion 2
    x=sustAtras(L,y)

    return x

#---------- 2.2 --------------------------
def ecuacion(alfa,beta,x):
    # Regresamo el valor de x en la ecuacion
    return alfa + beta*x


#---------- 2.3 --------------------------
def grafMinimos(A,b):
    # Solucionamos el sistema
    sol=minimos(A,b)
    alfa=sol[0][0]
    beta=sol[0][1]

    # Apartir de b
    # Obtenemos los valores de x
    vals=[]
    for i in range(A.shape[0]):
        vals.append(A[:,1][i,0])
    vals=np.array(vals)

    # Vector auxiliar
    x=np.linspace(0,7,20)

    # Valores de la recta
    y5=ecuacion(alfa,beta,5)
    y6=ecuacion(alfa,beta,6)
    y=ecuacion(alfa,beta,x)

    # Graficamos
    plt.plot(x,y,label="Ajuste por minimos")
    plt.plot(5,y5,"o",label="x = 5",)
    plt.plot(6,y6,"o",label="x = 6")
    plt.plot(vals,b,"o",label="Valores")

    plt.legend(shadow=True)

    plt.show()

#---------- Metodo Main ------------------
def main():

    # Validacion 1.1 ----------
    A=np.matrix([[(int)(np.random.uniform(1,80)) for i in range(3)],
                [(int)(np.random.uniform(1,80)) for i in range(3)],
                [(int)(np.random.uniform(1,80)) for i in range(3)]])

    Q,R=factQR(A)
    Result=np.dot(Q,R)

    for i in range(len(A)):
        for j in range(len(A[0])):
            assert  np.round(Result[i,j],0)==A[i,j]

    # Pruebas
    print("\n Prubas: descomposicion QR")
    print("\n Q")
    print(Q)
    print("\n R")
    print(R)
    print("\n A original")
    print(A)
    print("\n A por QR")
    print(Result)

    # Validacion 1.2 ----------
    
    A=np.matrix([[6,15,55],[15,55,225],[55,225,979]])
    L=cholesky(A)

    Ltest = np.linalg.cholesky(A)
    LTranspose=Ltest.T

    Ltrue=Ltest+LTranspose

    for i in range(Ltrue.shape[0]):
        for j in range(Ltrue.shape[1]):
            if(i==j):
                Ltrue[i,j]/=2

    for i in range(Ltrue.shape[0]):
        for j in range(Ltrue.shape[1]):
            assert L[i,j]==Ltrue[i,j]
    
    LNew=np.matrix(np.zeros((L.shape[0],L.shape[1])))
    LTransposeNew=np.matrix(np.zeros((L.shape[0],L.shape[1])))
    

    for i in range(L.shape[0]):
        for j in range(L.shape[1]):
            if(i==j):
                LTransposeNew[i,j]=L[i,j]
                LNew[i,j]=L[i,j]
            else:
                if(j > i):
                    LTransposeNew[i,j]=L[i,j]
                else:
                    LNew[i,j]=L[i,j]

    newA = np.matmul(LNew,LTransposeNew)

    for i in range(L.shape[0]):
        for j in range(L.shape[1]):
            assert np.round(newA[i,j],0)==A[i,j]

    # Pruebas
    print("\n Pruebas: Descomposicion cholesky")
    print("\n Matriz A")
    print(A)
    # La verdadera matriz tiene a L.T 
    # Como parte de sus entradas
    print("\n Matriz Cholesky L")
    print(LNew)

    # Validacion 2.1 ----------
    A=np.matrix([[1,1],[1,2],[1,3],[1,4]])
    b=np.array([20.73,20.77,19.90,18.73])
    
    sol=minimos(A,b)
    solTest=np.linalg.lstsq(A,b,rcond=None)   

    for i in range(sol.shape[1]):
        assert np.round(sol[0,i],6)==np.round(solTest[0][i],6)

    # Pruebas
    print("\n Matriz A")
    print(A)
    print("\n Vector b")
    print(b)
    print("\nValores de la recta por minimos cuadrados")
    print(sol)

    # Validacion 2.2 ----------
    y=ecuacion(1,1,1)
    assert y==2

    # Pruebas
    print("\n Valor de y")
    print(y)

    # Validacion 2.3 ----------
    grafMinimos(A,b)

if __name__=='__main__':
    main()