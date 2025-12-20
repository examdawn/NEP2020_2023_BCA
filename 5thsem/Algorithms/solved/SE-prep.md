---
order: 1
title: Algorithms Semester Exam Prep Questions
exclude: true
---

# Section A: 2 Marks Answer Questions

## Q1. What is an Algorithm? 
An algorithm is a finite set of clear, step‑by‑step instructions to solve a specific, well‑defined problem. It must have inputs, produce at least one output, be unambiguous, effective, and terminate after a finite number of steps.

## Q2. What are Order of Growth? Give one example for each.
Order of growth describes how an algorithm’s running time or space requirement increases as the input size n grows.  
- Common orders with examples:  
  - Constant: O(1), e.g., accessing an array element by index. 
  - Linear: O(n), e.g., linear search.
  - Quadratic: O(n²), e.g., bubble sort in the worst case. 
  - Logarithmic: O(log n), e.g., binary search.

## Q3. Define Input Size. Why is it important in algorithm analysis?
Input size is a measure of how much data an algorithm receives, typically the number of items nn (e.g., array length, number of vertices/edges). It is important because time and space complexities are expressed as functions of input size, allowing comparison of algorithm efficiency independent of hardware.

## Q4. Explain Prims Algorithm.
Prim’s algorithm finds a minimum spanning tree (MST) of a connected, weighted, undirected graph. It starts from any vertex, repeatedly adds the minimum‑weight edge that connects a new vertex to the growing tree until all vertices are included.

## Q5. Define Brute Force approach.
Brute force (exhaustive search) systematically enumerates and evaluates all possible candidate solutions to a problem. It guarantees finding an optimal solution, but is often impractical due to exponential time for large inputs.

## Q6. What is Sequential/Linear Search?
Linear search scans elements of a list sequentially from start to end to find a target value. It compares each element with the key and either returns its position when found or reports failure after the last element; its time complexity is O(n²).

## Q7. What is insertion sort?
Insertion sort builds a sorted list one element at a time by inserting each new element into its correct position among already sorted elements. It has O(n²) time in worst and average cases and O(n) in best case, with O(1) extra space.

## Q8. Give two applications of Depth First Search (DFS).
1. Detecting cycles and finding connected components in graphs.   
2. Topological sorting of directed acyclic graphs (DAGs) and solving maze/path existence problems. 

## Q9. Define P and NP Problems.
***P*** Problem : Decision problems solvable in polynomial time by a deterministic Turing machine. 
***NP*** Problem : Decision problems whose proposed solutions can be verified in polynomial time by a deterministic Turing machine. 

# Section B: 5 Marks Answer Questions

## Q1. Explain the fundamentals of algorithmic problem solving with an example.
Key fundamentals:  
- Problem specification: Clearly define input, output, and constraints.
- Model and abstraction: Represent the problem using appropriate data structures (graphs, arrays, etc.). 
- Algorithm design technique: Choose a strategy like divide-and-conquer, greedy, dynamic programming, brute force.
- Correctness: Prove that the algorithm always produces the required output. 
- Complexity analysis: Derive time and space complexity as functions of input size.

Example (maximum in an array):  
- Input: Array of (n) numbers; Output: largest element.  
- Algorithm: Initialize max with first element; scan the array and update max when a larger element is found; complexity O(n) time, (O(1) space

## Q2. Explain the working of Selection Sort and Bubble Sort with an example.
### Selection Sort

- Repeatedly selects the smallest remaining element and swaps it with the element at the current position. 
- Example: [29, 10, 14, 37]  
  - Pass 1: smallest is 10 → [10, 29, 14, 37]  
  - Pass 2: smallest in remaining is 14 → [10, 14, 29, 37]  
  - Pass 3: remaining already sorted.  
- Time O(n²), space O(1).

### Bubble Sort

- Repeatedly compares adjacent elements and swaps them if out of order, bubbling larger elements towards the end. 
- Example: [29, 10, 14, 37]  
  - Pass 1: (29,10)→[10,29,14,37], (29,14)→[10,14,29,37], (29,37) no swap.  
  - Further passes confirm sorted order.  
- Worst/average time O(n²), best case O(n); space O(1).

## Q3. Discuss the Exhaustive search technique. Explain the Traveling Salesman Problem (TSP) using exhaustive search.

Exhaustive search generates all possible solutions, tests each against constraints, and selects the best according to an objective (e.g., minimum cost). It is simple and guarantees optimality but often has exponential complexity, suitable only for small instances.

TSP using exhaustive search:  
- Given cities and distances, find the shortest tour visiting each city exactly once and returning to the start.
- Exhaustive search enumerates all permutations of cities (tours), computes distance of each feasible tour, discards invalid ones, and chooses the minimum-length tour; complexity O(n!).

## Q4. Explain Binary Search algorithm and give its best, average and worst case time complexities.
- Binary search works on a sorted array. It compares the key with the middle element, and recursively or iteratively searches either left or right half.
- Algorithm:  
  - low = 0, high = n−1.  
  - While low ≤ high:  
    - mid = ⌊(low + high)/2⌋.  
    - If key == a[mid], return mid; else if key < a[mid], high = mid−1; else low = mid+1.

Time complexities:  
- Best case: O(1) (key found at middle).
- Average case: O(log n).
- Worst case: O(log n).

## Q5. Write a short note on:
- Decision Trees
- Lower-Bound Arguments

### Decision Trees

- A decision tree models the sequence of comparisons made by a comparison-based algorithm; each internal node is a comparison and each leaf is an outcome. For sorting **n** distinct elements, any comparison sort corresponds to a binary decision tree with at least ***n!*** leaves.

### Lower-Bound Arguments

- A lower bound is a proven limit showing that no algorithm in a given model can solve a problem faster than a certain complexity. Using decision trees, any comparison-based sorting algorithm must perform at least Ω(n log n) comparisons in the worst case.

# Section C: 10 Marks Answer Questions

## Q1. Explain Asymptotic Notations O-notation, Ω-notation and Θ-notation with appropriate graphs and examples.
### Big O (O-notation)

- Describes an asymptotic upper bound on a function f(n); it gives worst-case growth rate.   
- f(n) is O(g(n)) if there exist constants c>0, n₀ such that f(n) <= c * g(n) for all n >= n₀.  
- Example: 3n² + 2n + 5 is O(n²); graphically, the curve stays below a constant multiple of n² for large n.

### Big Omega (Ω-notation)

- Gives an asymptotic lower bound, often used for best-case or guaranteed minimum growth.
- f(n) is Ω(g(n) if there exist c>0, n₀ such that f(n) >= c * g(n) for all n >= n₀.
- Example: 3n² + 2n + 5 is Ω(n²); its graph lies above some multiple of n² beyond n₀.

### Theta (Θ-notation)

- Gives a tight bound, both upper and lower; describes exact asymptotic growth.
- f(n) is (Theta) θ(g(n)) if it is both (Big O) O(g(n)) and (Omega) Ω(g(n)).  
- Example: 3n² + 2n + 5 is (Theta) θ(n²); graphically, it is sandwiched between two constants times n² for large n.

## Q2. Explain Merge Sort using the Divide and Conquer technique. Provide a step-by-step trace for a example and discuss its space and time complexity. 
- Merge sort uses **divide and conquer**:  
  - Divide: Split array into two halves.  
  - Conquer: Recursively sort each half.  
  - Combine: Merge two sorted halves into one sorted array.  

Example trace for [38, 27, 43, 3, 9, 82, 10]:  
- Split: [38, 27, 43, 3] and [9, 82, 10].  
- Left:  
  - [38, 27, 43, 3] → [38, 27] and [43, 3].  
  - [38, 27] → [38], [27] → merge → [27, 38].  
  - [43, 3] → [43], [3] → merge → [3, 43].  
  - Merge [27, 38] and [3, 43] → [3, 27, 38, 43]. 
- Right:  
  - [9, 82, 10] → [9] and [82, 10].  
  - [82, 10] → [82], [10] → merge → [10, 82].  
  - Merge [9] and [10, 82] → [9, 10, 82].
- Final merge: [3, 27, 38, 43] and [9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]. 

Complexity:  
- Time: Each level costs O(n), and there are O(log n) levels, so total is (Theta) θ(n log n) for all cases.
- Space: Requires extra O(n) auxiliary space for merging.

## Q3. Explain NP-Complete problems. Discuss their characteristics and explain why they pose challenges for numerical algorithms.
- NP-Complete problems are problems that are both in NP and NP-hard.  
- A decision problem is NP-Complete if:  
  - It is in NP (solutions can be verified in polynomial time).  
  - Every problem in NP can be polynomial-time reduced to it.

Characteristics and challenges:  
- Examples: SAT, 3-SAT, Hamiltonian cycle, CLIQUE, decision versions of TSP and Knapsack.  
- No polynomial-time algorithms are known; if any NP-Complete problem has a polynomial-time solution, then P = NP.  
- For numerical algorithms, these problems involve combinatorial explosion (e.g., exponentially many subsets/permutations), making exact algorithms infeasible for large inputs and forcing reliance on approximation or heuristics.

## Q4. Consider the following problem with following input. Solve the problem using Exhaustive Search technique. Enumerate all possiblities and indicate unfeasible solutions and optimal solution. Knapsack Capacity W = 15Kg.

| Item | Weight (Kg) | Value (Rs) |
|------|-------------|------------|
|  A   |      3      |    36      |
|  B   |      5      |    25      |
|  C   |      4      |    41      |
|  D   |      6      |    34      |


Capacity W = 15. Consider all subsets (0/1 knapsack).

All subsets:

| Subset | Items   | Total Weight | Total Value | Feasible? |
|--------|---------|--------------|-------------|----------|
| 1      | ∅      | 0            | 0           | Yes      |
| 2      | A       | 3            | 36          | Yes      |
| 3      | B       | 5            | 25          | Yes      |
| 4      | C       | 4            | 41          | Yes      |
| 5      | D       | 6            | 34          | Yes      |
| 6      | A,B     | 8            | 61          | Yes      |
| 7      | A,C     | 7            | 77          | Yes      |
| 8      | A,D     | 9            | 70          | Yes      |
| 9      | B,C     | 9            | 66          | Yes      |
| 10     | B,D     | 11           | 59          | Yes      |
| 11     | C,D     | 10           | 75          | Yes      |
| 12     | A,B,C   | 12           | 102         | Yes      |
| 13     | A,B,D   | 14           | 95          | Yes      |
| 14     | A,C,D   | 13           | 111         | Yes      |
| 15     | B,C,D   | 15           | 100         | Yes      |
| 16     | A,B,C,D | 18           | 136         | No       | 

- Only {A,B,C,D} is unfeasible (weight 18 > 15).  
- Among feasible subsets, {A,C,D} has maximum value 111 and total weight 13 ≤ 15, so it is the optimal solution under exhaustive search. 