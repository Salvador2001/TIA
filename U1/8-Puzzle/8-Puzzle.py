# %% [markdown]
# # 8-Puzzle
# 
# Estructura del nodo:
# 
# [1,2,3,4,5,6,7,8,0] <-- Ejemplo de meta
# 
# meta[n-1] donde n es el elemento de la lista, tiene que coincidir con el índice de la lista.<br>
# Por ejemplo, if meta[n-1] and n=3 -> meta[x,x,n,x,x,x,x,...] debería ser correcto, ya que n=3 y está en la posición 3.

# %%
from collections import deque

class PlayBFS:
    def __init__(self, board, zero_pos, moves, path):
        self.board = board
        self.zero_pos = zero_pos  # posición del espacio vacío
        self.moves = moves  # número de movimientos realizados
        self.path = path  # camino de estados desde el inicio

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_possible_moves(self):
        possible_moves = []
        x, y = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero_pos = (new_x, new_y)
                new_board = self.board[:]
                zero_index = x * 3 + y
                new_index = new_x * 3 + new_y
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                # Agregar el nuevo estado al camino
                possible_moves.append(PlayBFS(new_board, new_zero_pos, self.moves + 1, self.path + [new_board]))

        return possible_moves

    def print_board(self):
        # Método para imprimir el tablero de forma visual
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")

def bfs(start_board):
    start_zero_pos = start_board.index(0)
    start_state = PlayBFS(start_board, (start_zero_pos // 3, start_zero_pos % 3), 0, [start_board])
    queue = deque([start_state])
    visited = set()

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return current_state.moves, current_state.path  # Retornar el número de movimientos y el camino

        visited.add(tuple(current_state.board))

        for next_state in current_state.get_possible_moves():
            if tuple(next_state.board) not in visited:
                queue.append(next_state)

    return -1, []  # No se encontró solución

# Ejemplo de uso
def execute_bfs():
    start_board = [3, 8, 6, 1, 2, 4, 5, 7, 0]  # Configuración inicial
    result, path = bfs(start_board)

    if result != -1:
        print(f"Se encontró solución en {result} movimientos.")
        print("Recorrido:")
        for step in path:
            state = PlayBFS(step, (step.index(0) // 3, step.index(0) % 3), 0, [])
            state.print_board()  # Imprimir el tablero visualmente
            print()
    else:
        print("No se encontró solución.")

# %%
class PuzzleState:
    def __init__(self, board, zero_pos, moves, path):
        self.board = board
        self.zero_pos = zero_pos  # posición del espacio vacío
        self.moves = moves  # número de movimientos realizados
        self.path = path  # camino de estados desde el inicio

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_possible_moves(self):
        possible_moves = []
        x, y = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero_pos = (new_x, new_y)
                new_board = self.board[:]
                zero_index = x * 3 + y
                new_index = new_x * 3 + new_y
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                possible_moves.append(PuzzleState(new_board, new_zero_pos, self.moves + 1, self.path + [new_board]))

        return possible_moves

    def print_board(self):
        # Método para imprimir el tablero de forma visual
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")

def dfs(start_board):
    start_zero_pos = start_board.index(0)
    start_state = PuzzleState(start_board, (start_zero_pos // 3, start_zero_pos % 3), 0, [start_board])
    stack = [start_state]  # Solo apilamos el estado inicial
    visited = set()

    while stack:
        current_state = stack.pop()  # Tomamos el último estado agregado

        # Usar un hash del estado actual para comprobar si ya fue visitado
        state_tuple = tuple(current_state.board)
        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if current_state.is_goal():
            return current_state.moves, current_state.path  # Retornar el número de movimientos y el camino

        # Agregar todos los posibles movimientos a la pila
        for next_state in current_state.get_possible_moves():
            stack.append(next_state)  # Agregamos nuevos estados a la pila

    return -1, []  # No se encontró solución

# Ejemplo de uso
def execute_dfs():
    start_board = [1, 2, 3, 4, 5, 6, 7, 0, 8]  # Configuración inicial
    result, path = dfs(start_board)

    if result != -1:
        print(f"Se encontró solución en {result} movimientos.")
        print("Recorrido:")
        for step in path:
            state = PuzzleState(step, (step.index(0) // 3, step.index(0) % 3), 0, [])
            state.print_board()  # Imprimir el tablero visualmente
            print()
    else:
        print("No se encontró solución.")


# %%
class PuzzleState:
    def __init__(self, board, zero_pos, moves, path):
        self.board = board
        self.zero_pos = zero_pos  # posición del espacio vacío
        self.moves = moves  # número de movimientos realizados
        self.path = path  # camino de estados desde el inicio

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_possible_moves(self):
        possible_moves = []
        x, y = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero_pos = (new_x, new_y)
                new_board = self.board[:]
                zero_index = x * 3 + y
                new_index = new_x * 3 + new_y
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                # Agregar el nuevo estado al camino
                possible_moves.append(PuzzleState(new_board, new_zero_pos, self.moves + 1, self.path + [new_board]))

        return possible_moves

    def print_board(self):
        # Método para imprimir el tablero de forma visual
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")

def ldfs(start_board, depth_limit):
    start_zero_pos = start_board.index(0)
    start_state = PuzzleState(start_board, (start_zero_pos // 3, start_zero_pos % 3), 0, [start_board])
    stack = [(start_state, 0)]  # Apilamos el estado y la profundidad actual
    visited = set()

    while stack:
        current_state, current_depth = stack.pop()  # Tomamos el último estado agregado

        if tuple(current_state.board) in visited:
            continue

        visited.add(tuple(current_state.board))

        if current_state.is_goal():
            return current_state.moves, current_state.path  # Retornar el número de movimientos y el camino

        if current_depth < depth_limit:
            for next_state in current_state.get_possible_moves():
                stack.append((next_state, current_depth + 1))  # Agregamos nuevos estados a la pila con profundidad incrementada

    return -1, []  # No se encontró solución

# Ejemplo de uso
def execute_ldfs():
    start_board = [3, 8, 6, 1, 2, 4, 5, 7, 0]  # Configuración inicial
    depth_limit = 105  # Establecer un límite de profundidad
    result, path = ldfs(start_board, depth_limit)

    if result != -1:
        print(f"Se encontró solución en {result} movimientos.")
        print("Recorrido:")
        for step in path:
            state = PuzzleState(step, (step.index(0) // 3, step.index(0) % 3), 0, [])
            state.print_board()  # Imprimir el tablero visualmente
            print()
    else:
        print("No se encontró solución.")


# %%
class PuzzleState:
    def __init__(self, board, zero_pos, moves, path):
        self.board = board
        self.zero_pos = zero_pos  # posición del espacio vacío
        self.moves = moves  # número de movimientos realizados
        self.path = path  # camino de estados desde el inicio

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_possible_moves(self):
        possible_moves = []
        x, y = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero_pos = (new_x, new_y)
                new_board = self.board[:]
                zero_index = x * 3 + y
                new_index = new_x * 3 + new_y
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                # Agregar el nuevo estado al camino
                possible_moves.append(PuzzleState(new_board, new_zero_pos, self.moves + 1, self.path + [new_board]))

        return possible_moves

    def print_board(self):
        # Método para imprimir el tablero de forma visual
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")

def ldfs_iterative(start_board):
    depth_limit = 0  # Inicializa el límite de profundidad
    while True:
        result, path = ldfs(start_board, depth_limit)
        if result != -1:
            return result, path
        depth_limit += 1  # Incrementa el límite de profundidad si no se encontró solución

def ldfs(start_board, depth_limit):
    start_zero_pos = start_board.index(0)
    start_state = PuzzleState(start_board, (start_zero_pos // 3, start_zero_pos % 3), 0, [start_board])
    stack = [(start_state, 0)]  # Apilamos el estado y la profundidad actual
    visited = set()

    while stack:
        current_state, current_depth = stack.pop()  # Tomamos el último estado agregado

        if tuple(current_state.board) in visited:
            continue

        visited.add(tuple(current_state.board))

        if current_state.is_goal():
            return current_state.moves, current_state.path  # Retornar el número de movimientos y el camino

        if current_depth < depth_limit:
            for next_state in current_state.get_possible_moves():
                stack.append((next_state, current_depth + 1))  # Agregamos nuevos estados a la pila con profundidad incrementada

    return -1, []  # No se encontró solución

# Ejemplo de uso
def execute_ildfs():
    start_board = [3, 8, 6, 1, 2, 4, 5, 7, 0]  # Configuración inicial
    result, path = ldfs_iterative(start_board)

    if result != -1:
        print(f"Se encontró solución en {result} movimientos.")
        print("Recorrido:")
        for step in path:
            state = PuzzleState(step, (step.index(0) // 3, step.index(0) % 3), 0, [])
            state.print_board()  # Imprimir el tablero visualmente
            print()
    else:
        print("No se encontró solución.")


# %%
class PuzzleState:
    def __init__(self, board, zero_pos, moves, path):
        self.board = board
        self.zero_pos = zero_pos  # posición del espacio vacío
        self.moves = moves  # número de movimientos realizados
        self.path = path  # camino de estados desde el inicio

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_possible_moves(self):
        possible_moves = []
        x, y = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero_pos = (new_x, new_y)
                new_board = self.board[:]
                zero_index = x * 3 + y
                new_index = new_x * 3 + new_y
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                possible_moves.append(PuzzleState(new_board, new_zero_pos, self.moves + 1, self.path + [new_board]))

        return possible_moves

    def heuristic(self):
        """ Calcula la distancia de Manhattan como heurística. """
        total_distance = 0
        for i in range(1, 9):  # Excluimos el 0 (espacio vacío)
            current_index = self.board.index(i)
            target_index = i - 1  # La posición objetivo es i-1
            current_x, current_y = divmod(current_index, 3)
            target_x, target_y = divmod(target_index, 3)
            total_distance += abs(current_x - target_x) + abs(current_y - target_y)
        return total_distance

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")

def is_solvable(board):
    # Contar el número de inversiones
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] != 0 and board[j] != 0 and board[i] > board[j]:
                inversions += 1
    return inversions % 2 == 0

def greedy_search(start_board):
    if not is_solvable(start_board):
        return -1, []
    start_zero_pos = start_board.index(0)
    start_state = PuzzleState(start_board, (start_zero_pos // 3, start_zero_pos % 3), 0, [start_board])
    
    frontier = [start_state]  # Usamos una lista como la frontera
    visited = set()

    while frontier:
        # Ordenamos la frontera por la heurística
        frontier.sort(key=lambda state: state.heuristic())
        current_state = frontier.pop(0)  # Tomamos el estado con menor heurística

        if tuple(current_state.board) in visited:
            continue

        visited.add(tuple(current_state.board))

        if current_state.is_goal():
            return current_state.moves, current_state.path  # Retornar el número de movimientos y el camino

        for next_state in current_state.get_possible_moves():
            if tuple(next_state.board) not in visited:
                frontier.append(next_state)

    return -1, []  # No se encontró solución

# Ejemplo de uso
def execute_voraz():
    start_board = [3, 8, 6, 1, 2, 4, 5, 7, 0]  # Configuración inicial
    result, path = greedy_search(start_board)

    if result != -1:
        print(f"Se encontró solución en {result} movimientos.")
        print("Recorrido:")
        for step in path:
            state = PuzzleState(step, (step.index(0) // 3, step.index(0) % 3), 0, [])
            state.print_board()  # Imprimir el tablero visualmente
            print()
    else:
        print("No se encontró solución.")


# %%
class PuzzleState:
    def __init__(self, board, zero_pos, moves, path):
        self.board = board
        self.zero_pos = zero_pos  # posición del espacio vacío
        self.moves = moves  # número de movimientos realizados
        self.path = path  # camino de estados desde el inicio

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_possible_moves(self):
        possible_moves = []
        x, y = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero_pos = (new_x, new_y)
                new_board = self.board[:]
                zero_index = x * 3 + y
                new_index = new_x * 3 + new_y
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                possible_moves.append(PuzzleState(new_board, new_zero_pos, self.moves + 1, self.path + [new_board]))

        return possible_moves

    def heuristic(self):
        """ Calcula la distancia de Manhattan como heurística. """
        total_distance = 0
        for i in range(1, 9):  # Excluimos el 0 (espacio vacío)
            current_index = self.board.index(i)
            target_index = i - 1  # La posición objetivo es i-1
            current_x, current_y = divmod(current_index, 3)
            target_x, target_y = divmod(target_index, 3)
            total_distance += abs(current_x - target_x) + abs(current_y - target_y)
        return total_distance

    def f_cost(self):
        return self.moves + self.heuristic()

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")

def is_solvable(board):
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] != 0 and board[j] != 0 and board[i] > board[j]:
                inversions += 1
    return inversions % 2 == 0

def a_star_search(start_board):
    if not is_solvable(start_board):
        return -1, []

    start_zero_pos = start_board.index(0)
    start_state = PuzzleState(start_board, (start_zero_pos // 3, start_zero_pos % 3), 0, [start_board])
    
    frontier = [start_state]  # Usamos una lista como la frontera
    visited = set()

    while frontier:
        # Ordenamos la frontera por el costo total f(n)
        frontier.sort(key=lambda state: state.f_cost())
        current_state = frontier.pop(0)  # Tomamos el estado con menor costo f(n)

        if tuple(current_state.board) in visited:
            continue

        visited.add(tuple(current_state.board))

        if current_state.is_goal():
            return current_state.moves, current_state.path  # Retornar el número de movimientos y el camino

        for next_state in current_state.get_possible_moves():
            if tuple(next_state.board) not in visited:
                frontier.append(next_state)

    return -1, []  # No se encontró solución

# Ejemplo de uso
def execute_AStar():
    start_board = [3, 8, 6, 1, 2, 4, 5, 7, 0]  # Configuración inicial
    result, path = a_star_search(start_board)

    if result != -1:
        print(f"Se encontró solución en {result} movimientos.")
        print("Recorrido:")
        for step in path:
            state = PuzzleState(step, (step.index(0) // 3, step.index(0) % 3), 0, [])
            state.print_board()  # Imprimir el tablero visualmente
            print()
    else:
        print("No se encontró solución.")


# %%
def menu():
    while True:
        print("\n8-Puzzle")
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
            execute_bfs()
        elif opcion == '2':
            print("\nUsando DFS...")
            execute_dfs()
        elif opcion == '3':
            print("\nUsando LDFS...")
            execute_ldfs()
        elif opcion == '4':
            print("\nUsando ILDFS...")
            execute_ildfs()
        elif opcion == '5':
            print("\nUsando Voraz...")
            execute_voraz()
        elif opcion == '6':
            print("\nUsando AStar...")
            execute_AStar()
        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# %%
menu()


