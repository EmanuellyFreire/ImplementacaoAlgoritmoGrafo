## EXERCICIO 2

def criar_grafo():
    return [], [] 


def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print(f"Vértice '{vertice}' já existe!")
        return

    vertices.append(vertice)
    tamanho = len(vertices)

    for linha in matriz:
        linha.append(0)

    matriz.append([0] * tamanho)


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1

    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return

    idx = vertices.index(vertice)

    matriz.pop(idx)

    for linha in matriz:
        linha.pop(idx)

    vertices.remove(vertice)


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        print("Um dos vértices não existe.")
        return

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 0
    if nao_direcionado:
        matriz[j][i] = 0


def existe_aresta(matriz, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        return False

    i = vertices.index(origem)
    j = vertices.index(destino)

    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []

    i = vertices.index(vertice)
    viz = []

    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            viz.append(vertices[j])

    return viz


def grau_vertices(matriz, vertices):
    print("\n=== Grau dos Vértices ===")

    for i, v in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum(matriz[j][i] for j in range(len(vertices)))
        total = entrada + saída

        print(f"{v}: Entrada={entrada}, Saída={saida}, Total={total}")


def percurso_valido(matriz, vertices, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(matriz, vertices, caminho[i], caminho[i+1]):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return

    viz = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de {vertice}: {viz}")


def exibir_grafo(matriz, vertices):
    if not vertices:
        print("Grafo vazio.")
        return

    print("\n   ", " ".join(vertices))
    for i, v in enumerate(vertices):
        print(f"{v}  ", " ".join(map(str, matriz[i])))


def main():
    matriz, vertices = criar_grafo()

    while True:
        print("\n=== MENU — MATRIZ DE ADJACÊNCIA ===")
        print("1 - Mostrar Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Verificar Aresta")
        print("7 - Listar Vizinhos")
        print("8 - Grau dos Vértices")
        print("9 - Verificar Percurso")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "0":
            print("Finalizado!")
            break

        elif op == "1":
            exibir_grafo(matriz, vertices)

        elif op == "2":
            v = input("Vértice: ")
            inserir_vertice(matriz, vertices, v)

        elif op == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(matriz, vertices, o, d, nd)

        elif op == "4":
            v = input("Vértice: ")
            remover_vertice(matriz, vertices, v)

        elif op == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            remover_aresta(matriz, vertices, o, d, nd)

        elif op == "6":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(matriz, vertices, o, d))

        elif op == "7":
            v = input("Vértice: ")
            listar_vizinhos(matriz, vertices, v)

        elif op == "8":
            grau_vertices(matriz, vertices)

        elif op == "9":
            caminho = input("Digite o percurso (ex: A B C): ").split()
            print("Percurso válido?", percurso_valido(matriz, vertices, caminho))

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
