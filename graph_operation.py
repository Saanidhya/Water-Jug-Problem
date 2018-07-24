'''
Provides basic operations on the graph
Operation
 - BFS
 - BFS - Path
 - DFS
 - DFS - Path
'''

def bfs(graph, start, visited=list(), bfs=list()):
    queue = list()
    queue.append(start)
    visited.append(start)
    #print(len(list(graph.keys())))
    while queue:
        print("_"*20)
        for x in graph[start]:
            queue.append(x)
            visited.append(x)
        bfs.append(queue[0])
        print(queue)
        del queue[0]
        print(queue)
        print(visited)
        print(bfs)
        if queue:
            print(queue[0])
            start = queue[0]
    
    '''
    print(queue)
    i=0
    while queue[i] not in visited:
        print("index "+str(i))
        visited.append(queue[0])
        bfs.append(queue[0])
        for x in graph[queue[0]]:
            print(queue)
            queue.append(x)
        del queue[i]
        i=i+1
    print(bfs)
    '''




'''def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None'''