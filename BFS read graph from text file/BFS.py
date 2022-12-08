import ast  # Abstract Syntax Tree

file = open('graph.txt', 'r')   # function returns a file object
data = file.read()  # reads at most size bytes from the file
graph = ast.literal_eval(data)  # safely evaluate strings containing
file.close()    # file cannot be read or written any more
visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def BFS(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("Breadth-First Search Read From File Text :")
BFS(visited, graph, 'A')