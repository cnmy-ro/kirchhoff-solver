

def reduce_number_of_loops(closed_loops, n_nodes, n_components):
    """ Using the Fundamental Theorem of Network Topology,
    find the number of simple independent loops present in the circuit
    and keep only them

    Parameters:
        closed_loops: *All* possible closed loops present in the circuit.

    Returns:
        The minimal number of simplest loops required to form the mesh equations .

    """



    # 1. Sort the loops in ascending order of their node-length
    # 2. Calculate `m = b - n + 1` where `m` is #loops, `b` is #edges (i.e. branches), and `n` is #nodes
    # 3. Keep only the first `m` loops and discard the rest







class ClosedLoop:

    def __init__(self, name, node_list, component_list):
        self.name = name
        self.node_list = node_list             # Ex: ['0, '1', '2', '0']
        self.component_list = component_list   # Ex: [v_object, r_object, r_object]

    def __str__(self):
        component_names = [component.name for component in self.component_list]
        return f"{self.name} -- {component_names}"