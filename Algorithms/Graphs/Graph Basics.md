---
tags: [algorithms, graphs, data-structures]
---

# Graph Basics

## Definition
A graph $G = (V, E)$ models relationships between objects.

- **Vertex set** $V = \{v_1, v_2, ..., v_n\}$ represents the objects
- **Edge set** $E$ between vertices (e.g., $\{u, v\}$) represents relationships

## Real-World Examples

### Family Trees
- Vertices: People
- Edges: Parentage relationships

### Road Networks
- Vertices: Places/intersections
- Edges: Roads connecting them

### Subway Maps
- Vertices: Stations/stops
- Edges: When you can get from stop A to stop B directly

### Internet Routing
- Vertices: Routers or network devices (phones, computers, servers)
- Edges: If two devices are directly connected

### Recommendation Engines
- Vertices: Things being recommended (websites, movies/shows, videos, books)
- Edges: $\{A, B\}$ if B is recommended to those who used A

### Disease Spread
- Vertices: People (infected or not infected)
- Edges: Shows "infector" - $A \to B$ means A infected B

### Compiling Code
- Vertices: Code blocks (functions, for loops, different files, other graphs)
- Edges: Execution order among code blocks

### Folder Structure
- Directories: Files

### Code Dependencies
- Library depends on another library

## Related Topics
- [[Graph Types]]
- [[Graph Terminology]]
- [[Graph Representations]]
