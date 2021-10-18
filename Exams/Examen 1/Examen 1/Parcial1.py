"""
Examen Parcial 1

Carrillo Medina Alexis Adrian (CMAA)

Nombre del programa: Parcial1.py

NOTA: La finalidad de este archivo es hacer las respectivas pruebas.
      Los algoritmos se encuentran en matrices/Matriz.py
      Se probo usando linux.

"""
#----- Seccion de bibliotecas

from matrices import Matriz

#----- Codigo

if __name__=="__main__":
    # Metodo main
    # Hacemos las respectivas pruebas
    
    print("")
    # Construimos la matriz de nxm
    n=int(input("Ingresa el numero de columnas: \n"))
    m=int(input("Ingresa el numero de filas: \n"))

    Mat=Matriz.Matriz(n,m,Zeros=True)

    # Agregamos los elementos
    print("")
    print ("Ingrese los elementos de la  matriz")
    for i in range(n):
        for j in range(m):
            Mat.changeElement(i,j,float(input("Elemento (%2d,%2d): " % (i, j))))

    # Imprimimos la matriz
    print("\nLa matriz es")
    Mat.toString()

    # Calculamos e imprimimos la inversa
    print("\nSu inversa es")
    Mat.matrizInversa().toString()

    # Calculamos e imprimimos la potencia p
    print("\n")
    p=int(input("Ingrese la potencia "))
    print("La Matriz a la potencia %d es" %(p))
    Mat.potencia(p).toString()
    print("")