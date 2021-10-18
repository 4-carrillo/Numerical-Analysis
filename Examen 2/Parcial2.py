"""
Examen Parcial 2

Carrillo Medina Alexis Adrian (CMAA)

Nombre del programa: Parcial2.py

"""

#----- Seccion de bibliotecas

import numpy as np
import math

#----- Codigo

# funcion f1
def f1(x1, x2):
    return 2*x1-x2-math.e**(-x1)

# funcion f2
def f2(x1, x2):
    return -x1+2*x2-math.e**(-x2)

# denominador de la matriz jacobiana
def denominador(x1,x2):
    return 3+2*math.e**(-x2)+2*math.e**(-x1)+math.e**(-x1-x2)

# parcial (en este caso la parcial de f1 y f2 es la misma)
def par(x):
    return 2+math.e**(-x)

'''Metodo de Newton para sistemas
   de ecuaciones no lineales
   aprox: es la primera aproximacion
   en forma de vector'''
def JimyNewtron(aprox):
    # contador de iteraciones
    n = 0 
    while n <= 100: # maximo numero de iteraciones 100
        '''es necesario calcular la matriz jacobiana
        y para ello se necesita una matriz vacia de 2x2'''
        jacobinv = np.zeros([2,2])
        
        # valores de la matriz jacobiana en todas sus entradas
        jacobinv[0][0] = par(aprox[1])/denominador(aprox[0], aprox[1])
        jacobinv[0][1] = 1/denominador(aprox[0], aprox[1])
        jacobinv[1][0] = 1/denominador(aprox[0], aprox[1])
        jacobinv[1][1] = par(aprox[0])/denominador(aprox[0], aprox[1])
    
        # guarda la evalucion de f1 y f2 en forma de vector
        fx = np.array(aprox)
        fx[0] = f1(aprox[0], aprox[1])
        fx[1] = f2(aprox[0], aprox[1])
        
        # FORMA ITERATIVA DEL METODO DE NEWTON PARA SISTEMAS NO LIENALES
        aprox = aprox - np.matmul(jacobinv, fx)
        
        # se incrementa el contador
        n+=1
    
    # El valor devuelto es la aproximacion
    return aprox    

#---------- 1.1.1 ------------------------
# La validacion se encuentra en el metodo main

def norma1(vec):
    # Devuelve la norma 1 de vec
    Norm=0
    for i in range(len(vec)):
        # Sumamos los valores absolutos
        Norm+=abs(vec[i])
    # Regresamos la suma de los valores absolutos
    return Norm

def norma2(vec):
    # Devuelve la norma 2 de vec
    Norm=0
    for i in range(len(vec)):
        # Sumamos los cuadrados
        Norm+=vec[i]**2
    # Regresamos la raiz cuadrada
    return np.sqrt(Norm)

def normaInf(vec):
    # Devuelve la norma del supremo de vec
    Norm=0
    for i in range(len(vec)):
        if(Norm < abs(vec[i])):
            # Guardamos el mayor en Norm
            Norm=abs(vec[i])
    # Regresamos el mayor
    return Norm

#---------- 1.1.2 ------------------------

'''Metodo de Newton para sistemas de ecuaciones no lineales
   aprox: es la primera aproximacion en forma de vector'''

def NewtonBivariable(x0,Tol,N=100,Norma=norma2):
    # Contador de iteraciones
    n = 0 
    while n <= N: # Maximo numero de iteraciones 100
        '''es necesario calcular la matriz jacobiana
        y para ello se necesita una matriz vacia de 2x2'''
        jacobinv = np.zeros([2,2])
        
        # Valores de la matriz jacobiana en todas sus entradas
        jacobinv[0][0] = par(x0[1])/denominador(x0[0], x0[1])
        jacobinv[0][1] = 1/denominador(x0[0], x0[1])
        jacobinv[1][0] = 1/denominador(x0[0], x0[1])
        jacobinv[1][1] = par(x0[0])/denominador(x0[0], x0[1])
    
        # Guarda la evalucion de f1 y f2 en forma de vector
        fx = np.array(x0)
        fx[0] = f1(x0[0], x0[1])
        fx[1] = f2(x0[0], x0[1])
        
        # FORMA ITERATIVA DEL METODO DE NEWTON PARA SISTEMAS NO LIENALES
        xn = x0 - np.matmul(jacobinv, fx)

        # Criterios de paro si se excede la tolerancia
        if(Norma(fx) <= Tol and Norma(x0-xn) <= Tol):
            return [xn,"Total de iteraciones: %d" %(n+1)]
        
        # Se actualiza la aproximacion
        x0=xn

        # Se incrementa el contador
        n+=1

    # El valor devuelto es la aproximacion y el numero de iteraciones
    return [x0,"Total de iteraciones: %d" %(n)]

#---------- 1.2 --------------------------

'''Metodo de Newton para sistemas de ecuaciones no lineales
   aprox: es la primera aproximacion en forma de vector'''

def NewtonBivariable2(x0,Tol,N=60,Norma=norma2):
    # Contador
    n=0 
    # Variable auxiliar
    xn=x0

    # Condicion de paro en numero de iteraciones
    while n <= N:

        # Matriz auxiliar para el jacobiano
        jacobinv = np.zeros([2,2])
        
        # Valores de la matriz jacobiana en todas sus entradas
        jacobinv[0][0] = par(x0[0])
        jacobinv[0][1] = -1
        jacobinv[1][0] = -1
        jacobinv[1][1] = par(x0[1])

        # Valores de la funcion
        Fx = np.array(x0)
        Fx[0] = f1(x0[0], x0[1])
        Fx[1] = f2(x0[0], x0[1])

        # Forma de solucion de ecuacion lineal al metodo de newton
        xn+=np.linalg.solve(jacobinv,-Fx)
        
        # Condiciones de paro
        if(Norma(Fx)<=Tol and Norma(xn-np.array(x0))<=Tol):
            return [xn,"Total de iteraciones: %d" %(n+1)]
        
        # Actualizacion de la aproximacion
        x0=xn

        # Incremento del contador
        n+=1

    # Regresamos el valor aproximado
    return [x0,"Total de iteraciones: %d" %(n)]

#---------- 1.3 --------------------------

def descomposicionLU(A):
    # Matriz auxilar para no borrar A
    B=np.copy(A)
    # Encontramos las columnas y los renglones
    ren, col = np.shape(B)

    # Definimos matrices auxiliares
    L = np.zeros([ren, col])
    U = np.zeros([ren, col])

    # Recorremos los renglones
    for k in range(ren):
        # Hacemos U=mat
        U[k][k]=B[k][k]

        for i in range(k,ren):
            # Hacemos el calulo del pivote
            L[i][k]=B[i][k]/U[k][k]
            # U=mat
            U[k][i]=B[k][i]

        for i in range(k,ren):
            for j in range(k,ren):
                # Como U=mat basta actualizar mat
                # Para que U cambie
                # Aplicamos la definicion del pivote
                # y cambiamos mat
                B[i][j]=B[i][j]-L[i][k]*U[k][j]

    # Regresamos L,U
    return L, U

def sustDelante(A,b):
    # Vector auxiliar para la solucion
    sol=np.zeros(len(b))
        
    # Definicion de substitucion hacia adelante
    for i in range(len(b)):
        # sol=bi
        sol[i]=b[i]
        for j in range(0,i):
            # bi - sum_0^i lij*yj = x
            sol[i]-=A[i][j]*sol[j]
        # x/lii
        sol[i]/=A[i][i]

    return sol
    
def sustAtras(A,b):
    # Vector auxiliar para la solucion
    sol=np.zeros(len(b))

    # Definicion de substitucion hacia atras
    for i in range(len(b)-1,-1,-1):
        # sol=bi
        sol[i]=b[i]
        for j in range(i+1,len(b)):
            # yi - sum_i+1^n-1 = x
            sol[i]-=A[i][j]*sol[j]
        # x/uii
        sol[i]/=A[i][i]

    return sol

def solver(A,b):
    # Factorizacion LU
    L,U=descomposicionLU(A)
    # Sustituimos hacia adelante
    y=sustDelante(L,b)
    # Sustituimos hacia atras
    x=sustAtras(U,y)
    return x
    
#---------- Metodo Main ------------------
def main():

    # Validacion de 1.1.1 ----------
    # Lo haremos aleatorio por lo que usaremos np.random
    # Esto no viola la restriccion de paqueterias puesto
    # que lo usamos unicamente para validar
    A=[(np.random.uniform(1,6)) for i in range(5)]
    assert np.round(norma1(A),decimals=5)==np.round(np.linalg.norm(A,1),decimals=5) # Si no son iguales, regresa un error
    assert np.round(norma2(A),decimals=5)==np.round(np.linalg.norm(A,2),decimals=5)
    assert np.round(normaInf(A),decimals=5)==np.round(np.linalg.norm(A,np.Inf),decimals=5)

    # Pruebas
    # Norma 1
    print("")
    print("Valor para la norma 1")
    print(norma1(A))
    print("")

    # Norma 2
    print("Valor para la norma 2")
    print(norma2(A))
    print("")

    # Norma del supremo
    print("Valor para la norma del supremo")
    print(normaInf(A))
    print("")

    # Validacion de 1.1.2 ----------
    # Aproximacion inicial (X=(0.0,0.0))
    ap = np.zeros([2])

    # Norma 1
    Newton1=NewtonBivariable(ap,1e-16,100,norma1)
    Jimy1=JimyNewtron(ap)
    for i in range(len(Newton1[0])):
        assert np.round(Newton1[0][i],decimals=8)==np.round(Jimy1[i],decimals=8) # Si no son iguales, regresa un error

    # Norma 2
    Newton2=NewtonBivariable(ap,1e-16,100,norma2)
    Jimy2=JimyNewtron(ap)
    for i in range(len(Newton2[0])):
        assert np.round(Newton2[0][i],decimals=8)==np.round(Jimy2[i],decimals=8)

    # Norma del supremo
    NewtonInf=NewtonBivariable(ap,1e-16,100,normaInf)
    JimyInf=JimyNewtron(ap)
    for i in range(len(NewtonInf[0])):
        assert np.round(NewtonInf[0][i],decimals=8)==np.round(JimyInf[i],decimals=8)
    
    # Pruebas
    # Norma 1
    print('Usando la norma 1')
    sol = NewtonBivariable(ap,0.001,10000,norma1)
    print(sol[1])
    print('Aproximacion de la solucion')
    print(sol[0])
    print('Aproximacion evaluada en f1')
    print(f1(sol[0][0], sol[0][1]))
    print('Aproximacion evaluada en f2')
    print(f2(sol[0][0], sol[0][1]))
    print("")

    # Norma 2
    print('Usando la norma 2')
    sol = NewtonBivariable(ap,0.001,10000,norma2)
    print(sol[1])
    print('Aproximacion de la solucion')
    print(sol[0])
    print('Aproximacion evaluada en f1')
    print(f1(sol[0][0], sol[0][1]))
    print('Aproximacion evaluada en f2')
    print(f2(sol[0][0], sol[0][1]))
    print("")

    # Norma del supremo
    print('Usando la norma del supremo')
    sol = NewtonBivariable(ap,0.001,10000,normaInf)
    print(sol[1])
    print('Aproximacion de la solucion')
    print(sol[0])
    print('Aproximacion evaluada en f1')
    print(f1(sol[0][0], sol[0][1]))
    print('Aproximacion evaluada en f2')
    print(f2(sol[0][0], sol[0][1]))
    print("")

    # Validacion de 1.2 ----------
    # Norma 1
    Newton12=NewtonBivariable2(ap,1e-16,100,norma1)
    for i in range(len(Newton12[0])):
        assert np.round(Newton12[0][i],decimals=8)==np.round(Jimy1[i],decimals=8) # Si no son iguales, regresa un error

    # Norma 2
    Newton22=NewtonBivariable2(ap,1e-16,100,norma2)
    for i in range(len(Newton2[0])):
        assert np.round(Newton22[0][i],decimals=8)==np.round(Jimy2[i],decimals=8)

    # Norma del supremo
    NewtonInf2=NewtonBivariable2(ap,1e-16,100,normaInf)
    for i in range(len(NewtonInf[0])):
        assert np.round(NewtonInf2[0][i],decimals=8)==np.round(JimyInf[i],decimals=8)

    # Pruebas
    # Norma 1
    print('Usando la norma 1')
    sol = NewtonBivariable2(ap,0.001,10000,norma1)
    print(sol[1])
    print('Aproximacion de la solucion')
    print(sol[0])
    print('Aproximacion evaluada en f1')
    print(f1(sol[0][0], sol[0][1]))
    print('Aproximacion evaluada en f2')
    print(f2(sol[0][0], sol[0][1]))
    print("")

    # Norma 2
    print('Usando la norma 2')
    sol = NewtonBivariable2(ap,0.001,10000,norma2)
    print(sol[1])
    print('Aproximacion de la solucion')
    print(sol[0])
    print('Aproximacion evaluada en f1')
    print(f1(sol[0][0], sol[0][1]))
    print('Aproximacion evaluada en f2')
    print(f2(sol[0][0], sol[0][1]))
    print("")

    # Norma del supremo
    print('Usando la norma del supremo')
    sol = NewtonBivariable2(ap,0.001,10000,normaInf)
    print(sol[1])
    print('Aproximacion de la solucion')
    print(sol[0])
    print('Aproximacion evaluada en f1')
    print(f1(sol[0][0], sol[0][1]))
    print('Aproximacion evaluada en f2')
    print(f2(sol[0][0], sol[0][1]))
    print("")

    # Validacion 1.3 ----------
    # Matriz del ejemplo del Jupyter: 'FactorizacionLU'
    U=np.array([[-4,-3,1],[0,5,1],[0,0,3]])
    L=np.array([[1,0,0],[-2,1,0],[-1,3,1]])
    A=np.array([[-4,-3,1],[8,11,-1],[4,18,5]])
    LU1=descomposicionLU(A)

    # Validacion descomposicion LU
    for i in range(len(LU1[0])):
        for j in range(len(LU1[0][i])):
            assert LU1[0][i][j]==L[i][j]
    
    for i in range(len(LU1[1])):
        for j in range(len(LU1[1][i])):
            assert LU1[1][i][j]==U[i][j]
    
    # Validacion substitucion hacia adelante/atras
    A=np.array([[(int)(np.random.uniform(1,80)) for i in range(3)],
                [(int)(np.random.uniform(1,80)) for i in range(3)],
                [(int)(np.random.uniform(1,80)) for i in range(3)]])

    b=np.array([(int)(np.random.uniform(1,20)) for i in range(3)])
    try:
        L,U=descomposicionLU(A)
    except:
        print("\nEjecutame de nuevo, la matriz aleatoria no era invertible :C")

    y1=sustDelante(L,b)
    y2=np.linalg.solve(L,b)

    x1=sustAtras(U,b)
    x2=np.linalg.solve(U,b)

    # Substitucion hacia adelante
    for i in range(len(y1)):
        assert np.round(y1[i],decimals=5)==np.round(y2[i],decimals=5)
    

    # Substitucion hacia atras
    for i in range(len(x1)):
        assert np.round(x1[i],decimals=5)==np.round(x2[i],decimals=5)
    
    # Validacion de solver
    A=np.array([[-4,-3,1],[8,11,-1],[4,18,5]])
    b=[5,6,1]
    z1=solver(A,b)
    z2=np.linalg.solve(A,b)

    # solver
    for i in range(len(z1)):
        assert np.round(z1[i],decimals=5)==np.round(z2[i],decimals=5)
    
    


    # Pruebas
    print("Matriz inferior")
    print(LU1[0])

    print("\nMatriz superior")
    print(LU1[1])

    U=np.array([[-4,-3,1],[0,5,1],[0,0,3]])
    L=np.array([[1,0,0],[-2,1,0],[-1,3,1]])
    A=sustDelante(L,[5,6,1])
    print("\nSolucion al ejemplo de clase sustDelante")
    print(A)
    print("\n Solucion al ejemplo de clase susDetras")
    B=sustAtras(U,[5,16,-42])
    print(B)
    A=np.array([[-4,-3,1],[8,11,-1],[4,18,5]])
    b=[5,6,1]
    print("\nsolucion al ejemplo de clase solver")
    print(solver(A,b))
    print('')



if __name__=='__main__':
    main()