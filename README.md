# PDSA - Problem-Solving and Data Structures & Algorithms

This workspace contains Python programs for common data structures and algorithms. Each file now includes simple, beginner-friendly explanations so the logic is easier to understand.

## What was updated

- Added clear explanations at the top of each script.
- Added inline comments to explain the main steps.
- Fixed a small syntax issue in the counting sort example.
- Added comprehensive documentation for all stack operations in `stack.py`.

## Repository overview

### Sorting algorithms
- [insertion_sort.py](insertion_sort.py): Implements insertion sort by inserting each element into its correct place.
- [merge_sort.py](merge_sort.py): Implements merge sort using divide-and-conquer.
- [selection_sort.py](selection_sort.py): Implements selection sort by repeatedly picking the smallest value.

### Data structures
- [linkedlist.py](linkedlist.py): Shows a simple linked list with append and delete operations.
- [stack.py](stack.py): Implements a stack using a Python list with clear documentation for all operations.
- [stacklinkedlist.py](stacklinkedlist.py): A linked-list-based stack file for future implementation.

### Graph and path problems
- [find_if_path_exista_in_graph.py](find_if_path_exista_in_graph.py): Checks whether a path exists between two nodes using BFS.
- [numberofprovinces.py](numberofprovinces.py): Counts connected provinces/cities using DFS.
- [week4grap1.py](week4grap1.py): Finds the shortest connection level between two people in a graph using BFS.
- [week4grap3.py](week4grap3.py): Finds the longest route in a directed graph using topological traversal.
- [week5_grap1.py](week5_grap1.py): Finds the minimum spanning tree (MST) using Kruskal's algorithm.

### Practice and assignment problems
- [w1_grpa1.py](w1_grpa1.py): Finds the minimum difference when choosing P elements using a sliding window approach.
- [w1_grpa3.py](w1_grpa3.py): Detects the data type that appears only once in a mixed list.
- [w1_ppa2.py](w1_ppa2.py): Validates and classifies triangles, including area calculation using Heron's formula.
- [w2_grpa1.py](w2_grpa1.py): Sorts strings in two different ways (by first letter, and by letter/number combination).
- [w2_grpa2.py](w2_grpa2.py): Finds the largest element in a rotated sorted array using binary search.
- [w2_grpa3.py](w2_grpa3.py): Merges two sorted arrays in place while maintaining sorted order.
- [w2_ppa1.py](w2_ppa1.py): Performs binary search and counts the number of comparisons made.
- [w2_ppa2.py](w2_ppa2.py): Implements counting sort for values in a small range [0, r).
- [week3_grap2.py](week3_grap2.py): Evaluates arithmetic expressions in postfix form (Reverse Polish Notation) using a stack.
- [week3_ppa1.py](week3_ppa1.py): Sorts dish IDs by frequency (descending) and value (ascending).
- [week5_live_coding_p1](week5_live_coding_p1): Finds the minimum spanning tree (MST) using Prim's algorithm with a min-heap.
- [week5grpa2.py](week5grpa2.py): Finds the shortest path with minimum cost using Dijkstra's algorithm.
- [week5grpa3.py](week5grpa3.py): Detects negative weight cycles in a graph using the Bellman-Ford algorithm.

## How to run the files

Run any Python file directly from the workspace folder:

```bash
python insertion_sort.py
python merge_sort.py
python selection_sort.py
python linkedlist.py
python stack.py
python find_if_path_exista_in_graph.py
python numberofprovinces.py
python w1_grpa1.py
python w2_grpa1.py
python week3_grap2.py
python week5_live_coding_p1
python week5_grap1.py
python week5grpa2.py
python week5grpa3.py
```

## Key concepts covered

- Sorting algorithms: insertion sort, merge sort, selection sort
- Data structures: linked list, stack
- Graph search: BFS and DFS
- Searching: binary search
- Problem-solving patterns: sliding window, counting sort, topological-style traversal
- Minimum Spanning Tree: Prim's and Kruskal's algorithms using a min-heap
- Shortest path: Dijkstra's algorithm
- Negative cycle detection: Bellman-Ford algorithm

## Notes

The code is written for learning purposes and is intended to be easy to read, understand, and modify.
