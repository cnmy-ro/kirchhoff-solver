# Basic loop finding code taken from -- https://stackoverflow.com/questions/12367801/finding-all-cycles-in-undirected-graphs
# EDIT:  This will NOT work.


# graph = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [0, 5], [1, 5], [3, 5]]
graph = [ [0, 1], [1, 2], [0, 2], [0, 2]]  # Can't handle this input
cycles = []

def main():
    global graph
    global cycles
    for edge in graph:
        for node in edge:
            find_new_cycles([node])
    for cy in cycles:
        path = [str(node) for node in cy]
        s = ",".join(path)
        print(s)

def find_new_cycles(path):
    start_node = path[0]
    next_node= None
    sub = []

    global graph
    global cycles

    # Visit each edge and each node of that edge
    for edge in graph:

        node1, node2 = edge

        if start_node in edge:

                if node1 == start_node:
                    next_node = node2

                else:
                    next_node = node1

                if not visited(next_node, path):
                        # Neighbor node not on path yet
                        sub = [next_node]
                        sub.extend(path)
                        # Explore extended path
                        find_new_cycles(sub);

                elif len(path) > 2  and next_node == path[-1]:
                        # Cycle found
                        p = rotate_to_smallest(path);
                        inv = get_reverse(p)
                        if is_new(p) and is_new(inv):
                            cycles.append(p)

def get_reverse(path):
    return rotate_to_smallest(path[::-1])

def rotate_to_smallest(path):
    """ Rotate cycle path such that it begins with the smallest node """
    n = path.index(min(path))
    return path[n:] + path[:n]

def is_new(path):
    return not path in cycles

def visited(node, path):
    return node in path

main()
