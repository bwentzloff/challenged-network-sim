from mpi4py import MPI
import time

def receive_connectivity():
    """Receive connectivity map from orchestrator."""
    try:
        allowed_nodes = comm.recv(source=0)
        print(f"Node {rank} received connectivity map: {allowed_nodes}", flush=True)
        return allowed_nodes
    except Exception as e:
        print(f"Node {rank} error receiving connectivity: {e}", flush=True)
        return []

def communicate_with_nodes(allowed_nodes):
    """Send messages to connected nodes."""
    print(f"Node {rank} attempting to communicate with: {allowed_nodes}", flush=True)
    for node in allowed_nodes:
        try:
            msg = f"Message from Node {rank} to Node {node}"
            comm.send(msg, dest=node)
            print(f"Node {rank} sent: {msg}", flush=True)
        except Exception as e:
            print(f"Node {rank} failed to communicate with Node {node}: {e}", flush=True)


def listen_for_messages():
    """Listen for incoming messages."""
    print(f"Node {rank} is listening for messages.", flush=True)
    while True:
        try:
            msg = comm.recv()
            print(f"Node {rank} received: {msg}", flush=True)
        except Exception:
            print(f"Node {rank} stopped listening.", flush=True)
            break  # Exit loop when no more messages

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank > 0:  # Worker nodes
        print(f"Worker node {rank} initialized and waiting.", flush=True)
        while True:
            allowed_connections = receive_connectivity()  # Receive map from orchestrator
            communicate_with_nodes(allowed_connections)  # Send messages
            listen_for_messages()  # Receive messages
            time.sleep(5)  # Simulate periodic activity

