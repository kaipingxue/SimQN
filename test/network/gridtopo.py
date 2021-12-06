from qns.network.network import QuantumNetwork
from qns.network.topology.gridtopo import GridTopology

topo = GridTopology(nodes_number=9)
net = QuantumNetwork(topo)

print(net.nodes, net.qchannels)
