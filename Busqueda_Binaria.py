lista = []

numero_de_elementos = int( input( " Digite un numero de elementos: " ) )
while ( numero_de_elementos < 0 ):
    print( " ---------------------------------------------- " )
    print( " La cantidad de elementos no puede ser negativa " )
    print( " ---------------------------------------------- " )
    numero_de_elementos = int( input( " Digite de nuevo la cantidad de elementos: " ) )

for i in range( numero_de_elementos ):
    valor = int( input( f" Digite un numero en la posicion [ { i } ]: " ) )
    lista.append( valor )

def Metodo_Burbuja( lista ):
    for pasanum in range( len(lista)-1,0,-1 ):
        for i in range(pasanum):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    print(lista)

print( " Lista Ordenada con el Metodo Burbuja " )
Metodo_Burbuja(lista)

buscado = int( input( " Digite el numero que quiere encontrar: " ) )

def Busqueda_Binaria( lista, elemento ):
    inicio = 0
    final = len(lista)-1

    while inicio <= final:
        medio = ( inicio + final )//2

        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        elif lista[medio] > elemento:
            final = medio - 1 
    return None

def buscar_Valor( elemento ):
    res_busqueda = Busqueda_Binaria( lista, elemento )
    if ( res_busqueda is None ):
        print( f" El numero { elemento } no se encuentra "  )
    else:
        print( f" El numero { elemento } se encuentra en la posicion [ { res_busqueda } ] " )

buscar_Valor(buscado)