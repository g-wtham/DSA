def bfs_using_stack(graph, start_node):
    stack_in = []
    stack_out = []
    
    visited = set()
    
    stack_in.append(start_node)
    
    while stack_in or stack_out:
        if not stack_out:
            while stack_in:
                stack_out.append(stack_in.pop())
                
        current = stack_out.pop()
        
        if current not in visited:
            print(current)
            visited.add(current)
            
        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                stack_in.append(neighbour)
            
            
graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': ['F'],
'F': []
}

bfs_using_stack(graph, 'A')