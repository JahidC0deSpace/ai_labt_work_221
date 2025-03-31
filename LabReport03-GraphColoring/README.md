# Depth-First Search (DFS) Grid Pathfinding

## Introduction

This program implements a Depth-First Search (DFS) algorithm to find a path between a source and a goal in a randomly generated grid. The grid contains both walkable cells (`.`) and blocked cells (`#`). The DFS algorithm starts at a randomly selected source and explores the grid to find a path to a randomly chosen goal. The program outputs the grid, the source, the goal, the found path, and the topological order of the DFS traversal.

### Features:
- Random grid generation with obstacles.
- Source and goal are randomly placed in empty cells.
- DFS algorithm for pathfinding.
- Output includes the grid with path, source, and goal.
- Topological order of the DFS traversal.

## Example Usage

### Input

The program generates a random grid with dimensions ranging from 4x4 to 7x7, filled with random walkable (`.`) and blocked (`#`) cells. It also randomly selects a source and goal position. No user input is required, as the grid and positions are randomly generated each time the program runs.

### Example Output

```plaintext
Generated Grid:
. . # . # . 
. # . . # . 
. # . # . G 
# . . . . . 
S . # . # . 

Source: (4, 0)
Goal: (2, 5)
DFS Path: [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)]
Topological Order of DFS Traversal: [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (1, 0), (0, 0), (1, 1), (0, 1), (1, 2), (0, 2), (1, 3), (0, 3), (1, 4), (0, 4), (1, 5), (0, 5)]
