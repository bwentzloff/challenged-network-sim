from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def receive_connectivity():
    """Receive connectivity map from orchestrator."""
    try:
        allowed_nodes = comm.recv(source=0)
        print(f"Node {rank} allowed to communicate with: {allowed_nodes}")
        return allowed_nodes
    except Exception as e:
        print(f"Node {rank} error receiving connectivity: {e}")
        return []

def communicate_with_nodes(allowed_nodes):
    """Simulate communication with other nodes."""
    for node in allowed_nodes:
        try:
            comm.send(f"Message from Node {rank}", dest=node)
            print(f"Node {rank} sent message to Node {node}")
        except Exception as e:
            print(f"Node {rank} failed to communicate with Node {node}: {e}")

def listen_for_messages():
    """Listen for incoming messages."""
    while True:
        try:
            msg = comm.recv()
            print(f"Node {rank} received: {msg}")
        except:
            break

if rank > 0:
    print(f"Node {rank} started.")
    while True:
        allowed_nodes = receive_connectivity()
        communicate_with_nodes(allowed_nodes)
        listen_for_messages()
        time.sleep(5)
