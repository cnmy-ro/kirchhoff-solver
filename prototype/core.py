import numpy as np
import graph_utils


def get_node_current_coeffs(nodes, currents):
    n_currents = len(currents.keys())
    current_coeffs = {}

    # For each node
    for node in nodes:

        current_coeffs[node] = {}

        # Find the incoming and outgoing currents
        for current_name in currents.keys():

            if currents[current_name].dst_node == node:
                # Incoming current
                current_coeffs[node][current_name] = 1

            elif currents[current_name].src_node == node:
                # Outgoing current
                current_coeffs[node][current_name] = -1

    return current_coeffs


def get_loop_current_coeffs(closed_loops, voltage_sources, resistors, currents):
    # Find all loops in the circuit
    closed_loops = _get_all_closed_loops(nodes, voltage_sources, resistors)

    closed_loops = graph_utils.reduce_number_of_loops(closed_loops, n_nodes, n_components)

    # TODO
    # ...

    return loop_current_coeffs


def _get_all_closed_loops(nodes, voltage_sources, resistors):

    # Some useful info available at -- https://math.stackexchange.com/questions/8140/find-all-cycles-faces-in-a-graph
    undirected_edges = []
    for component in {**voltage_sources, resistors}.values():
        undirected_edges.append(set(component.get_edge()))

    # TODO
    # ...

    pass







def solve_for_currents(node_current_coeffs, loop_current_coeffs):
    # Convert the coefficient dicts into a single coefficient matrix
    # TODO
    # ...


    # Solve the matrix form of the equations
    # TODO
    # ...

    pass



def solve_for_potential_diffs(currents, resistors):

    # TODO
    # ...

    return potential_diffs