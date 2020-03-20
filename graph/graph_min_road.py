from collections import deque

n = 15
m = 16

graph = {i:set() for i in range(n)}
s = ((0,1),(0,12),(0,11),(0,10),(1,6),(1,7),(3,11),(4,10),(5,8),(5,13),(6,10),(7,13),(8,12),(9,11),(11,12),(11,14),(2,6))
for k in s:
    v1, v2 = k[0], k[1]
    graph[v1].add(v2)
    graph[v2].add(v1)

distances = [None]*n
start_vertex = 0
distances[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v]+1
            queue.append(neigh_v)
for k in range(len(distances)):
    print('самый короткий путь от начало до элемента '+str(k)+' состоит из '+str(distances[k])+' ребер')

