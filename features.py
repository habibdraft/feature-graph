def expand_features(graph, operators):
    new_graph = dict(graph)
    
    for name, node in graph.items():
        if node['level'] != 0:
            continue
    
        for op_name, op_func in operators.items():
            new_name = f'{op_name}_{name}'
            
            new_graph['new_name'] = {
                'level': 1,
                'op': op_name,
                'parents': [name],
                'tensor': op_func(node['tensor'])
            }
            
    return new_graph
