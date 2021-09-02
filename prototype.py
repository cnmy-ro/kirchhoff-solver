

def main(netlist_file):

    with open(netlist_file, 'r') as nf:
        netlist = nf.read()

    netlist = netlist.split('\n')
    circuit_name = netlist.pop(0)

    # Identify the components and the nodes
    components, nodes = get_components_and_nodes(netlist)

    print("Circuit name:", circuit_name)
    print("Voltage sources:", components['voltage-sources'])
    print("Resistors:", components['resistors'])
    print("Nodes:", nodes)
    print("---")


    # Using KVL and KCL, calculate the currents.
    # TODO

    # Then calculate the potential diffs for all edges
    # TODO




# -----
# Utils

def get_components_and_nodes(netlist):

    voltage_sources = {}
    resistors = {}
    nodes = []

    for line in netlist:
        component_specs = line.split(' ')

        if ".end" in component_specs:
            break

        component_name = component_specs[0]
        component_node_1 = int(component_specs[1])
        component_node_2 = int(component_specs[2])

        if 'v' in component_name:
            source_type = component_specs[3]
            voltage_value = int(component_specs[4])
            voltage_sources[component_name] = [component_node_1, component_node_2, source_type, voltage_value]

        elif 'r' in component_name:
            resistance_value = int(component_specs[3])
            resistors[component_name] = [component_node_1, component_node_2, resistance_value]

        nodes.extend([component_node_1, component_node_2])

    nodes = sorted(list(set(nodes)))

    components = {'voltage-sources': voltage_sources, 'resistors': resistors}

    return components, nodes




# -------------

if __name__ == '__main__':

    netlist_file = "./netlists/simple_circuit.txt"
    main(netlist_file)