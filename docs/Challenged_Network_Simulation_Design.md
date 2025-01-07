
# Challenged Network Simulation Design Document

## **1. Project Overview**
The Challenged Network Simulation models a network of intermittently connected, resource-constrained nodes. Using Docker containers to represent network nodes and Python MPI for communication, this project aims to simulate real-world challenged networks as described in the accompanying research paper. The system is designed to evolve into a robust framework capable of testing distributed computing in extreme networking environments.

---

## **2. Objectives**
1. Simulate a network of nodes with:
   - Intermittent and unpredictable connections.
   - Node-level failures and recoveries.
   - Variable connection speeds and latencies.
2. Provide a modular framework for:
   - Sending messages between nodes (initially "hello, world").
   - Supporting JSON/YAML and larger scientific data formats (e.g., FASTA).
   - Handling distributed computing tasks in future iterations.
3. Visualize the network state in a programmer-friendly way.
4. Incorporate core concepts from the research paper:
   - Weighted Temporal Graphs.
   - Group Formation & Leader Election.

---

## **3. System Architecture**
### **3.1. Core Components**
1. **Nodes:**
   - Docker containers running Python scripts to simulate individual network nodes.
   - Each node includes MPI-based communication, queuing logic, and failure simulation.

2. **Orchestrator:**
   - Centralized controller ("god mode") to manage:
     - Node connections and disconnections.
     - Network latencies and interruptions.
     - Node crashes and recoveries.
   - Configurable via a YAML file for extensibility.

3. **Visualization Tool:**
   - Text-based table displaying:
     - Node statuses (e.g., online, offline, recovering).
     - Connection statuses and attributes (e.g., latency, reliability).
     - Data propagation logs.

4. **Weighted Temporal Graph Engine:**
   - Manages node and edge attributes:
     - Node reliability, queuing delay.
     - Connection bandwidth, latency, and reliability.
   - Built using Python’s NetworkX library.

5. **Group Formation & Leader Election Manager:**
   - Dynamically clusters nodes into groups based on connectivity and reliability.
   - Elects group leaders using predefined criteria (e.g., trustworthiness, resources).

---

### **3.2. Workflow**
1. **Startup:**
   - Orchestrator initializes nodes based on configuration.
   - Nodes establish MPI communication channels.
   - Initial Weighted Temporal Graph created.

2. **Dynamic Behavior:**
   - Orchestrator periodically:
     - Modifies connection statuses.
     - Adjusts node attributes (e.g., queue delays, reliability).
     - Simulates crashes and recoveries.
   - Group Formation & Leader Election Manager updates groups and leaders as conditions change.

3. **Data Exchange:**
   - Nodes exchange simple messages ("hello, world") initially.
   - Future iterations to include structured data and distributed task execution.

4. **Visualization & Logging:**
   - Real-time text-based display of network state.
   - Logs generated for post-simulation analysis.

---

## **4. Repository Structure**
```
challenged-network-sim/
├── docker/
│   ├── Dockerfile         # Base image for nodes
│   ├── docker-compose.yml # Orchestrates the simulation
│   └── network_config/    # Configuration files (e.g., connection algorithms)
├── scripts/
│   ├── orchestrator.py    # Controls node behavior, connections, and interruptions
│   ├── node_script.py     # Handles communication and basic processing for each node
│   ├── visualization.py   # Text-based visualization tool
│   └── utils.py           # Shared utility functions
├── tests/
│   ├── test_orchestrator.py
│   ├── test_node_script.py
│   └── test_network_dynamics.py
├── docs/
│   ├── README.md          # Main documentation
│   ├── architecture.md    # Detailed project architecture and design
│   ├── configuration.md   # Explanation of config files and parameters
│   └── future_work.md     # Notes on scalability and potential features
└── .gitignore
```

---

## **5. Key Features**
### **5.1. Initial Features**
- Simulate intermittent connections and node failures.
- Visualize node and connection states in real time.
- Weighted Temporal Graphs capturing:
  - Node reliability and queuing delays.
  - Connection bandwidth, latency, and reliability.
- Group Formation & Leader Election for dynamic clustering.

### **5.2. Future Features**
- Support for structured data (JSON, YAML) and large scientific files (FASTA).
- Distributed task execution.
- Advanced network dynamics (e.g., Gaussian/random walk models).
- HPC and cloud compatibility.

---

## **6. Configuration Example**
```yaml
network_dynamics:
  algorithm: "uniform_random"
  parameters:
    update_interval: 5  # seconds
node_settings:
  default_reliability: 0.9
  default_latency: [50, 2000]  # ms
visualization:
  refresh_interval: 2  # seconds
```

---

## **7. Development Roadmap**
1. **Phase 1: Core System**
   - Build orchestrator, node scripts, and basic visualization.
   - Implement "hello, world" communication.

2. **Phase 2: Graph Integration**
   - Add Weighted Temporal Graph logic.
   - Incorporate Group Formation & Leader Election.

3. **Phase 3: Data Handling**
   - Enable structured data exchange (JSON, YAML).
   - Test with scientific data formats.

4. **Phase 4: Distributed Computing**
   - Introduce task splitting, scheduling, and execution.
   - Optimize for HPC environments.

5. **Phase 5: Advanced Features**
   - Expand network dynamics models.
   - Add detailed fault tolerance and recovery mechanisms.

---

## **8. Summary**
This project lays the foundation for simulating and analyzing challenged networks in controlled environments. With its modular architecture and focus on extensibility, it will evolve into a versatile tool for studying distributed computing in extreme conditions.

---

Let’s get started!
