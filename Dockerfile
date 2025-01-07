# Base image with Python and MPI
FROM ubuntu:20.04

# Set environment variables to suppress prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages: Python, pip, Open MPI
RUN apt-get update && apt-get install -y \
    python3 python3-pip openmpi-bin libopenmpi-dev \
    && apt-get clean

# Install mpi4py
RUN pip3 install mpi4py

# Set working directory
WORKDIR /app

# Copy the scripts into the container
COPY scripts/ /app/scripts/

# Set default command
CMD ["mpiexec", "-n", "5", "python3", "/app/scripts/orchestrator.py"]
