#  Maze Generator & Solver :-

A terminal-based Python program that **Generates and Solves mazes** using **Depth-First Search (DFS)** and **recursive backtracking**, 
built from scratch — as part of the **MainFlow Python Internship Task 2**.
**No external libraries used. 100% pure Python. No matplotlib. No pygame. No shortcuts.**


## Overview :-
This project demonstrates:
- Maze generation via **Recursive backtracking**
- Maze solving using **Depth-First Search (DFS)**
- Simple and clear **terminal-based visualization**
- **No third-party dependencies** — only core Python is used


## Features :-

-  Fully random maze generation
-  Terminal-based display using ASCII characters
-  DFS pathfinding with backtracking
-  Adjustable maze size (rows x columns)
-  Clear code structure & comments


##  Maze Characters :-

| Symbol | Meaning         |
|--------|------------------|
| `#`    | Wall             |
| `' '`  | Empty Path       |
| `S`    | Start Point      |
| `E`    | End Point        |
| `.`    | Visited Path     |


##  How It Works :-

1. **Maze Initialization**: Grid filled with walls (`#`)
2. **Path Carving**: Starts at `(1,1)` and carves paths recursively using random directions
3. **Start (`S`) and End (`E`)** positions are marked
4. **Maze Solving**: DFS explores all possible paths to find a solution, marking visited cells
5. **Final Output**: Maze is printed again, now showing the path taken



