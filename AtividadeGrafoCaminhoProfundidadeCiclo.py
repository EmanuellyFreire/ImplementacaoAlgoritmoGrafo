from collections import deque

## EXERCICIO 3

def criar_grafo():
  return [], []


def inserir_vertice(vertices, arestas, vertice):
  if vertice in vertices:
    print(f"Vértice '{vertice}' já existe.")
    return
  vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
  if origem not in vertices:
    inserir_vertice(vertices, arestas, origem)
  if destino not in vertices:
    inserir_vertice(vertices, arestas, destino)

  if (origem, destino) not in arestas:
    arestas.append((origem, destino))

  if nao_direcionado and (destino, origem) not in arestas:
    arestas.append((destino, origem))


def remover_vertice(vertices, arestas, vertice):
  if vertice not in vertices:
    print(f"Vértice '{vertice}' não existe.")
    return

  vertices.remove(vertice)

  arestas[:] = [a for a in arestas if a[0] != vertice and a[1] != vertice]


def remover_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
  if (origem, destino) in arestas:
    arestas.remove((origem, destino))

  if nao_direcionado and (destino, origem) in arestas:
    arestas.remove((destino, origem))


def existe_aresta(vertices, arestas, origem, destino):
  return (origem, destino) in arestas


def vizinhos(vertices, arestas, vertice):
  if vertice not in vertices:
    return []

  return [dest for (orig, dest) in arestas if orig == vertice]


def grau_vertices(vertices, arestas):
    print("\n=== Grau dos Vértices ===")

    for v in vertices:
        saida = sum(1 for (o, _) in arestas if o == v)
        entrada = sum(1 for (_, d) in arestas if d == v)
        total = entrada + saida

        print(f"{v}: Entrada={entrada}, Saída={saida}, Total={total}")


def percurso_valido(vertices, arestas, caminho):
  for i in range(len(caminho) - 1):
    if not existe_aresta(vertices, arestas, caminho[i], caminho[i+1]):
      return False
  return True


def listar_vizinhos(vertices, arestas, vertice):
  if vertice not in vertices:
    print("Vértice não existe.")
    return

  print(f"Vizinhos de {vertice}: {vizinhos(vertices, arestas, vertice)}")


def exibir_grafo(vertices, arestas):
  print("\nVértices:", vertices)
  print("Arestas:", arestas)


def caminho_all_vertices(vertices, arestas):
  if not vertices:
    return []

  fila = [] # fila
# 1. insere o vertice inicial na fila
  fila.append(vertices[0])
# 2. inicia a lista de visitados vazia
  visitados = []
# 3. enquanto a fila não estiver vazia
  while fila:
  # a. retira o 1 vertice da fila
    vertice = fila.pop(0)
  # b. verifica se o vertice já foi visitado
    if vertice not in visitados:
  # b. manca vértice como visitado
      visitados.append(vertice)

  # c. obtem vizinhos do vértice
      vizinhos_vertice = vizinhos(vertices, arestas, vertice)
  # d. para cada vizinho:
      for vizinho in vizinhos_vertice:
        # i. verifica se o vizinho não esta na fila
        # ii. verifica se o vizinho já não foi vizitado
        if vizinho not in fila and vizinho not in visitados:
    # iii. caso não esteja na fila e não tenha sido visitado, adiciona o vizinho na fila
          fila.append(vizinho)
# 4. retorna os visitados
  return visitados


def menor_caminho_bfs(vertices, arestas, inicio, destino):
  # Verificações básicas
  if inicio not in vertices or destino not in vertices:
    print("Um dos vértices informados não existe.")
    return []

  # Fila de dicionários com vértice atual e caminho até ele
  fila = deque([{'vertice': inicio, 'caminho': [inicio]}])
  visitados = []

  while fila:
    item = fila.popleft()
    vertice_atual = item['vertice']
    caminho_atual = item['caminho']


    if vertice_atual == destino:
      return caminho_atual


    visitados.append(vertice_atual)


    for vizinho in vizinhos(vertices, arestas, vertice_atual):
      if vizinho not in visitados:
        fila.append({
          'vertice': vizinho,
          'caminho': caminho_atual + [vizinho]
        })

  return []


def busca_profundidade_padrao(vertices, arestas):
  if not vertices:
    return []

  pilha = []
  # inicia a lista de vizitados vazia
  visitados = []
  # insere o vertice inicial na pilha
  pilha.append(vertices[0])
  # enquanto a pilha não estiver vazia:
  while pilha:
    # retira o vertice da pilha
    vertice = pilha.pop()
    # marca vertice como vizitado
    if vertice not in visitados:
      visitados.append(vertice)

      for vizinho in reversed(vizinhos(vertices, arestas, vertice)):
        if vizinho not in visitados:
          pilha.append(vizinho)

  return visitados




def detectar_ciclo(vertices, arestas):
# inserir a estrutura com vertice inicial e pai vazio na fila
  fila = []
  fila.append({'vertice': vertices[0], 'pai': None})
  # inicar a lista de vizitados vazia
  visitados = []
  # enquanto a pilha não estiver vazia:
  while fila:
    # retira o vertice da pilha
    item = fila.pop(0)
    vertice = item['vertice']
    pai = item['pai']
    # marcar vertice do item como vizitado
    if vertice not in visitados:
      visitados.append(vertice)
      # obtem os vizinhos do vertice
      vizinhos_vertice = vizinhos(vertices, arestas, vertice)
      # para cada vizinho:
      for vizinho in vizinhos_vertice:
        # verifica se o vizinho não esta na pilha e se já não foi vizitado
        if vizinho not in visitados:
          # caso falso para os dois: adciona o viziho na pilha com o vertice atual como pai
          fila.append({'vertice': vizinho, 'pai': vertice})
          # se nao:
        elif vizinho != pai:
          # caso o vizinho nao seja o pai
          # retorna verdadeiro
          return True
  # retorna falso
  return False





def main():
  vertices, arestas = criar_grafo()

  while True:
    print("\n=== MENU — LISTA DE ARESTAS ===")
    print("1 - Mostrar Grafo")
    print("2 - Inserir Vértice")
    print("3 - Inserir Aresta")
    print("4 - Remover Vértice")
    print("5 - Remover Aresta")
    print("6 - Verificar Aresta")
    print("7 - Listar Vizinhos")
    print("8 - Grau dos Vértices")
    print("9 - Verificar Percurso")
    print("10 - Caminho passando por todos os vertices")
    print("11 - Menor caminho")
    print("12 - Busca por profundidade padrão")
    print("13 - Detectar ciclo")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "0":
      print("Encerrado!")
      break

    elif op == "1":
      exibir_grafo(vertices, arestas)

    elif op == "2":
      v = input("Vértice: ")
      inserir_vertice(vertices, arestas, v)

    elif op == "3":
      o = input("Origem: ")
      d = input("Destino: ")
      nd = input("Não direcionado? (s/n): ").lower() == "s"
      inserir_aresta(vertices, arestas, o, d, nd)

    elif op == "4":
      v = input("Vértice: ")
      remover_vertice(vertices, arestas, v)

    elif op == "5":
      o = input("Origem: ")
      d = input("Destino: ")
      nd = input("Não direcionado? (s/n): ").lower() == "s"
      remover_aresta(vertices, arestas, o, d, nd)

    elif op == "6":
      o = input("Origem: ")
      d = input("Destino: ")
      print("Existe aresta?", existe_aresta(vertices, arestas, o, d))

    elif op == "7":
      v = input("Vértice: ")
      listar_vizinhos(vertices, arestas, v)

    elif op == "8":
      grau_vertices(vertices, arestas)

    elif op == "9":
      caminho = input("Caminho (ex: A B C): ").split()
      print("Percurso válido?", percurso_valido(vertices, arestas, caminho))

    elif op == "10":
      print("Vertices: ", vertices)
      print("Aestas: ", arestas)
      print("Caminho completo: ", caminho_all_vertices(vertices, arestas))

    elif op == "11":
      inicio = input("Vértice inicial: ")
      destino = input("Vértice destino: ")
      caminho = menor_caminho_bfs(vertices, arestas, inicio, destino)
      if caminho:
        print("Menor caminho encontrado:", " → ".join(caminho))
      else:
        print("Não existe caminho entre os vértices.")



    elif op == "12":
      print("Vertices: ", vertices)
      print("Aestas: ", arestas)
      print(busca_profundidade_padrao(vertices, arestas))

    elif op == "13":
      print("Vertices: ", vertices)
      print("Aestas: ", arestas)
      print(detectar_ciclo(vertices, arestas))

    else:
      print("Opção inválida!")


if __name__ == "__main__":
  main()
