from mpi4py import MPI
import time
import random

class Orchestrator:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.connectivity = {i: [] for i in range(1, num_nodes)}  # Connectivity map

    def randomize_connectivity(self):
        """Randomly define which nodes can communicate."""
        for node in range(1, self.num_nodes):
            self.connectivity[node] = random.sample(
                [i for i in range(1, self.num_nodes) if i != node],
                random.randint(0, self.num_nodes - 2)
            )
        print("Updated Connectivity Map:", self.connectivity)

    def enforce_connectivity(self):
        """Broadcast connectivity map to all nodes."""
        for node in range(1, self.num_nodes):
            if node < size:  # Ensure we only send to valid ranks
                comm.send(self.connectivity[node], dest=node)

    def start(self):
        print(f"Orchestrator started with {self.num_nodes - 1} worker nodes.")
        while True:
            print("Randomizing connectivity...")
            self.randomize_connectivity()
            print("Broadcasting connectivity map...")
            self.enforce_connectivity()
            print("Connectivity map broadcast complete. Sleeping...")
            time.sleep(5)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        orchestrator = Orchestrator(num_nodes=size)
        orchestrator.start()
    else:
        print(f"Node {rank} started and waiting for messages...")
        while True:
            try:
                allowed_connections = comm.recv(source=0)  # Get connectivity map
                print(f"Node {rank} allowed to communicate with: {allowed_connections}")
            except:
                pass
