#  BFS 
import collections
def bfs(graph,root):
    visited,queue=set(),collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                
graph = {0:[1,2],1:[0,3,4],2:[0,5],3:[1,4],4:[1,3],5:[2]}
bfs(graph,5)
