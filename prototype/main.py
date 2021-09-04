import numpy as np

import component_utils
import core


# ---------
# Constants

ENDLIST_TOKEN = '.end'


# ----
# Main

def main(netlist_file):

    with open(netlist_file, 'r') as nf:
        netlist = nf.read()

    print("Circuit specs:")
    print(netlist)
    print("\n---\n")

    netlist = netlist.split('\n')
    circuit_name = netlist.pop(0)

    # Identify the components and the nodes
    voltage_sources, resistors, nodes = component_utils.get_components_and_nodes(netlist)


    # ---
    # Associate a current with each edge
    currents = component_utils.initialize_currents(voltage_sources, resistors)

    # Apply KCL at each node and get the current coefficients
    node_current_coeffs = core.get_node_current_coeffs(nodes, currents)


    # ---
    # Apply KVL for each loop and get the current coefficients
    loop_current_coeffs = core.get_loop_current_coeffs(nodes, closed_loops, voltage_sources, resistors, currents)


    # ---
    # Solve the equations to obtain the currents
    currents = core.solve_for_currents(node_current_coeffs, loop_current_coeffs)

    # Then calculate the potential diffs for all resistors
    potential_diffs = core.solve_for_potential_diffs(currents, resistors)


    # ---
    print("Solution:")
    print("...")


# ---
# Run
if __name__ == '__main__':

    netlist_file = "../netlists/circuit_1.txt"
    main(netlist_file)