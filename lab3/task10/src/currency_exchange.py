from utils import read, write
from collections import deque


def currency_exchange(data):
    n, m = data[0]
    edges = data[1:m+1]
    adj_reach = [[] for _ in range(n + 1)]
    for edge in edges:
        u = edge[0]
        v = edge[1]
        adj_reach[u].append(v)

    s = data[-1][0]

    # поиск достижимых вершин
    visited = [False] * (n + 1)
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        u = q.popleft()
        for v in adj_reach[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    # алгоритм Беллмана-Форда
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0

    for i in range(n - 1):
        updated = False
        for (u, v, w) in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # поиск отрицательных циклов
    possible_cycle_nodes = set()
    for (u, v, w) in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            possible_cycle_nodes.add(v)

    # создаем новый список смежности
    adj_cycle = [[] for _ in range(n + 1)]
    for u, v, _ in edges:
        adj_cycle[u].append(v)

    in_cycle = [False] * (n + 1)
    for node in possible_cycle_nodes:
        if not in_cycle[node]:
            q = deque()
            q.append(node)
            in_cycle[node] = True
            while q:
                u = q.popleft()
                for v in adj_cycle[u]:
                    if not in_cycle[v]:
                        in_cycle[v] = True
                        q.append(v)

    # результат
    result = []
    for i in range(1, n + 1):
        if not visited[i]:
            result.append('*')
        elif in_cycle[i]:
            result.append('-')
        else:
            result.append(dist[i] if dist[i] != INF else '*')

    return result


def main():
    data = [list(line) for line in read(type_convert=int)]
    print(data)
    write(end='')
    result = currency_exchange(data)
    for line in result:
        write(line, to_end=True)


if __name__ == "__main__":
    main()
