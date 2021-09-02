
def collapse_ideal_wires(nodes, edges, resistances):

    # Collapse zero-resistance edges
    for i, r in enumerate(resistances):

        if r == 0:
            node_1, node_2 = edges[i]
            nodes[nodes.index(node_1)] = node_2
            edges[i] = node_2 + node_2

            for j, e in enumerate(edges):
                if node_1 in e:
                    edges[j] = e.replace(node_1, node_2)

    # Remove redundant nodes and clean up the unnecessary edges
    nodes = sorted(list(set(nodes)))
    for i, e in enumerate(edges):
        if e[0] == e[1]:
            edges.pop(i)
            resistances.pop(i)

    return nodes, edges, resistances