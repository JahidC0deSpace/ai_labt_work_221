## Overview
The **IDDFS Maze Solver** is a Python program that uses the **Iterative Deepening Depth-First Search (IDDFS)** algorithm to find a path in a grid-based maze. It explores the maze depth by depth until it reaches the target position.

## Features
- Uses **IDDFS** for pathfinding
- Handles different maze sizes
- Detects walls and prevents invalid moves
- Displays the path if a solution is found
- Provides detailed traversal order

## How It Works
1. The user inputs the maze dimensions.
2. The user provides the maze grid (0 = open path, 1 = wall).
3. The user specifies the start and target coordinates.
4. The program runs IDDFS to search for a path.
5. If a path is found, the traversal order is displayed; otherwise, it notifies that no path exists.

## Input Example
```
Enter the number of rows and columns (space separated):
5 5

Enter the maze (0 for empty, 1 for wall):
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
1 1 0 1 0
0 0 0 0 0

Enter start coordinates (space separated):
0 0

Enter target coordinates (space separated):
4 4
```

## Output Example
```
Path found at depth 6 using IDDFS
Traversal Order: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
```

