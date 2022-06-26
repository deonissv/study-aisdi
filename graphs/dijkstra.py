from collections import deque


def dijkstra(graph, start, end):
    queue = deque()
    width = len(graph)
    length = len(graph[0])
    visited = []
    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    distances = {}
    for i in range(width):
        for j in range(length):
            distances.update({(i, j): float('Inf')})
    distances[start] = 0

    queue.append((0, start))

    while queue:
        curr = queue.pop()
        dist, pos = curr
        for i in adj:
            x = pos[0] + i[0]
            y = pos[1] + i[1]
            if x >= width or x < 0 or y >= length or y < 0:
                continue
            new_dist = dist + graph[x][y]
            if new_dist < distances[(x, y)]:
                distances[(x, y)] = new_dist
                queue.append((new_dist, (x, y)))
                visited.append((x, y))

    path = deque()
    path.append(end)
    curr = end
    dist = distances[end]
    while curr != start:
        for i in adj:
            x = curr[0] + i[0]
            y = curr[1] + i[1]
            if x >= width or x < 0 or y >= length or y < 0:
                continue
            if distances[(x, y)] == dist - graph[curr[0]][curr[1]]:
                dist = distances[(x, y)]
                path.appendleft((x, y))
                curr = (x, y)
                break
    return path
