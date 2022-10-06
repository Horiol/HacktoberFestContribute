#!/usr/bin/python3

"""
Python implementation for Depth First Search algorithm
"""


dummy_graph = {
	'A': {'C', 'E'},
	'B': {'C', 'E', 'G'},
	'C': {'D', 'F', 'G'},
	'D': {'H'},
	'E': {'A', 'B', 'C'},
	'F': {'D', 'I'},
	'G': {'A'},
	'H': set([]),
	'I': {'B', 'C'},
}

def dfs(graph, node, visited_nodes):
	if node not in visited_nodes:
		visited_nodes.append(node)
		for n in graph[node]:
			dfs(graph, n, visited_nodes)
	return visited_nodes


def main():
	first_node = list(dummy_graph.keys())[0]
	dfs_sequence = dfs(dummy_graph, first_node, [])
	print(dfs_sequence)

if __name__ == '__main__':
	main()
	
