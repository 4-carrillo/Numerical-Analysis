"""
Examen Parcial 4

Carrillo Medina Alexis Adrian (CMAA)

Nombre del programa: Parcial4.py

"""

#----- Seccion de bibliotecas

import numpy as np
import matplotlib.pyplot as plt

# scipy es utilizado unicamente para la comprobacion
import scipy.integrate as integrate

#----- Codigo
# La validacion se encuentra en el metodo main

#---------- Metodos auxiliares -----------

def exacSolution(x):
    return 2*np.e**x-x-1

def random(N,seed=0.128258):
    # Semilla
    fx=[seed]
    x=[]

    for i in range(1,N+1):
        # Generador lineal congruencial
        fx.append((7**5)*(fx[i-1])%(2*31-1)) 
        x.append(fx[i]/(2*31-1))

    return x

def random2(N,seed=0.128258):
    # Semilla
    fx=[seed]

    # Mapeo logisticpo
    for i in range(1,N+1):
        fx.append(4*fx[i-1]*(1-fx[i-1]))
    
    # La distribucion invariante 
    # del mapeo logistico es Beta(1/2, 1/2)
    # X ~ Beta(1/2,1/2) => Y=(2/Pi)(arcsin(sqrt(X))) ~ Uniform(0,1)
    x=(2/np.pi)*(np.arcsin(np.sqrt(fx)))

    return x

def fRandom(x,y,z):
    return x*y*np.sin(y*z)

#---------- 1 ----------------------------
#---------- 1.1 --------------------------
def difFinitas1D(a,N,xmax):
    """
    a := Condicion inicial
    N := # Nodos de la discretizacion
    xmax := Valor maximo del eje x
    """

    # Discretizacion
    y=np.zeros([N+1])
    # Condicion inicial
    y[0]=a

    # Discretizacion temporal
    t=np.zeros([N+1])
    # Tiempo inicial
    t[0]=0

    # Delta
    Delta=float(xmax)/N

    # Diferencias finitas con sustitucion hacia adelante
    for i in range(0,N):
        # Aproximacion
        y[i+1]=y[i]*(Delta+1)+Delta*t[i]
        t[i+1]=t[i]+Delta

    # La grafica de la funcion
    # la podemos encontrar en el metodo main.
    # Esto es por motivos esteticos del codigo

    return t,y

#---------- 2 ----------------------------
#---------- 2.1 --------------------------

def aproxTrapecioCompuesto(f,n,a,b):
    """
    f := funcion a aproximar integral
    n := Numero de puntos
    (a,b) := Intervalo de integracion
    """
    # Valor inicial de la integral
    integral=f(a)
    # Punto inicial x
    x=a
    # Delta
    delta=(b-a)/n

    # Suma de la definicion
    suma=0;
    for i in range(1,n):
        x+=delta
        suma+=f(x)
    
    # Suma interior de la definicion
    integral+=2*suma+f(b)
    
    # Definicion
    return (delta/2)*integral

#---------- 3 ----------------------------
#---------- 3.1 --------------------------

def integralMonteCarlo1(f,N,a,b,c,d,e,g,seed=0.1578):

    """
    f := funcion a aproximar
    N := Numero de vectores aleatorios
    (a,b)x(c,d)x(e,g) := Rectangulo de integracion
    seed := semilla
    """

    # Volumen del rectangulo
    vol=(b-a)*(d-c)*(g-e)

    # Numero aleatorios
    # Generados por lineal congruencial
    x=random(N,seed)
    y=random(N,seed)
    z=random(N,seed)

    # Suma de los montecarlo
    monteCarlo=0
    for i in range(N):
        # Valores recorridos
        xr=x[i]*(b-a)+a
        yr=y[i]*(d-c)+c
        zr=z[i]*(g-e)+e
        
        # Paso de suma
        monteCarlo+=f(xr,yr,zr)

    # Definicion de MonteCarlo
    return (vol/N)*monteCarlo

def integralMonteCarlo2(f,N,a,b,c,d,e,g,seed=0.1578):
    """
    f := funcion a aproximar
    N := Numero de vectores aleatorios
    (a,b)x(c,d)x(e,g) := Rectangulo de integracion
    seed := semilla
    """

    # Volumen del rectangulo
    vol=(b-a)*(d-c)*(g-e)

    # Numero aleatorios
    # Generados por mapeo logistico
    x=random2(N,seed)
    y=random2(N,seed)
    z=random2(N,seed)

    # Suma de los montecarlo
    monteCarlo=0
    for i in range(N):
        # Valores recorridos
        xr=x[i]*(b-a)+a
        yr=y[i]*(d-c)+c
        zr=z[i]*(g-e)+e
        
        # Paso de suma
        monteCarlo+=f(xr,yr,zr)

    # Definicion de MonteCarlo
    return (vol/N)*monteCarlo


def integralMonteCarlo(f,N,a,b,c,d,e,g):
    """
    f := funcion a aproximar
    N := Numero de vectores aleatorios
    (a,b)x(c,d)x(e,g) := Rectangulo de integracion
    """
    # Volumen del rectangulo
    vol=(b-a)*(d-c)*(g-e)

    # Numero aleatorios por Numpy
    # Para ejemplificar el error
    # Del generador aleatorio
    x=np.random.uniform(size=N)
    y=np.random.uniform(size=N)
    z=np.random.uniform(size=N)

    # Suma de los montecarlo
    monteCarlo=0
    for i in range(N):
        # Valores recorridos
        xr=x[i]*(b-a)+a
        yr=y[i]*(d-c)+c
        zr=z[i]*(g-e)+e
        
        # Paso de suma
        monteCarlo+=f(xr,yr,zr)

    # Definicion de MonteCarlo
    return (vol/N)*monteCarlo


#---------- Metodo Main ------------------
def main():

    # Validacion 1 ------------
    # Validacion 1.1 ----------
    example=[1,1.2,1.48,1.856,2.3472,2.97664]
    t,y=difFinitas1D(1,5,1)
    for i in range(len(y)):
        assert y[i]==example[i]

    # Pruebas
    a=1
    N=10
    xmax=1

    # Grafica
    t,y=difFinitas1D(a,N,xmax)
    plt.plot(t,y,color="red",label="Aproximacion")
    plt.plot(np.linspace(0,xmax,N+1),exacSolution(np.linspace(0,xmax,N+1)),color="blue",label="Funcion real")
    plt.legend(shadow=True)
    plt.show()
    # Solucion
    print("\nEjercicio 1.1")
    print("\nDerivadas")
    print(y)
    print("")

    # Validacion 2 ------------
    # Validacion 2.1 ----------
    aproxSc,error=integrate.quad(lambda x:np.cos(x),-2,3)
    aproxTrapecio=aproxTrapecioCompuesto(np.cos,100,-2,3)
    assert np.round(aproxSc,2)==np.round(aproxTrapecio,2)

    # Pruebas
    print("Ejercicio 2.1 \n")
    print("f(x)=cos(x) \n")
    print("Solucion 'exacta'")
    print(aproxSc)
    print("\nSolucion aproximada")
    print(aproxTrapecio)
    print("")
    
    # Validacion 2 ------------
    # Validacion 2.1 ----------
    int1=integralMonteCarlo1(fRandom,10000,1,3,0,np.pi,0,np.pi/3,np.random.uniform())
    int2=integralMonteCarlo2(fRandom,10000,1,3,0,np.pi,0,np.pi/3,np.random.uniform())
    assert abs(int1-int2) < 1

    # Pruebas
    print("Ejercicio 3.1 \n")
    print("f(x,y,z)=x*y*sin(y*z)\n")
    print("Integral por Generador lineal congruencial")
    print(int1)
    print("\nIntegral por Mapeo logistico")
    print(int2)
    print("\nIntegral por Numpy")
    print(integralMonteCarlo(fRandom,10000,1,3,0,np.pi,0,np.pi/3))
    print("")

if __name__=='__main__':
    main()  