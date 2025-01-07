from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def send_message(dest, msg):
    comm.send(msg, dest=dest)

def receive_message():
    msg = comm.recv()
    print(f"Node {rank} received: {msg}")

if rank == 0:
    print("Orchestrator should control communication. Node script ready.")
else:
    while True:
        time.sleep(2)  # Wait for orchestrator to allow communication
        try:
            receive_message()
        except:
            pass  # No message received, likely due to disconnection
