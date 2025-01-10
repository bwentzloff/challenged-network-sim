from mpi4py import MPI
import time
import random

class Orchestrator:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.connectivity = {i: [] for i in range(1, num_nodes)}  # Connectivity map
        self.comm = MPI.COMM_WORLD

    def randomize_connectivity(self):
        """Randomly define which nodes can communicate."""
        for node in range(1, self.num_nodes):
            # Exclude the current node itself
            possible_connections = [i for i in range(1, self.num_nodes) if i != node]
            
            # Pick a random number of connections (up to the available population)
            num_connections = random.randint(1, len(possible_connections))
            
            # Create the connectivity list
            self.connectivity[node] = random.sample(possible_connections, num_connections)
            
        print(f"Updated Connectivity Map: {self.connectivity}")

    def broadcast_connectivity(self):
        """Send connectivity map to all nodes."""
        for node in range(1, self.num_nodes):
            self.comm.send(self.connectivity[node], dest=node)
            print(f"Sent connectivity map to Node {node}: {self.connectivity[node]}")

    def start(self):
        print(f"Orchestrator started with {self.num_nodes - 1} worker nodes.")
        while True:
            self.randomize_connectivity()
            self.broadcast_connectivity()
            time.sleep(5)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:  # Orchestrator
        orchestrator = Orchestrator(num_nodes=size)
        orchestrator.start()
    else:  # Worker nodes
        print(f"Worker node {rank} initialized and waiting.")
        while True:
            try:
                connectivity = comm.recv(source=0)
                print(f"Node {rank} received connectivity map: {connectivity}")
            except Exception as e:
                print(f"Node {rank} encountered an error: {e}")
                break
