# %% [markdown]
# ### Teoría del problema
# Considerar el conjunto de misioneros, caníbales y bote como: <br>
# [0,0,0] <-> [3,3,1]
# 
# El segundo dígito, que representa a los caníbales no debe ser mayor que el primer dígito<br>
# que representa a los misioneros. El tercer dígito representa el lado que se encuentra el bote.
# 
# Solamente 2 unidades pueden moverse al otro lado y sólamente si está el bote en ese lado. <br>
# Por lo cual, a M y C se le puede restar de 0 hasta 2. <br>
# De igual forma, en cada movimiento a B se le debe restar 1.<br>
# 
# [M,C,B]<br>
# 
# Por cada resta que se haga en un lado, en el otro lado debe hacerse lo inverso, una suma. <br>
# En perspectiva, la resta sólamente puede hacerse en el lado donde se encuentra el bote.
# 

# %% [markdown]
# Ejemplo de camino exitoso: <br>
# [0,0,0] <-> [3,3,1] <-- Inicio<br>
# [1,1,1] <-> [2,2,0] <br>
# [0,1,0] <-> [3,2,1] <br>
# [0,3,1] <-> [3,0,0] <br>
# [0,2,0] <-> [3,1,1] <br>
# [2,2,1] <-> [1,1,0] <br>
# [1,1,0] <-> [2,2,1] <br>
# [3,1,1] <-> [0,2,0] <br>
# [3,0,0] <-> [0,3,1] <br>
# [3,2,1] <-> [0,1,0] <br>
# [3,1,0] <-> [0,2,1] <br>
# [3,3,1] <-> [0,0,0] <-- Meta

# %%
#Función para verificar si se cumple la condición de llegar a meta
def criterioAceptacion(posicion, meta):
  return posicion == meta

# %%
print(criterioAceptacion([3,3,1], [3,3,1]))
print(criterioAceptacion([3,2,1], [2,2,0]))

# El que realmente se usará
print(criterioAceptacion(([3, 3, 1], [0, 0, 0]), ([3, 3, 1], [0, 0, 0])))
print(criterioAceptacion(([0, 0, 0], [3, 3, 1]), ([3, 3, 1], [0, 0, 0])))

# %% [markdown]
# Para generar las soluciones del problema, tenemos las siguientes opciones: <br>
# 1.- Restar 2 a misioneros, sólo si hay más de 1. <br>
# 2.- Restar 2 a caníbales, sólo si hay más de 1. <br>
# 3.- Restar 1 a misioneros y 1 a caníbales, sólo si hay más de 0 en ambos. <br>
# 4.- Restar 1 a misioneros o 1 a caníbales, sólo si hay más de 0 en alguno de los dos. <br>

# %%
#Función que permite generar todas las posibles soluciones
#En este caso genera todos los posibles movimientos del estado actual
def generarSoluciones(ladoIzq, ladoDer):
  soluciones = []
  #Generar posibles soluciones

  # Se restan 2 misioneros (perspectiva lado derecho).
  m, c, b = ladoIzq[0] + 2, ladoIzq[1], ladoIzq[2]
  m2, c2, b2 = ladoDer[0] - 2, ladoDer[1], ladoDer[2]
  if m2 >= 0 and b2 == 1:
    #print("a")
    soluciones.append(([m,c,b+1],[m2,c2,b2-1]))
  
  # Se aumentan 2 misioneros.
  m, c, b = ladoIzq[0] - 2, ladoIzq[1], ladoIzq[2]
  m2, c2, b2 = ladoDer[0] + 2, ladoDer[1], ladoDer[2]
  if m2 <= 3 and b2 == 0:
    #print("b")
    soluciones.append(([m,c,b-1],[m2,c2,b2+1]))
  
  # Se restan 2 caníbales.
  m, c, b = ladoIzq[0], ladoIzq[1] + 2, ladoIzq[2]
  m2, c2, b2 = ladoDer[0], ladoDer[1] - 2, ladoDer[2]
  if c2 >= 0 and b2 == 1:
    #print("c")
    soluciones.append(([m,c,b+1],[m2,c2,b2-1]))

  # Se aumentan 2 caníbales.
  m, c, b = ladoIzq[0], ladoIzq[1] - 2, ladoIzq[2]
  m2, c2, b2 = ladoDer[0], ladoDer[1] + 2, ladoDer[2]
  if c2 <= 3 and b2 == 0:
    #print("d")
    soluciones.append(([m,c,b-1],[m2,c2,b2+1]))
  
  # Se resta 1 y 1.
  m, c, b = ladoIzq[0] + 1, ladoIzq[1] + 1, ladoIzq[2]
  m2, c2, b2 = ladoDer[0] - 1, ladoDer[1] - 1, ladoDer[2]
  if (m2 >= 0 and c2 >= 0) and b2 == 1:
    #print("e")
    soluciones.append(([m,c,b+1],[m2,c2,b2-1]))
  
  # Se aumenta 1 y 1.
  m, c, b = ladoIzq[0] - 1, ladoIzq[1] - 1, ladoIzq[2]
  m2, c2, b2 = ladoDer[0] + 1, ladoDer[1] + 1, ladoDer[2]
  if (m2 <= 3 and c2 <= 3) and b2 == 0:
    #print("f")
    soluciones.append(([m,c,b-1],[m2,c2,b2+1]))

  # Se resta 1 a misioneros.
  m, c, b = ladoIzq[0] + 1, ladoIzq[1], ladoIzq[2]
  m2, c2, b2 = ladoDer[0] - 1, ladoDer[1], ladoDer[2]
  if m2 >= 0 and b2 == 1:
    #print("g")
    soluciones.append(([m,c,b+1],[m2,c2,b2-1]))
  
  # Se aumenta 1 a misioneros.
  m, c, b = ladoIzq[0] - 1, ladoIzq[1], ladoIzq[2]
  m2, c2, b2 = ladoDer[0] + 1, ladoDer[1], ladoDer[2]
  if m2 <= 3 and b2 == 0:
    #print("h")
    soluciones.append(([m,c,b-1],[m2,c2,b2+1]))

  # Se resta 1 a caníbales.
  m, c, b = ladoIzq[0], ladoIzq[1] + 1, ladoIzq[2]
  m2, c2, b2 = ladoDer[0], ladoDer[1] - 1, ladoDer[2]
  if c2 >= 0 and b2 == 1:
    #print("i")
    soluciones.append(([m,c,b+1],[m2,c2,b2-1]))
  
  # Se aumenta 1 a caníbales.
  m, c, b = ladoIzq[0], ladoIzq[1] - 1, ladoIzq[2]
  m2, c2, b2 = ladoDer[0], ladoDer[1] + 1, ladoDer[2]
  if c2 <= 3 and b2 == 0:
    #print("j")
    soluciones.append(([m,c,b-1],[m2,c2,b2+1]))
  
  return soluciones

# %%
generarSoluciones([1, 0, 1], [2, 3, 0])

# %%
def validar(ladoIzq, ladoDer, visitados):
    # Si visitados no está vacía, el bote podría haberse movido.
    if (len(visitados) != 0):
        # Verificar que el último nodo de visitados no tenga el bote en el mismo lado que el nodo actual.
        if (ladoIzq[2] != visitados[-1][0][2]):
            # Validar que en el nodo no haya más caníbales que misioneros en cualquiera de los lados.
            return ((ladoIzq[0] >= ladoIzq[1] or ladoIzq[0] == 0) and (ladoDer[0] >= ladoDer[1] or ladoDer[0] == 0))
        else:
            return False
    # Si está vacía, el bote siempre estará a la derecha.
    else:
        return True

# %%
validar([1, 1, 1], [2, 2, 0],[])

# %%
def imprimir_tablero(recorrido):
    for estado in recorrido:
        izquierda, derecha = estado
        misioneros_izq, canibales_izq, barco_izq = izquierda
        misioneros_der, canibales_der, barco_der = derecha
        
        # Representación visual
        print("Izquierda:  " + "M: " + str(misioneros_izq) + " C: " + str(canibales_izq) + " B: " + str(barco_izq))
        print("Barco       " + ("<--" if barco_izq else "-->"))
        print("Derecha:    " + "M: " + str(misioneros_der) + " C: " + str(canibales_der) + " B: " + str(barco_der))
        print('-' * 40)

# %%
#Implementación del algoritmo de búsqueda BFS
def BFS(frontera_act, visitados, solucion, meta, n_iteraciones):
  n_iteraciones = n_iteraciones + 1
  frontera = frontera_act[:]
  #Si ya no hay posibles caminos, entonces no se encontro solución
  if len(frontera) == 0:
    print("Número de iteraciones: {}".format(n_iteraciones))
    return []
  #Se toma el primer elemento de la lista y se elimina de la misma
  cabeza = frontera.pop(0)
  #Si el elemento no ha sido anteriormente visitado o generado,
  #entonces no se generan más soluciones, para evitar enciclarse
  # y también valida el nodo actual usando las reglas de juego.
  if cabeza not in visitados and validar(cabeza[0], cabeza[1], visitados):
  #if cabeza not in visitados:
    #Se agrega el elemento a la lista de soluciones, es decir el camino recorrido hasta ahora
    solucion.append(cabeza)
    #Si cumple con el criterio de aceptación entonces llega a la meta
    if criterioAceptacion(cabeza, meta):
      print("Se ha llegado a la meta: {}".format(cabeza))
      print("Número de iteraciones: {}".format(n_iteraciones))
      return solucion
    #Se agrega a la lista de visitados para evitar enciclamientos
    print("Recorriendo, actualmente en: {}".format(cabeza))
    visitados.append(cabeza)
    #Se generan las nuevas posibilidades a partir de la posición actual
    nuevas_soluciones = generarSoluciones(cabeza[0], cabeza[1])
    print("Nuevas soluciones: {}".format(nuevas_soluciones))
    #Se agregan los elementos nuevos al final de la lista para simular una cola
    frontera = frontera + nuevas_soluciones
  #Se hace un llamado recursivo
  return BFS(frontera, visitados, solucion, meta, n_iteraciones)

# %%
#Función que utiliza todos las funciones creadas para hacer la simulación
def play_bfs():
  inicio = ([0,0,0], [3,3,1])
  meta = ([3,3,1], [0,0,0])
  visitados, solucion = [], []
  solBFS = BFS([inicio], visitados, solucion, meta, 0)
  print("Cantidad recorrida con BFS: {}".format(len(solBFS)))
  print("Recorrido: {}".format(solBFS))
  imprimir_tablero(solBFS)
  if len(solBFS) == 0:
    print("No se encontro solucion")
    return

# %%
#play_bfs()

# %%
#Implementación del algoritmo de búsqueda DFS
def DFS(frontera_act, visitados, solucion, meta, n_iteraciones):
  n_iteraciones = n_iteraciones + 1
  frontera = frontera_act[:]
  #Si ya no hay posibles caminos, entonces no se encontro solución
  if len(frontera) == 0:
    print("Número de iteraciones: {}".format(n_iteraciones))
    return []
  #Se toma el primer elemento de la lista y se elimina de la misma
  cabeza = frontera.pop(0)
  #Si el elemento no ha sido anteriormente visitado o generado,
  #entonces no se generan más soluciones, para evitar enciclarse
  # y también valida el nodo actual usando las reglas de juego.
  if cabeza not in visitados and validar(cabeza[0], cabeza[1], visitados):
  #if cabeza not in visitados:
    #Se agrega el elemento a la lista de soluciones, es decir el camino recorrido hasta ahora
    solucion.append(cabeza)
    #Si cumple con el criterio de aceptación entonces llega a la meta
    if criterioAceptacion(cabeza, meta):
      print("Se ha llegado a la meta: {}".format(cabeza))
      print("Número de iteraciones: {}".format(n_iteraciones))
      return solucion
    #Se agrega a la lista de visitados para evitar enciclamientos
    print("Recorriendo, actualmente en: {}".format(cabeza))
    visitados.append(cabeza)
    #Se generan las nuevas posibilidades a partir de la posición actual
    nuevas_soluciones = generarSoluciones(cabeza[0], cabeza[1])
    print("Nuevas soluciones: {}".format(nuevas_soluciones))
    #Se agregan los elementos nuevos al inicio de la lista para simular una pila
    frontera = nuevas_soluciones + frontera
  #Se hace un llamado recursivo
  return DFS(frontera, visitados, solucion, meta, n_iteraciones)

# %%
#Función que utiliza todos las funciones creadas para hacer la simulación
def play_dfs():
  inicio = ([0,0,0], [3,3,1])
  meta = ([3,3,1], [0,0,0])
  visitados, solucion = [], []
  solDFS = DFS([inicio], visitados, solucion, meta, 0)
  print("Cantidad recorrida con DFS: {}".format(len(solDFS)))
  print("Recorrido: {}".format(solDFS))
  imprimir_tablero(solDFS)
  if len(solDFS) == 0:
    print("No se encontro solucion")
    return

# %%
#play_dfs()

# %%
#import numpy as np
def profundidad(inicio, actual):
  #Inicio = (x1, y1); actual (x2, y2)
  #Se calcula el límite de la profundidad, mediante la diferencia mayor de los puntos
  #res = abs(np.array(inicio) - np.array(actual))
  #return max(res)
  res = abs(inicio[1] - actual[1])
  return res

# %%
#profundidad((2,2), (4,1))
profundidad((([0,0,0], [3,3,1]),1), (([0,0,0], [3,3,1]),3))

# %%
#Función DFS limitada a un valor de profundidad
def LDFS(frontera_act, visitados, solucion, meta, n_iteraciones, inicio, limite):
  n_iteraciones = n_iteraciones + 1
  frontera = frontera_act[:]
  #Si ya no hay posibles caminos, entonces no se encontro solución
  if len(frontera) == 0:
    print("Número de iteraciones: {}".format(n_iteraciones))
    return []
  #Se toma el primer elemento de la lista y se elimina de la misma
  cabeza = frontera.pop(0)
  #Si el elemento no ha sido anteriormente visitado o generado,
  #entonces no se generan más soluciones, para evitar enciclarse
  # y también valida el nodo actual usando las reglas de juego.
  if cabeza[0] not in visitados and validar(cabeza[0][0], cabeza[0][1], visitados):
  #if cabeza not in visitados:
    #Se agrega el elemento a la lista de soluciones, es decir el camino recorrido hasta ahora
    solucion.append(cabeza[0])
    #Si cumple con el criterio de aceptación entonces llega a la meta
    if criterioAceptacion(cabeza[0], meta):
      print("Se ha llegado a la meta: {}".format(cabeza))
      print("Número de iteraciones: {}".format(n_iteraciones))
      return solucion
    #Se agrega a la lista de visitados para evitar enciclamientos
    print("Recorriendo, actualmente en: {}".format(cabeza))
    visitados.append(cabeza[0])
    #Se establece una condición sobre si la generación de profundidad de las posibilidades es menor al limite establecido
    if profundidad(inicio, cabeza) <= limite:
      #Se generan las nuevas posibilidades a partir de la posición actual
      nuevas_soluciones = generarSoluciones(cabeza[0][0], cabeza[0][1])
      nuevas_soluciones_nivel = []
      for sol in nuevas_soluciones:
        nuevas_soluciones_nivel.append((sol, cabeza[1] + 1))
      print("Nuevas soluciones + nivel: {}".format(nuevas_soluciones_nivel))
      frontera = frontera + nuevas_soluciones_nivel
  #Se hace un llamado recursivo
  return LDFS(frontera, visitados, solucion, meta, n_iteraciones, inicio, limite)

# %%
#Función que utiliza todos las funciones creadas para hacer la simulación
def play_ldfs():
  # Se establece un limite para evitar que recorra todo el espacio de soluciones
  limite = 9
  inicio = ([0,0,0], [3,3,1])
  meta = ([3,3,1], [0,0,0])
  visitados, solucion = [], []
  solLDFS = LDFS([(inicio,0)], visitados, solucion, meta, 0, (inicio, 0), limite)
  print("Cantidad recorrida con LDFS: {}".format(len(solLDFS)))
  # El recorrido no se imprimirá si no llega a la solución, pero se puede ver mientras recorre nodos.
  print("Recorrido: {}".format(solLDFS))
  imprimir_tablero(solLDFS)
  if len(solLDFS) == 0:
    print("No se encontro solucion")
    return

# %%
#play_ldfs()

# %%
#Función que implementa la variación del DFS limitado con una estructura iterativa
def ILDFS(frontera, limite_inicial, inicio, meta, n_iteraciones):
  #Se guarda el limite inicial para que altere solo el valor de la variable local
  limite_actual = limite_inicial
  #Ciclo infinito
  while True:
    #Si el limite es mayor a uno establecido
    if limite_actual >= 100:
      #entonces no encontro una solición (Evita enciclarse por siempre)
      print("No se encontro solución")
      return []
    solucion = []
    visitados = []
    #Se llama al algoritmo LDFS creado anteriormente con el limite actual
    sol = LDFS(frontera, visitados, solucion, meta, n_iteraciones, (inicio,0), limite_actual)
    #Si encuentra una solción, la lista debe tener más de un elemento
    if len(sol) > 0:
      print("Se encontro la solución en el nivel: {}".format(limite_actual))
      #Se retorna la solución encontrada
      return sol
    #Si no encuentra aun la solución, entonces aumenta el limite establecido, para aumentar el rango de posibilidades
    limite_actual += 1
    print("No se encontro solución en el nivel: {}".format(limite_actual))

# %%
#Función que utiliza todos las funciones creadas para hacer la simulación
def play_ildfs():
  limite = 1
  inicio = ([0,0,0], [3,3,1])
  meta = ([3,3,1], [0,0,0])
  solILDFS = ILDFS([(inicio,0)], limite, inicio, meta, 0)
  print("Cantidad recorrida con ILDFS: {}".format(len(solILDFS)))
  # El recorrido no se imprimirá si no llega a la solución, pero se puede ver mientras recorre nodos.
  print("Recorrido: {}".format(solILDFS))
  imprimir_tablero(solILDFS)
  if len(solILDFS) == 0:
    print("No se encontro solucion")
    return

# %%
#play_ildfs()

# %%
def heuristica(ladoIzq):
    m, c, _ = ladoIzq
    return m + c

# %%
def evaluacionVoraz(posibilidades, visitados):
    best_val = 100000
    best = None
    for posible in posibilidades:
        if posible not in visitados:
            val = heuristica(posible[0])
            if val < best_val:
                best = posible
                best_val = val
    return best

# %%
def eliminaPosibilidadeIguales(posibilidades, lista):
  nueva_lista = []
  for posible in posibilidades:
    if posible in lista:
      continue
    nueva_lista.append(posible)
  return nueva_lista

# %%
def voraz(nodo, visitados, solucion, meta, n_iteraciones):
  n_iteraciones = n_iteraciones + 1
  if nodo == None:
    return []
  print("Recorriendo, actualmente en: {}".format(nodo))
  solucion.append(nodo)
  if criterioAceptacion(nodo, meta):
    print("Se ha llegado a la meta: {}".format(nodo))
    print("Número de iteraciones: {}".format(n_iteraciones))
    return solucion
  print("nodo: {}".format(nodo))
  nuevas_soluciones = generarSoluciones(nodo[0], nodo[1])
  print("Nuevas soluciones: {}".format(nuevas_soluciones))
  #print(nuevas_soluciones)
  nuevas_soluciones = eliminaPosibilidadeIguales(nuevas_soluciones, visitados)
  #print(nuevas_soluciones)
  mejor = evaluacionVoraz(nuevas_soluciones, visitados)
  #print(mejor)
  visitados.append(nodo)
  return voraz(mejor, visitados, solucion, meta, n_iteraciones)

# %%
def play_voraz():
  inicio = ([0,0,0], [3,3,1])
  meta = ([3,3,1], [0,0,0])
  visitados, solucion = [], []
  solVoraz = voraz(inicio, visitados, solucion, meta, 0)
  print("Cantidad recorrida con voraz: {}".format(len(solVoraz)))
  # El recorrido no se imprimirá si no llega a la solución, pero se puede ver mientras recorre nodos.
  print("Recorrido: {}".format(solVoraz))
  imprimir_tablero(solVoraz)
  if len(solVoraz) == 0:
    print("No se encontro solucion")
    return

# %%
#play_voraz()

# %%
#Función que evalua cada posibilidad y ordena la lista de menor a mayor en este caso.
def evaluacion_aStar(posibilidades, visitados):
  evaluaciones = []
  for posible in posibilidades:
    if posible not in visitados:
        #Se suma g(n) + h(n)
        valor = posible[1] + heuristica(posible[0][0])
        evaluaciones.append([posible, valor])
  #print(evaluaciones)
  def second_value(elemento):
    return elemento[1]
  evaluaciones.sort(key= second_value)
  #print(evaluaciones)
  resultado = [posible for (posible, valor_evaluacion) in evaluaciones]
  #print(resultado)
  return resultado

# %%
def AStar(frontera_act, visitados, solucion, meta, n_iteraciones):
  n_iteraciones = n_iteraciones + 1
  frontera = frontera_act[:]
  print("Inicio",frontera)
  if len(frontera) == 0:
    return []
  nodo = frontera.pop(0)
  solucion.append(nodo[0])
  if criterioAceptacion(nodo[0], meta):
    return solucion
  print("Nod", nodo[0])
  nuevas_soluciones = generarSoluciones(nodo[0][0], nodo[0][1])
  print("Sol",nuevas_soluciones)
  nuevas_soluciones = eliminaPosibilidadeIguales(nuevas_soluciones, visitados)
  print("No obs", nuevas_soluciones)
  nuevas_soluciones_costo = []
  for sol in nuevas_soluciones:
    nuevas_soluciones_costo.append((sol, nodo[1] + 1))
  frontera = frontera + nuevas_soluciones_costo
  #print(frontera)
  frontera_ordenada = evaluacion_aStar(frontera, visitados)
  visitados.append(nodo[0])
  #LLamado recursivo
  return AStar(frontera_ordenada, visitados, solucion, meta, n_iteraciones)

# %%
def play_AStar():
  inicio = ([0,0,0], [3,3,1])
  meta = ([3,3,1], [0,0,0])
  inicio = (inicio, 0)
  visitados, solucion = [], []
  solAStar = AStar([inicio], visitados, solucion, meta, 0)
  print("Cantidad recorrida con AStar: {}".format(len(solAStar)))
  # El recorrido no se imprimirá si no llega a la solución, pero se puede ver mientras recorre nodos.
  print("Recorrido: {}".format(solAStar))
  imprimir_tablero(solAStar)
  if len(solAStar) == 0:
    print("No se encontro solucion")
    return

# %%
#play_AStar()

# %%
def menu():
    while True:
        print("\nSeleccione un algoritmo:")
        print("1. BFS")
        print("2. DFS")
        print("3. LDFS")
        print("4. ILDFS")
        print("5. Voraz")
        print("6. AStar")
        print("0. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            play_bfs()
        elif opcion == '2':
            play_dfs()
        elif opcion == '3':
            play_ldfs()
        elif opcion == '4':
            play_ildfs()
        elif opcion == '5':
            play_voraz()
        elif opcion == '6':
            play_AStar()
        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# %%
# Iniciar programa
menu()


