# %% [markdown]
# ### Teoría del problema
# Se requiere almacenar todos los nodos posibles, además debe haber una forma en la que se pueda obtener los vecinos del nodo actual. Se podría tener una lista que almacene una serie de tuplas que contienen el Punto A, Punto B y el costo (distancia) para cada uno de los nodos (ciudades) y hacer un chequeo en la función que genera soluciones.
# 
# [ <br>
# (Arad, Arad, 0) <-- Se usaría como nodo inicial <br>
# (Arad, Zerind, 75) <br>
# (Arad, Sibiu, 140) <br>
# (Arad, Timisoara, 118) <br>
# ] <br>
# 
# La distancia no sería relevante para los primeros 4 algoritmos, si no hasta que se llegue a usar en los que requieren heurística (Voraz, AEstrella, etc). Cada ciudad debe tener un nodo que se conecte consigo mismo como en el nodo inicial, pero el algoritmo debe evitar estos nodos a menos que sea el nodo destino (meta), esto es para casos en que se requiera cambiar el inicio y la meta.

# %%
ciudades = [
    ("Arad","Arad",0),
    ("Arad","Zerind",75),
    ("Arad","Sibiu",140),
    ("Arad","Timisoara",118),
    ("Zerind","Zerind",0),
    ("Zerind","Oradea",71),
    ("Oradea","Oradea",0),
    ("Oradea","Sibiu",151),
    ("Timisoara","Timisoara",0),
    ("Timisoara","Lugoj",111),
    ("Lugoj","Lugoj",0),
    ("Lugoj","Mehadia",70),
    ("Mehadia","Mehadia",0),
    ("Mehadia","Drobeta",75),
    ("Drobeta","Drobeta",0),
    ("Drobeta","Craiova",120),
    ("Sibiu","Sibiu",0),
    ("Sibiu","Fagaras",99),
    ("Sibiu","Rimnicu Vilcea",80),
    ("Rimnicu Vilcea","Rimnicu Vilcea",0),
    ("Rimnicu Vilcea","Pitesti",97),
    ("Rimnicu Vilcea","Craiova",146),
    ("Craiova","Craiova",0),
    ("Craiova","Pitesti",138),
    ("Pitesti","Bucharest",101),
    ("Bucharest","Bucharest",0),
    ("Fagaras","Fagaras",0),
    ("Fagaras","Bucharest",211),
    ("Bucharest","Giurgiu",90),
    ("Giurgiu","Giurgiu",0),
    ("Bucharest","Urziceni",85),
    ("Urziceni","Urziceni",0),
    ("Urziceni","Hirsova",98),
    ("Urziceni","Vaslui",142),
    ("Hirsova","Hirsova",0),
    ("Hirsova","Eforie",86),
    ("Eforie","Eforie",0),
    ("Vaslui","Vaslui",0),
    ("Vaslui","Iasi",92),
    ("Iasi","Iasi",0),
    ("Iasi","Neamt",87),
    ("Neamt","Neamt",0)
]

# %%
#Función para verificar si se cumple la condición de llegar a meta
def criterioAceptacion(posicion, meta):
  return posicion == meta

# %%
print(criterioAceptacion(("Bucarest","Bucarest",0), ("Bucarest","Bucarest",0)))
print(criterioAceptacion(("Arad","Sibiu",140), ("Bucarest","Bucarest",0)))

# %% [markdown]
# Para generar las soluciones, la función debe revisar el Punto B del nodo actual, y regresar los posibles nodos que contengan ese Punto B como Punto A, por ejemplo: <br>
# 
# Nodo: (A,B,n) <br>
# ... <br>
# Soluciones: <br>
# (B,X,n) <br>
# (B,Y,n) <br>
# (B,Z,n) <br>
# (B,B,0) <br>
# 
# En todos los casos, se omitiría la última solución a menos que sea la meta.

# %%
#Función que permite generar todas las posibles soluciones
#En este caso genera todos los posibles movimientos del estado actual
def generarSoluciones(actual, meta):
  soluciones = []
  
  #Generar posibles soluciones
  for nodo in ciudades:
    if nodo[0] == actual[1] and nodo == meta:
      soluciones.append(nodo)
    elif nodo[0] == actual[1] and nodo[0] != nodo[1]:
      soluciones.append(nodo)
  return soluciones

# %%
generarSoluciones(("Arad","Zerind",75), ("Bucharest","Bucharest",0))

# %%
def validar(actual, visitados):
    #print("validar actual: {}".format(actual))
    #print("validar visitados: {}".format(visitados))
    if len(visitados) == 0:
        return True
    else:
        if visitados[-1][1] == actual[0]:
            return True

# %%
validar(("Zerind","Oradea",71),[("Arad", "Zerind", 75)])

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
  if cabeza not in visitados and validar(cabeza, visitados):
    #print("entró: {}".format(cabeza))
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
    nuevas_soluciones = generarSoluciones(cabeza, meta)
    print("Nuevas soluciones: {}".format(nuevas_soluciones))
    #Se agregan los elementos nuevos al final de la lista para simular una cola
    frontera = frontera + nuevas_soluciones
  #Se hace un llamado recursivo
  return BFS(frontera, visitados, solucion, meta, n_iteraciones)

# %%
#Función que utiliza todos las funciones creadas para hacer la simulación
def play_bfs():
  inicio = ("Arad","Arad",0)
  meta = ("Bucharest","Bucharest",0)
  visitados, solucion = [], []
  solBFS = BFS([inicio], visitados, solucion, meta, 0)
  print("Cantidad recorrida con BFS: {}".format(len(solBFS)))
  print("Recorrido: {}".format(solBFS))
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
  if cabeza not in visitados and validar(cabeza, visitados):
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
    nuevas_soluciones = generarSoluciones(cabeza, meta)
    print("Nuevas soluciones: {}".format(nuevas_soluciones))
    #Se agregan los elementos nuevos al inicio de la lista para simular una pila
    frontera = nuevas_soluciones + frontera
  #Se hace un llamado recursivo
  return DFS(frontera, visitados, solucion, meta, n_iteraciones)

# %%
#Función que utiliza todos las funciones creadas para hacer la simulación
def play_dfs():
  inicio = ("Arad","Arad",0)
  meta = ("Bucharest","Bucharest",0)
  visitados, solucion = [], []
  solDFS = DFS([inicio], visitados, solucion, meta, 0)
  print("Cantidad recorrida con DFS: {}".format(len(solDFS)))
  print("Recorrido: {}".format(solDFS))
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
profundidad((("Arad","Arad",0),1), (('Arad', 'Zerind', 75),3))

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
  if cabeza[0] not in visitados and validar(cabeza[0], visitados):
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
      nuevas_soluciones = generarSoluciones(cabeza[0], meta)
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
  limite = 4
  inicio = ("Arad","Arad",0)
  meta = ("Bucharest","Bucharest",0)
  visitados, solucion = [], []
  solLDFS = LDFS([(inicio,0)], visitados, solucion, meta, 0, (inicio, 0), limite)
  print("Cantidad recorrida con LDFS: {}".format(len(solLDFS)))
  # El recorrido no se imprimirá si no llega a la solución, pero se puede ver mientras recorre nodos.
  print("Recorrido: {}".format(solLDFS))
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
  inicio = ("Arad","Arad",0)
  meta = ("Bucharest","Bucharest",0)
  solILDFS = ILDFS([(inicio,0)], limite, inicio, meta, 0)
  print("Cantidad recorrida con ILDFS: {}".format(len(solILDFS)))
  # El recorrido no se imprimirá si no llega a la solución, pero se puede ver mientras recorre nodos.
  print("Recorrido: {}".format(solILDFS))
  if len(solILDFS) == 0:
    print("No se encontro solucion")
    return

# %%
#play_ildfs()

# %%
def evaluacionVoraz(posibilidades):
  best_val = 100000
  best = None
  for posible in posibilidades:
    #val = distanciaEuclidiana(posible, meta)
    val = posible[2]
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
  nuevas_soluciones = generarSoluciones(nodo, meta)
  print("Nuevas soluciones: {}".format(nuevas_soluciones))
  #print(nuevas_soluciones)
  nuevas_soluciones = eliminaPosibilidadeIguales(nuevas_soluciones, visitados)
  #print(nuevas_soluciones)
  mejor = evaluacionVoraz(nuevas_soluciones)
  #print(mejor)
  visitados.append(nodo)
  return voraz(mejor, visitados, solucion, meta, n_iteraciones)

# %%
def play_voraz():
  inicio = ("Arad","Arad",0)
  meta = ("Bucharest","Bucharest",0)
  visitados, solucion = [], []
  solVoraz = voraz(inicio, visitados, solucion, meta, 0)
  print("Cantidad recorrida con voraz: {}".format(len(solVoraz)))
  # El recorrido no se imprimirá si no llega a la solución, pero se puede ver mientras recorre nodos.
  print("Recorrido: {}".format(solVoraz))
  if len(solVoraz) == 0:
    print("No se encontro solucion")
    return

# %%
#play_voraz()

# %%
distancias=[
    ("Arad", 366),
    ("Zerind", 374),
    ("Oradea", 380),
    ("Timisoara", 329),
    ("Lugoj", 244),
    ("Mehadia", 241),
    ("Drobeta", 242),
    ("Sibiu", 253),
    ("Rimnicu Vilcea", 193),
    ("Craiova", 160),
    ("Fagaras", 176),
    ("Pitesti", 100),
    ("Bucharest", 0),
    ("Giurgiu", 77),
    ("Urziceni", 80),
    ("Hirsova", 151),
    ("Eforie", 161),
    ("Neamt", 234),
    ("Iasi", 226),
    ("Vaslui", 199)
]

# %%
def getDistancia(ciudad):
    for capital in distancias:
        if capital[0] == ciudad:
            return capital[1]

# %%
#Función que evalua cada posibilidad y ordena la lista de menor a mayor en este caso.
def evaluacion_aStar(posibilidades, visitados):
  evaluaciones = []
  for posible in posibilidades:
    if posible not in visitados:
        #Se suma g(n) + h(n)
        valor = getDistancia(posible[0][0]) + posible[0][2]
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
  nuevas_soluciones = generarSoluciones(nodo[0], meta)
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
  inicio = ("Arad","Arad",0)
  meta = ("Bucharest","Bucharest",0)
  inicio = (inicio, 0)
  visitados, solucion = [], []
  solAStar = AStar([inicio], visitados, solucion, meta, 0)
  print("Cantidad recorrida con AStar: {}".format(len(solAStar)))
  # El recorrido no se imprimirá si no llega a la solución, pero se puede ver mientras recorre nodos.
  print("Recorrido: {}".format(solAStar))
  #imprimir_tablero(solAStar)
  if len(solAStar) == 0:
    print("No se encontro solucion")
    return

# %%
#play_AStar()

# %%
def menu():
    while True:
        print("\nProblema del viajero")
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
            print("\nUsando BFS...")
            play_bfs()
        elif opcion == '2':
            print("\nUsando DFS...")
            play_dfs()
        elif opcion == '3':
            print("\nUsando LDFS...")
            play_ldfs()
        elif opcion == '4':
            print("\nUsando ILDFS...")
            play_ildfs()
        elif opcion == '5':
            print("\nUsando Voraz...")
            play_voraz()
        elif opcion == '6':
            print("\nUsando AStar...")
            play_AStar()
        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# %%
# Iniciar programa
menu()


