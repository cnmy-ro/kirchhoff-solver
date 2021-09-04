
class Resistor:
    def __init__(self, name, node_1, node_2, value):
        self.name = name
        self.node_1 = node_1
        self.node_2 = node_2
        self.value = value
    def __str__(self):
        return f"{self.name} -- {self.node_1} {self.node_2} -- {self.value}"
    def get_edge(self):
        return (self.node_1, self.node_2)

class VoltageSource:
    def __init__(self, name, node_1, node_2, source_type, value):
        self.name = name
        self.node_1 = node_1
        self.node_2 = node_2
        self.source_type = source_type
        self.value = value
    def __str__(self):
        return f"{self.name} -- {self.node_1} {self.node_2} -- {self.source_type} -- {self.value}"
    def get_edge(self):
        return (self.node_1, self.node_2)

class EdgeCurrent:
    def __init__(self, name, src_node, dst_node, component, value):
        self.name = name
        self.src_node = src_node
        self.dst_node = dst_node
        self.associated_component = component  # Of type `Resistor` or `VoltageSource`
        self.value = value
    def __str__(self):
        return f"{self.name} -- {self.src_node} {self.dst_node} -- {self.component.name} -- {self.value}"



def initialize_currents(voltage_sources, resistors):

    currents = {}

    for component in {**voltage_sources, **resistors}.values():
        src_node, dst_node = component.get_edge()
        current_name = f"I_{component.name}_{src_node}{dst_node}"
        currents[current_name] = EdgeCurrent(current_name, src_node, dst_node, component, value=None)

    return currents


def get_components_and_nodes(netlist):

    voltage_sources = {}
    resistors = {}
    currents = {}
    nodes = []

    for line in netlist:
        tokens = line.split(' ')

        if ENDLIST_TOKEN in tokens:
            break

        component_name = tokens[0]
        component_node_1 = tokens[1]
        component_node_2 = tokens[2]

        if 'v' in component_name:
            source_type = tokens[3]
            voltage_value = int(tokens[4])
            voltage_sources[component_name] = VoltageSource(component_name, component_node_1, component_node_2, source_type, voltage_value)

        elif 'r' in component_name:
            resistance_value = int(tokens[3])
            resistors[component_name] = Resistor(component_name, component_node_1, component_node_2, resistance_value)

        nodes.extend([component_node_1, component_node_2])

    nodes = sorted(list(set(nodes)))
    return voltage_sources, resistors, nodes