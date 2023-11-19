# USA-Map-Navigation-using-Advanced-Algorithms

## Overview
This project, under the guidance of Prof. Garg, was aimed at implementing and evaluating four search algorithms (UCS, BFS, DFS, and A-Star Search) using Python. The objective was to find paths between any two locations on a USA map, leveraging these algorithms for efficient route finding.

## Methodology
The project methodology involved:
1. **Algorithm Implementation:** Developing four distinct search algorithms in Python based on pseudocodes.
2. **Script Development:** Creating the `find_path.py` script for processing command line arguments and input data from text files describing city paths.
3. **Data Processing:** Utilizing `input_file.txt` to describe paths between different cities and calculating the distance and route.

## How to Run
After cloning this repository, you should run as follows:

find_path.py [ucs/bfs/dfs/astar] [input_file.txt] [point_of_origin] [point_of_destination] [heuristic_file.txt]*

- **[ucs/bfs/dfs/astar]:** Choose the algorithm that you want to run (required)
- **[input_file.txt]:** Provide the path to the input file (required)
- **[point_of_origin]:** Provide the point of origin (required)
- **[point_of_destination]:** Provide the point of destination (required)
- **[heuristic_file.txt]:** Provide the heuristic file if applicable (A-Star) (optional)

Sample command that you can run with the existing input and heuristic files:
- find_path.py ucs input_file1.txt Columbia WashingtonDC
- find_path.py ucs input_file1.txt Boise Nashville
- find_path.py astar input_file1.txt Columbia Frankfort heuristic_Frankfort.txt
