#Importamos random para poder generar la matriz inicial
#por medio de revolver una que contenga todos los numeros
#[0,1,2,3,4,5,6,7,8]
import random
#importamos deque de collections para utilizar en la cola del metodo
#puzzle8, porque queria poder eliminar el 1er elemento de dicha cola
#entonces la defini como deque para usar .popleft()
from collections import deque
#Se utilizara Algoritmo de Busqueda de Amplitud
#Definicion de las Matrices
solucionFinal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]
matriz8 = [0,1,2,3,4,5,6,7,8]
#Metodo para revolver el tablero, se usa al iniciar y al seleccionar "Restablecer"
def restablecer(matriz8):
    random.shuffle(matriz8)
    matriz=[]
    for i in range(0,9,3):
        fila=matriz8[i:i+3]
        matriz.append(fila)
    return matriz
#Este metodo se encarga de localizar el 0
def buscarZero(matriz,zero):
    #Buscar 0
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == zero:
                return (i,j)
#Este metodo recibe la posicion del 0 y analiza sus movimientos
def movimientos(matriz):
    i,j = buscarZero(matriz,0)
    rutas = []
    if i > 0 :
        rutas.append((i-1,j))
    if i<2 :
        rutas.append((i+1,j))
    if j > 0 :
        rutas.append((i,j-1))
    if j<2 :
        rutas.append((i,j+1))  
    return rutas
# Este metodo recibe la matriz del juego y la que se
# busca alcanzar para comprobar si ya se logro una victoria
# si ambas son iguales acabo el juego
def victoria(matriz1,matriz2):
    return matriz1==matriz2 

# Metodo que se encargue de mover el 0
def movZero(matriz,movimiento):
    i,j= buscarZero(matriz,0)
    mi,mj=movimiento
    nueva= [list(fila) for fila in matriz]
    nueva[i][j], nueva[mi][mj]=nueva[mi][mj],nueva[i][j]
    return tuple(tuple(fila) for fila in nueva)
#Metodo que se encarga de retornar una Matriz de Matrices que almacena 
#todas las matrices correspondientes a los movimientos que llevaron
#a la matriz solucion
def recorrido(predecesor,solucionado):
    camino=[]
    actual=solucionado
    while actual is not None:
        camino.append(actual)
        actual=predecesor[actual]
    camino.reverse()
    return camino
#Este metodo es el que se encarga de que la compu sea quien juegue a Puzzle8
#Utilizando el Algoritmo de Busqueda de Amplitud
def puzzle8(matrizJuego,matrizSolucion):
    #Primero se definen la matriz inicio, la que es la correspondiente a la solucion
    #y:
    #cola que sera la servira para llevar registro de la posicion actual,
    #visitados se encarga de revisar que las formaciones que puedan provocar los continuos
    #movimientos no hayan sido provocadas ya,
    #predecesor se encarga de ir llevando registro de la matriz padre de cada formacion
    inicio=tuple(tuple(fila) for fila in matrizJuego)
    solucion=tuple(tuple(fila) for fila in matrizSolucion)
    cola=deque([])
    cola.append(inicio)
    visitados={inicio}
    predecesor={inicio:None}
    noEncontrado=False
    #Para encontrar la matriz solucion se esta repitiendo constantemente un while
    #el cual se repit mientras que no se haya llegado a la matriz solucion,
    #para ello se comprueban todos los posibles movimientos que pueden derivar
    #dependiendo en donde se encuentre el 0, en caso de que la matriz resultante
    #de algun movimiento ya se haya formado antes, se omite, y se pasa a analizar
    #el siguiente movimiento, en caso que seaa nueva, se guarda en la cola y en los visitados,
    #ademas se registra la matriz padre.

    #Dependiendo la matriz Inicial puede o no haber una solucion
    while not victoria(cola[0],solucion):
        movs = movimientos(cola[0])
        for i in movs:
            tablero_temporal=movZero(cola[0],i)
            if tablero_temporal not in visitados:
                visitados.add(tablero_temporal)
                cola.append(tablero_temporal)
                predecesor[tablero_temporal]=cola[0]
                if victoria(tablero_temporal,solucion)==True:
                    break
        if victoria(tablero_temporal,solucion):
            break
        cola.popleft()
        if not cola:
            noEncontrado=True
            break
    #En caso de que si hubiera solucion se retorna el recorrido completo
    #en una matriz, pero eb caso de que no, se enviara una Matriz Vacia
    if noEncontrado==False and victoria(cola[-1],solucion):
        #Metodo para cuando ya se gano
        return recorrido(predecesor,solucion)
    elif noEncontrado==True:
        return []


