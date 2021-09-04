import numpy as np


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
    closed_loops = get_all_closed_loops(nodes, voltage_sources, resistors)

    # TODO

    return loop_current_coeffs




def solve_for_currents(node_current_coeffs, loop_current_coeffs):
    # Convert the coefficient dicts into a single coefficient matrix
    # TODO

    # Solve the matrix form of the equations
    # TODO
    pass



def solve_for_potential_diffs(currents, resistors):

    # TODO

    return potential_diffs


def _get_all_closed_loops(nodes, voltage_sources, resistors):
    undirected_edges = []
    for component in {**voltage_sources, resistors}.values():
        undirected_edges.append(set(component.get_edge()))

    # TODO

    pass



class ClosedLoop:
    def __init__(self, name, node_list, component_list):
        self.name = name
        self.node_list = node_list             # Ex: ['0, '1', '2', '0']
        self.component_list = component_list   # Ex: [v_object, r_object, r_object]
    def __str__(self):
        component_names = [component.name for component in self.component_list]
        return f"{self.name} -- {component_names}"