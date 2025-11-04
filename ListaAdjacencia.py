# EXERCICIO 1

def criar_grafo():
    return {}


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
    else:
        print(f"Vértice '{vertice}' já existe.")


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)

    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)


def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []


def listar_vizinhos(grafo, vertice):
    if vertice not in grafo:
        print(f"Vértice '{vertice}' não existe.")
        return
    print(f"Vizinhos de {vertice}: {grafo[vertice]}")


def exibir_grafo(grafo):
    if not grafo:
        print("Grafo vazio.")
        return

    print("\n=== Lista de Adjacência ===")
    for v in sorted(grafo.keys()):
        print(f"{v} -> {grafo[v]}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)

    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        print(f"Vértice '{vertice}' não existe.")
        return

    for v in grafo:
        if vertice in grafo[v]:
            grafo[v].remove(vertice)

    del grafo[vertice]


def existe_aresta(grafo, origem, destino):
    if origem in grafo and destino in grafo[origem]:
        return True
    return False


def grau_vertices(grafo):
    graus = {}

    for v in grafo:
        out_degree = len(grafo[v])
        in_degree = 0

        for u in grafo:
            if v in grafo[u]:
                in_degree += 1

        graus[v] = {
            "entrada": in_degree,
            "saida": out_degree,
            "total": in_degree + out_degree
        }

    print("\n=== Grau dos Vértices ===")
    for v, g in graus.items():
        print(f"{v}: In={g['entrada']} | Out={g['saida']} | Total={g['total']}")


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        if not existe_aresta(grafo, caminho[i], caminho[i + 1]):
            return False
    return True


def main():
    grafo = criar_grafo()

    while True:
        print("\n=== MENU ===")
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

        opc = input("Escolha: ")

        if opc == "0":
            print("Encerrando...")
            break

        elif opc == "1":
            exibir_grafo(grafo)

        elif opc == "2":
            v = input("Vértice: ")
            inserir_vertice(grafo, v)

        elif opc == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(grafo, o, d, nd)

        elif opc == "4":
            v = input("Vértice: ")
            remover_vertice(grafo, v)

        elif opc == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            remover_aresta(grafo, o, d, nd)

        elif opc == "6":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe?" , existe_aresta(grafo, o, d))

        elif opc == "7":
            v = input("Vértice: ")
            listar_vizinhos(grafo, v)

        elif opc == "8":
            grau_vertices(grafo)

        elif opc == "9":
            caminho = input("Caminho (ex: A B C): ").split()
            print("Percurso válido?", percurso_valido(grafo, caminho))

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()




