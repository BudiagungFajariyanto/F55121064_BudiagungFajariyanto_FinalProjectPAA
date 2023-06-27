import networkx as nx
import time

# Inisialisasi graf
G = nx.Graph()

# Tambahkan edge dan bobotnya ke graf
G.add_edge('a', 'b', weight=12)
G.add_edge('a', 'c', weight=10)
G.add_edge('a', 'g', weight=12)
G.add_edge('b', 'a', weight=12)
G.add_edge('b', 'c', weight=8)
G.add_edge('b', 'd', weight=12)
G.add_edge('c', 'a', weight=10)
G.add_edge('c', 'b', weight=8)
G.add_edge('c', 'd', weight=11)
G.add_edge('c', 'e', weight=3)
G.add_edge('c', 'g', weight=9)
G.add_edge('d', 'c', weight=11)
G.add_edge('d', 'e', weight=11)
G.add_edge('d', 'f', weight=10)
G.add_edge('e', 'c', weight=3)
G.add_edge('e', 'd', weight=11)
G.add_edge('e', 'f', weight=6)
G.add_edge('e', 'g', weight=7)
G.add_edge('f', 'd', weight=10)
G.add_edge('f', 'e', weight=6)
G.add_edge('f', 'g', weight=9)
G.add_edge('g', 'a', weight=12)
G.add_edge('g', 'c', weight=9)
G.add_edge('g', 'e', weight=7)
G.add_edge('g', 'f', weight=9)


def tsp(graph):
    start_time = time.time()
    time.sleep(0.1)
    path = nx.approximation.traveling_salesman_problem(graph)

    total_weight = 0
    for i in range(len(path) - 1):
        source = path[i]
        target = path[i + 1]
        weight = graph[source][target]['weight']
        total_weight += weight
        print("Pergi dari", source, "ke", target, "dengan bobot", weight)

    end_time = time.time()

    print("Hasil TSP:")
    print("Rute:", " -> ".join(path))
    print("Total Bobot:", total_weight)
    print("Waktu komputasi:", "{:.6f}".format(end_time - start_time), "detik")


def dijkstra(graph, start_node, target_node):
    start_time = time.time()
    time.sleep(0.1)
    path = nx.shortest_path(graph, start_node, target_node)

    total_weight = 0
    for i in range(len(path) - 1):
        source = path[i]
        target = path[i + 1]
        weight = graph[source][target]['weight']
        total_weight += weight
        print("Pergi dari", source, "ke", target, "dengan bobot", weight)

    end_time = time.time()

    print("Hasil Dijkstra:")
    print("Rute:", " -> ".join(path))
    print("Total Bobot:", total_weight)
    print("Waktu komputasi:", "{:.6f}".format(end_time - start_time), "detik")


def main():
    print("Pilihan Algoritma:")
    print("1. TSP (Traveling Salesman Problem)")
    print("2. Dijkstra")
    choice = input("Pilih Algoritma (1/2): ")
    if choice.lower() == "1":
        tsp(G)
    elif choice.lower() == "2":
        start_node = input("Masukkan node awal: ")
        target_node = input("Masukkan node tujuan: ")
        dijkstra(G, start_node, target_node)
    else:
        print("Pilihan tidak valid.")


if __name__ == '__main__':
    main()
