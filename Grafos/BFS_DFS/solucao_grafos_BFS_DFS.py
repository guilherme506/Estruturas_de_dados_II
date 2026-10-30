"""
solucao_grafos.py
Disciplina: Estrutura de Dados II – Ciência da Computação
Estudo de caso: pane relacionada ao GPS (simulação didática)

Autor: [Guilherme Borges Galvão]
"""

from collections import deque
from typing import Dict, List, Optional


# ============================================================
# Modelagem do grafo (lista de adjacência)
# Grafo não dirigido com 9 vértices
# ============================================================

GRAFO: Dict[str, List[str]] = {
    "Brasília": ["Goiânia", "Belo Horizonte", "Cuiabá"],
    "Goiânia": ["Brasília", "São Paulo", "Cuiabá", "Campo Grande"],
    "Belo Horizonte": ["Brasília", "Rio de Janeiro", "São Paulo"],
    "São Paulo": ["Goiânia", "Belo Horizonte", "Curitiba", "Rio de Janeiro"],
    "Cuiabá": ["Brasília", "Goiânia", "Campo Grande", "Curitiba"],
    "Rio de Janeiro": ["Belo Horizonte", "São Paulo", "Curitiba"],
    "Curitiba": ["São Paulo", "Cuiabá", "Rio de Janeiro", "Florianópolis"],
    "Campo Grande": ["Goiânia", "Cuiabá"],
    "Florianópolis": ["Curitiba"],
}


def imprimir_grafo(rede: Dict[str, List[str]]) -> None:
    print("\n=== Lista de Adjacência ===")
    for vertice in sorted(rede.keys()):
        vizinhos = ", ".join(rede[vertice]) if rede[vertice] else "(nenhum)"
        print(f"  {vertice}: [{vizinhos}]")


# ============================================================
# BFS – Busca em Largura (fila FIFO)
# ============================================================

def bfs(rede: Dict[str, List[str]], origem: str, destino: str) -> Optional[List[str]]:
    """Retorna caminho com menor número de arestas (grafo não ponderado)."""
    if origem not in rede or destino not in rede:
        return None

    fila = deque([(origem, [origem])])
    visitados = {origem}

    while fila:
        atual, caminho = fila.popleft()

        if atual == destino:
            return caminho

        for vizinho in rede.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return None


# ============================================================
# DFS – Busca em Profundidade (pilha LIFO)
# ============================================================

def dfs(rede: Dict[str, List[str]], origem: str, destino: str) -> Optional[List[str]]:
    """Retorna um caminho qualquer (não necessariamente o menor)."""
    if origem not in rede or destino not in rede:
        return None

    pilha = [(origem, [origem])]
    visitados = set()

    while pilha:
        atual, caminho = pilha.pop()

        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == destino:
            return caminho

        for vizinho in reversed(rede.get(atual, [])):
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho]))

    return None


# ============================================================
# Simulação de bloqueio (não altera o grafo original)
# ============================================================

def bloquear_conexao(rede: Dict[str, List[str]], a: str, b: str) -> Dict[str, List[str]]:
    """Cria cópia do grafo e remove a aresta a–b nos dois sentidos."""
    copia = {no: vizinhos.copy() for no, vizinhos in rede.items()}

    if b in copia.get(a, []):
        copia[a].remove(b)
    if a in copia.get(b, []):
        copia[b].remove(a)

    return copia


# ============================================================
# Utilitários
# ============================================================

def formatar_caminho(caminho: Optional[List[str]]) -> str:
    if caminho is None:
        return "Nenhum caminho encontrado"
    arestas = len(caminho) - 1
    return f"{' → '.join(caminho)}  ({arestas} aresta{'s' if arestas != 1 else ''})"


def executar_busca(rede: Dict[str, List[str]], origem: str, destino: str, nome_cenario: str) -> None:
    print(f"\n--- Cenário: {nome_cenario} ---")
    print(f"Origem: {origem}  |  Destino: {destino}")

    caminho_bfs = bfs(rede, origem, destino)
    caminho_dfs = dfs(rede, origem, destino)

    print(f"BFS: {formatar_caminho(caminho_bfs)}")
    print(f"DFS: {formatar_caminho(caminho_dfs)}")


def validar_vertice(rede: Dict[str, List[str]], nome: str) -> bool:
    return nome in rede


# ============================================================
# Programa principal
# ============================================================

def main() -> None:
    print("=" * 60)
    print("  SIMULAÇÃO DE ROTAS AÉREAS – BFS e DFS")
    print("  Estudo de caso: pane relacionada ao GPS (didático)")
    print("=" * 60)

    imprimir_grafo(GRAFO)

    # ---------- Testes automáticos ----------
    print("\n" + "=" * 60)
    print("  TESTES AUTOMÁTICOS")
    print("=" * 60)

    origem_padrao = "Brasília"
    destino_padrao = "Curitiba"

    # Experimento A – rede completa
    executar_busca(GRAFO, origem_padrao, destino_padrao, "Rede completa (sem bloqueios)")

    # Experimento B – bloqueio Goiânia–São Paulo
    rede_bloqueada1 = bloquear_conexao(GRAFO, "Goiânia", "São Paulo")
    executar_busca(rede_bloqueada1, origem_padrao, destino_padrao,
                   "Bloqueio: Goiânia ↔ São Paulo")

    # Experimento C – segundo bloqueio
    rede_bloqueada2 = bloquear_conexao(rede_bloqueada1, "Cuiabá", "Curitiba")
    executar_busca(rede_bloqueada2, origem_padrao, destino_padrao,
                   "Bloqueio adicional: Cuiabá ↔ Curitiba")

    # Teste até a folha
    executar_busca(GRAFO, "Brasília", "Florianópolis", "Caminho até Florianópolis")

    # Isolamento da folha
    rede_isolada = bloquear_conexao(GRAFO, "Curitiba", "Florianópolis")
    executar_busca(rede_isolada, "Brasília", "Florianópolis",
                   "Bloqueio Curitiba ↔ Florianópolis (isola a folha)")

    # ---------- Modo interativo ----------
    print("\n" + "=" * 60)
    print("  MODO INTERATIVO")
    print("=" * 60)
    print("Vértices disponíveis:", ", ".join(sorted(GRAFO.keys())))
    print("(Digite 'sair' a qualquer momento para encerrar)\n")

    while True:
        origem = input("Origem: ").strip()
        if origem.lower() == "sair":
            break
        if not validar_vertice(GRAFO, origem):
            print(f"  [ERRO] Vértice '{origem}' não existe no grafo.\n")
            continue

        destino = input("Destino: ").strip()
        if destino.lower() == "sair":
            break
        if not validar_vertice(GRAFO, destino):
            print(f"  [ERRO] Vértice '{destino}' não existe no grafo.\n")
            continue

        if origem == destino:
            print("  Origem e destino são iguais. Caminho trivial.\n")
            continue

        executar_busca(GRAFO, origem, destino, "Rede completa (interativo)")

        resp = input("\nDeseja simular um bloqueio de conexão? (s/n): ").strip().lower()
        if resp == "s":
            a = input("  Primeira cidade da aresta: ").strip()
            b = input("  Segunda cidade da aresta: ").strip()
            if a in GRAFO and b in GRAFO:
                rede_temp = bloquear_conexao(GRAFO, a, b)
                executar_busca(rede_temp, origem, destino, f"Bloqueio temporário: {a} ↔ {b}")
            else:
                print("  Cidades inválidas para bloqueio.")

        print()

    print("\nPrograma encerrado.")


if __name__ == "__main__":
    main()
