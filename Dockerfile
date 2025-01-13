# Base image with Python and MPI
FROM ubuntu:20.04

# Set environment variables to suppress prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages: Python, pip, Open MPI
RUN apt-get update && apt-get install -y \
    python3 python3-pip openmpi-bin libopenmpi-dev openssh-server \
    && apt-get clean

# Install mpi4py
RUN pip3 install mpi4py

# Allow OpenMPI to run as root
ENV OMPI_ALLOW_RUN_AS_ROOT=1
ENV OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

# Configure SSH
RUN mkdir -p /var/run/sshd \
    && echo 'root:root' | chpasswd \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

# Set working directory
WORKDIR /app

# Copy the scripts into the container
COPY scripts/ /app/scripts/
COPY hostfile /app/hostfile

# Start SSH by default
CMD ["/usr/sbin/sshd", "-D"]

# Set default command to avoid accidental container exit
CMD ["sleep", "infinity"]
