Disclaimer from the real living breathing human behind this: I designed this project myself and wrote an extensive outline prior to writing any code or using any AI tools. I then fed the design outline through ChatGPT (4o) to generate design docs and READMEs since it can write a lot better and faster than I do. Github Copilot was used as a helper while writing the code, but most of it was still written by my fingers on a keyboard. (Although I let Github Copilot completely write all commit messages by itself. Who among us is any good at writing commit messages, anyway?)

# Challenged Network Simulation
This repository contains a simulation for challenged networks with intermittent connectivity and resource-constrained nodes, inspired by research into delay-tolerant and distributed computing.

## Features
- Dockerized network nodes with Python MPI communication.
- Dynamic simulation of node connectivity, reliability, and queuing delays.
- Modular design for easy extension and testing.

## Documentation
See the [Design Document](docs/Challenged_Network_Simulation_Design.md) for details on the system architecture and roadmap.

## Getting Started

```
docker build
```

```
docker-compose up
```