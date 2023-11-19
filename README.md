# USA-Map-Navigation-using-Advanced-Algorithms

## Overview
This project, under the guidance of Prof. Garg, was aimed at implementing and evaluating four search algorithms (UCS, BFS, DFS, and A-Star Search) using Python. The objective was to find paths between any two locations on a USA map, leveraging these algorithms for efficient route finding.

## Methodology
The project methodology involved:
1. **Algorithm Implementation:** Developing four distinct search algorithms in Python based on pseudocodes.
2. **Script Development:** Creating the `find_path.py` script for processing command line arguments and input data from text files describing city paths.
3. **Data Processing:** Utilizing `input_file.txt` to describe paths between different cities and calculating the distance and route.

## Evaluation
The project evaluation focused on:
- **Accuracy and Efficiency:** Ensuring the search algorithms correctly determine the distance and list all locations on the path between two points.
- **Algorithm Performance:** Analyzing each algorithm's performance in terms of speed and resource efficiency.
- **Heuristic Optimization in A-Star Search:** Implementing heuristic optimization for the A-Star search algorithm to reduce node expansions.

## Key Findings
- Successful implementation and validation of UCS, BFS, DFS, and A-Star search algorithms for the USA road map.
- Demonstrated efficiency in pathfinding, with accurate distance calculation and route listing.
- Effective use of heuristic data in A-Star search to optimize the search process.

## Personal Contributions
- **Implementation of Search Algorithms:** Developed four search algorithms (UCS, BFS, DFS, and A-Star Search) in Python to find paths between any two locations on the USA map.
- **Programming and Script Development:** Created the `find_path.py` script capable of taking command line arguments for different search strategies and processing input data from `input_file.txt`.
- **Output Functionality:** Ensured the implementation outputs the total distance and a list of all locations on the path between the specified points of origin and destination.
- **Testing and Validation:** Conducted rigorous testing of the implemented algorithms, ensuring accurate outputs.
- **Heuristic Analysis for A-Star Search:** Incorporated a heuristic file (`heuristic_Frankfort.txt`) in the A-Star search algorithm to optimize the search process.

## How to Run
After clloning this repository, you should run as follows:

find_path.py [ucs/bfs/dfs/astar] [input_file.txt] [point_of_origin] [point_of_destination] [heuristic_file.txt]*

- **[ucs/bfs/dfs/astar]:** Choose the algorithm that you want to run (required)
- **[input_file.txt]:** Provide the path to the input file (required)
- **[point_of_origin]:** Provide the point of origin (required)
- **[point_of_destination]:** Provide the point of destination (required)
- **[heuristic_file.txt]:** Provide the heuristic file if available (optional)

Sample command that you can run with the existing input and heuristic files:
- find_path.py ucs input_file1.txt Columbia WashingtonDC
- find_path.py ucs input_file1.txt Boise Nashville
- find_path.py astar input_file1.txt Columbia Frankfort heuristic_Frankfort.txt
