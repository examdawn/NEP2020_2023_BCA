---
order: 1
title: DAA Lab Records
---

# Design & Analysis Of Algorithms - Lab Part A

(Important Questions are marked with a *!)

## * Q1. write a program to sort a list of N element using selection Sort techique using C.

::: details See Code {open}
```C
#include <stdio.h>

void main() {
    int arr[100], n, i, j, min, temp;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    for (i = 0; i < n - 1; i++) {
        min = i;
        for (j = i + 1; j < n; j++)
            if (arr[j] < arr[min])
                min = j;
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
    printf("Sorted array: ");
    for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
}
```
:::

::: details Show Output
```
Enter number of elements: 5
Enter 5 elements: 5 2 3 6 1
Sorted array: 1 2 3 5 6 
```
:::

## * Q2: Write a program to perform Travelling Salesman Problem.
::: details See Code {open}
```C
#include <stdio.h>
#include <limits.h>

#define MAX 10

int tsp(int graph[MAX][MAX], int visited[MAX], int pos, int n, int count, int cost, int start, int *minCost) {
    if (count == n && graph[pos][start]) {
        int totalCost = cost + graph[pos][start];
        if (totalCost < *minCost)
            *minCost = totalCost;
        return *minCost;
    }
    for (int i = 0; i < n; i++) {
        if (!visited[i] && graph[pos][i]) {
            visited[i] = 1;
            tsp(graph, visited, i, n, count + 1, cost + graph[pos][i], start,
                minCost);
            visited[i] = 0;
        }
    }
    return *minCost;
}

void main() {
    int graph[MAX][MAX], visited[MAX] = {0};
    int n, minCost = INT_MAX;
    printf("Enter number of cities: ");
    scanf("%d", &n);
    printf("Enter cost matrix (%dx%d):\n", n, n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &graph[i][j]);
    visited[0] = 1;
    tsp(graph, visited, 0, n, 1, 0, 0, &minCost);
    printf("Minimum cost: %d\n", minCost);
}
```
:::

::: details Show Output
```
Enter number of cities: 3
Enter cost matrix (3x3):
0 10 15
10 0 35 
15 35 0 
Minimum cost: 60
```
:::

## * Q3: Write program to implement Dynamic programming Algorithm for the 0/1 Knapsack problem.

::: details See Code {open}
```C
#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapsack(int W, int wt[], int val[], int n) {
    int dp[n + 1][W + 1];
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (wt[i - 1] <= w)
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }
    return dp[n][W];
}

void main()
{
    int n, W;
    int val[100], wt[100];
    printf("Enter number of items: ");
    scanf("%d", &n);
    printf("Enter weights of items: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &wt[i]);
    printf("Enter values of items: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &val[i]);
    printf("Enter capacity of knapsack: ");
    scanf("%d", &W);
    int result = knapsack(W, wt, val, n);
    printf("Maximum value in knapsack: %d\n", result);
}
```
:::

::: details Show Output
```
Enter number of items: 4
Enter weights of items: 2 3 4 5
Enter values of items: 3 4 5 6
Enter capacity of knapsack: 5
Maximum value in knapsack: 7
```
:::


## Q4. Write a program to perform knapsack problem using Greedy solution.

::: details See Code {open}
```C
#include <stdio.h>

void main() {
    int n, W;
    float weight[100], value[100], ratio[100], total = 0;
    printf("Enter number of items: ");
    scanf("%d", &n);
    printf("Enter knapsack capacity: ");
    scanf("%d", &W);
    for (int i = 0; i < n; i++) {
        printf("Enter weight and value of item %d: ", i + 1);
        scanf("%f %f", &weight[i], &value[i]);
        ratio[i] = value[i] / weight[i];
    }
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (ratio[i] < ratio[j]) {
                float tmp;
                tmp = ratio[i];
                ratio[i] = ratio[j];
                ratio[j] = tmp;
                tmp = weight[i];
                weight[i] = weight[j];
                weight[j] = tmp;
                tmp = value[i];
                value[i] = value[j];
                value[j] = tmp;
            }
    for (int i = 0; i < n && W > 0; i++) {
        if (weight[i] <= W) {
            total += value[i];
            W -= weight[i];
        }
        else {
            total += ratio[i] * W;
            break;
        }
    }
    printf("Maximum value: %.2f\n", total);
}
```
:::

::: details Show Output
```
Enter number of items: 3
Enter knapsack capacity: 50
Enter weight and value of item 1: 10 60
Enter weight and value of item 2: 20 120 
Enter weight and value of item 3: 30 60
Maximum value: 220.00
```
:::

## * Q5. Write a program to implement the dfs and bfs algorithm for a graph.

::: details See Code {open}
```C
#include <stdio.h>

#define MAX 100
int adj[MAX][MAX], visited[MAX], n;

void dfs(int v) {
    printf("%d ", v);
    visited[v] = 1;
    for (int i = 0; i < n; i++)
        if (adj[v][i] && !visited[i])
            dfs(i);
}

void bfs(int start) {
    int queue[MAX], front = 0, rear = 0;
    for (int i = 0; i < n; i++)
        visited[i] = 0;
    queue[rear++] = start;
    visited[start] = 1;
    while (front < rear) {
        int v = queue[front++];
        printf("%d ", v);
        for (int i = 0; i < n; i++) {
            if (adj[v][i] && !visited[i]) {
                queue[rear++] = i;
                visited[i] = 1;
            }
        }
    }
}

void main() {
    int edges, u, v, start;
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter number of edges: ");
    scanf("%d", &edges);
    printf("\n");
    for (int i = 0; i < edges; i++) {
        printf("Enter edge (u v): ");
        scanf("%d %d", &u, &v);
        adj[u][v] = 1;
        adj[v][u] = 1;
    }
    printf("Enter starting vertex: ");
    scanf("%d", &start);
    printf("\nDFS traversal: ");
    for (int i = 0; i < n; i++)
        visited[i] = 0;
    dfs(start);
    printf("\nBFS traversal: ");
    bfs(start);
}
```
:::

::: details Show Output
```
Enter number of vertices: 4
Enter number of edges: 3

Enter edge (u v): 0 1
Enter edge (u v): 1 2
Enter edge (u v): 2 3
Enter starting vertex: 0

DFS traversal: 0 1 2 3 
BFS traversal: 0 1 2 3
```
:::

## * Q6. Write a program to find minimum and maximum value in an array using divide and conquer.

::: details See Code {open}
```C
#include <stdio.h>

void findMinMax(int arr[], int low, int high, int *min, int *max) {
    int mid;
    if (low == high) {
        *min = arr[low];
        *max = arr[low];
        return;
    }
    if (high == low + 1) {
        if (arr[low] < arr[high]) {
            *min = arr[low];
            *max = arr[high];
        }
        else {
            *min = arr[high];
            *max = arr[low];
        }
        return;
    }
    mid = (low + high) / 2;
    int min1, max1, min2, max2;
    findMinMax(arr, low, mid, &min1, &max1);
    findMinMax(arr, mid + 1, high, &min2, &max2);
    *min = (min1 < min2) ? min1 : min2;
    *max = (max1 > max2) ? max1 : max2;
}

void main() {
    int arr[100], n, min, max;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter array elements: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    findMinMax(arr, 0, n - 1, &min, &max);
    printf("\nMinimum element: %d\n", min);
    printf("Maximum element: %d\n", max);
}
```
:::

::: details Show Output
```
Enter number of elements: 4
Enter array elements: 4 10 2 5

Minimum element: 2
Maximum element: 10
```
:::

## Q7. Write a simple test program to implement divide and conquer strategy. E.g Quick sort algorithm for sorting list of integers in ascending order.

::: details See Code {open}
```C
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter %d elements: ", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    quickSort(arr, 0, n - 1);
    printf("\nSorted array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
```
:::

::: details Show Output
```
Enter number of elements: 5
Enter 5 elements: 2 6 1 8 3

Sorted array: 1 2 3 6 8 
```
:::

## * Q8: Write a program to implement merge sort algorithm for sorting a list of integers in ascending order.

::: details See Code {open}
```C
#include <stdio.h>

void merge(int arr[], int l, int m, int r) {
    int i = l, j = m + 1, k = 0;
    int temp[r - l + 1];
    while (i <= m && j <= r) {
        if (arr[i] <= arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }
    while (i <= m)
        temp[k++] = arr[i++];
    while (j <= r)
        temp[k++] = arr[j++];
    for (i = l, k = 0; i <= r; i++, k++)
        arr[i] = temp[k];
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

void main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter elements: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    mergeSort(arr, 0, n - 1);
    printf("\nSorted array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
```
:::

::: details Show Output
```
Enter number of elements: 4
Enter elements: 4 2 1 7

Sorted array: 1 2 4 7
```
:::

## Q9: Write a program to display Automated Merge Sort Timing for Multiple Input Sizes.

::: details See Code {open}
```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int arr[], int l, int m, int r) {
	int i = l, j = m + 1, k = 0;
	int *temp = (int *)malloc((r - l + 1) * sizeof(int));
	while (i <= m && j <= r) {
		if (arr[i] <= arr[j]) 
            temp[k++] = arr[i++];
		else 
            temp[k++] = arr[j++];
	}
	while (i <= m) 
        temp[k++] = arr[i++];
	while (j <= r) 
        temp[k++] = arr[j++];
	for (i = l, k = 0; i <= r; i++, k++)
		arr[i] = temp[k];
	free(temp);
}

void mergeSort(int arr[], int l, int r) {
	if (l < r) {
		int m = (l + r) / 2;
		mergeSort(arr, l, m);
		mergeSort(arr, m + 1, r);
		merge(arr, l, m, r);
	}
}

void main() {
	int testSizes[] = {6000, 10000, 20000, 40000, 80000, 160000};
	int numTests = sizeof(testSizes) / sizeof(testSizes[0]);
	printf("n\tTime (seconds)\n");
	printf("--------------------\n");
	for (int t = 0; t < numTests; t++) {
		int n = testSizes[t];
		int *arr = (int *)malloc(n * sizeof(int));
		srand(time(NULL));
		for (int i = 0; i < n; i++) 
			arr[i] = rand();
		clock_t start = clock();
		mergeSort(arr, 0, n - 1);
		clock_t end = clock();
		double timeTaken = ((double)(end - start)) / CLOCKS_PER_SEC;
		printf("%d\t%.5f\n", n, timeTaken);
		free(arr);
	}
}
```
:::

::: details Show Output
```
n       Time (seconds)
--------------------
6000    0.00000
10000   0.00000
20000   0.01500
40000   0.00000
80000   0.01600
160000  0.02000
```
:::

## Q10: Write a program to Sort a given set of n integer elements using Quick Sort method and compute its time complexity.

> [!NOTE]
>  Run the program for varied values of [n > 5000] and record the time taken to sort. 

::: details See Code {open}
```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int partition(int arr[], int low, int high) {
	int pivot = arr[high];
	int i = (low - 1);
	for (int j = low; j < high; j++) {
		if (arr[j] <= pivot) {
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i + 1], &arr[high]);
	return (i + 1);
}

void quickSort(int arr[], int low, int high) {
	if (low < high) {
		int pi = partition(arr, low, high);
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

void generateRandomArray(int arr[], int n) {
	for (int i = 0; i < n; i++) 
		arr[i] = rand() % 100000;
}

void main() {
	int sizes[] = {6000, 10000, 20000, 50000, 100000};
	int num_tests = sizeof(sizes) / sizeof(sizes[0]);
	printf("Quick Sort Time Measurement:\n");
	printf("-----------------------------\n");
	for (int t = 0; t < num_tests; t++) {
		int n = sizes[t];
		int *arr = (int *)malloc(n * sizeof(int));
		if (arr == NULL) {
			printf("Memory allocation failed for size %d\n", n);
			continue;
		}
		generateRandomArray(arr, n);
		clock_t start = clock();
		quickSort(arr, 0, n - 1);
		clock_t end = clock();
		double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
		printf("Size: %6d -> Time taken: %.6f seconds\n", n, time_taken);
		free(arr);
	}
}
```
:::

::: details Show Output
```
Quick Sort Time Measurement:
-----------------------------
Size:   6000 -> Time taken: 0.000000 seconds
Size:  10000 -> Time taken: 0.000000 seconds
Size:  20000 -> Time taken: 0.000000 seconds
Size:  50000 -> Time taken: 0.007000 seconds
Size: 100000 -> Time taken: 0.009000 seconds
```
:::

## * Q11. Write a program that Accepts the Vertices and Edges for a Graph and Stores it as an Adjacency Matrix.

::: details See Code {open}
```C
#include <stdio.h>

void main() {
	int vertices, edges;
	int i, j;
	printf("Enter number of vertices: ");
	scanf("%d", &vertices);
	int adj[vertices][vertices];
	for (i = 0; i < vertices; i++) {
		for (j = 0; j < vertices; j++)
			adj[i][j] = 0;
	}
	printf("Enter number of edges: ");
	scanf("%d", &edges);
	printf("Enter edges [source and destination vertices between 0 and %d]:\n", vertices - 1);
	for (i = 0; i < edges; i++) {
		int u, v;
		printf("Edge %d: ", i + 1);
		scanf("%d %d", &u, &v);
		if (u >= 0 && u < vertices && v >= 0 && v < vertices)
			adj[u][v] = 1;
		else {
			printf("Invalid edge! Vertex out of range.\n");
			i--;
		}
	}
	printf("\nAdjacency Matrix:\n");
	for (i = 0; i < vertices; i++) {
		for (j = 0; j < vertices; j++)
			printf("%d ", adj[i][j]);
		printf("\n");
	}
}
```
:::

::: details Show Output
```
Enter number of vertices: 3
Enter number of edges: 3
Enter edges [source and destination vertices between 0 and 2]:
Edge 1: 1 2
Edge 2: 0 1
Edge 3: 1 1

Adjacency Matrix:
0 1 0
0 1 1
0 0 0
```
:::

## * Q12. Write a program to implement function to print In-Degree, Out-Degree and to Display that Adjacency Matrix.

::: details See Code {open}
```C
#include <stdio.h>

void main() {
	int vertices, edges;
	int i, j;
	printf("Enter number of vertices: ");
	scanf("%d", &vertices);
	int adj[vertices][vertices];
	for (i = 0; i < vertices; i++)
		for (j = 0; j < vertices; j++)
			adj[i][j] = 0;
	printf("Enter number of edges: ");
	scanf("%d", &edges);
	printf("Enter edges [source and destination, 0 to %d):\n", vertices - 1];
	for (i = 0; i < edges; i++) {
		int u, v;
		printf("Edge %d: ", i + 1);
		scanf("%d %d", &u, &v);
		if (u >= 0 && u < vertices && v >= 0 && v < vertices)
			adj[u][v] = 1;
		else {
			printf("Invalid edge! Please enter vertices between 0 and %d.\n", vertices - 1);
			i--;
		}
	}
	printf("\nAdjacency Matrix:\n");
	for (i = 0; i < vertices; i++) {
		for (j = 0; j < vertices; j++)
			printf("%d ", adj[i][j]);
		printf("\n");
	}
	printf("\nVertex\tIn-Degree\tOut-Degree\n");
	for (i = 0; i < vertices; i++) {
		int in = 0, out = 0;
		for (j = 0; j < vertices; j++) {
			if (adj[j][i] == 1)
				in++;
			if (adj[i][j] == 1)
				out++;
		}
		printf("%d\t%d\t\t%d\n", i, in, out);
	}
}
```
:::

::: details Show Output
```
Enter number of vertices: 3
Enter number of edges: 3
Enter edges [source and destination, 0 to 2]:
Edge 1: 1 2
Edge 2: 2 0
Edge 3: 1 0

Adjacency Matrix:
0 0 0
1 0 1
1 0 0

Vertex  In-Degree       Out-Degree
0       2               0
1       0               2
2       1               1
```
:::

## Q13.  Write a program to implement Backtracking Algorithm for Solving problems like N Queens.  

::: details See Code {open}
```C
#include <stdio.h>
#include <stdbool.h>
#define N 4

int board[N];
bool isSafe(int row, int col) {
	for (int i = 0; i < row; i++) {
		if (board[i] == col || board[i] - i == col - row || board[i] + i == col + row)
			return false;
	}
	return true;
}

void printBoard() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (board[i] == j)
				printf("Q ");
			else
				printf(". ");
		}
		printf("\n");
	}
	printf("\n");
}

void solve(int row) {
	if (row == N) {
		printBoard();
		return;
	}

	for (int col = 0; col < N; col++) {
		if (isSafe(row, col)) {
			board[row] = col;
			solve(row + 1);
		}
	}
}

int main() {
	printf("Solutions to %d-Queens Problem:\n\n", N);
	solve(0);
	return 0;
}
```
:::


::: details Show Output
```
Solutions to 4-Queens Problem:

. Q . .
. . . Q
Q . . .
. . Q .

. . Q .
Q . . .
. . . Q
. Q . .
```
:::


## * Q14.  Write a program to implement the Backtracking Algorithm for the Sum of Sub-sets problem. 

::: details See Code {open}
```C
#include <stdio.h>

int set[100], subset[100];
int n, target, found = 0;

void sumOfSubsets(int index, int currentSum, int subsetSize) {
	if (currentSum == target) {
		printf("Subset: ");
		for (int i = 0; i < subsetSize; i++)
			printf("%d ", subset[i]);
		printf("\n");
		found = 1;
		return;
	}
	for (int i = index; i < n; i++) {
		if (currentSum + set[i] <= target) {
			subset[subsetSize] = set[i];
			sumOfSubsets(i + 1, currentSum + set[i], subsetSize + 1);
		}
	}
}

void main() {
	printf("Enter number of elements: ");
	scanf("%d", &n);
	printf("Enter the elements: ");
	for (int i = 0; i < n; i++)
		scanf("%d", &set[i]);
	printf("Enter target sum: ");
	scanf("%d", &target);
	printf("Subsets with sum %d:\n", target);
	sumOfSubsets(0, 0, 0);
	if (!found)
		printf("No subset found.\n");
}
```
:::


::: details Show Output
```
Enter number of elements: 3
Enter the elements: 21 29 12
Enter target sum: 50
Subsets with sum 50:
Subset: 21 29
```

:::

## * Q15. Write program to implement Greedy Algorithm for job sequencing with deadlines.

::: details See Code {open}
```C
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct {
    char id;
    int deadline;
    int profit;
} Job;

int compare(const void *a, const void *b) {
    return ((Job *)b)->profit - ((Job *)a)->profit;
}

int min(int a, int b) {
    return (a < b) ? a : b;
}

void main() {
    int n;
    Job jobs[MAX];
    int slot[MAX] = {0};
    char result[MAX];
    printf("Enter number of jobs: ");
    scanf("%d", &n);
    printf("Enter job id, deadline, and profit:\n");
    for (int i = 0; i < n; i++)
        scanf(" %c %d %d", &jobs[i].id, &jobs[i].deadline, &jobs[i].profit);
    qsort(jobs, n, sizeof(Job), compare);
    int maxDeadline = 0;
    for (int i = 0; i < n; i++)
        if (jobs[i].deadline > maxDeadline)
            maxDeadline = jobs[i].deadline;
    int totalProfit = 0;
    for (int i = 0; i < n; i++)
        for (int j = min(maxDeadline, jobs[i].deadline) - 1; j >= 0; j--)
            if (slot[j] == 0) {
                slot[j] = 1;
                result[j] = jobs[i].id;
                totalProfit += jobs[i].profit;
                break;
            }
    printf("Job sequence: ");
    for (int i = 0; i < maxDeadline; i++)
        if (slot[i])
            printf("%c ", result[i]);
    printf("\nTotal Profit: %d\n", totalProfit);
}
```
:::

::: details Show Output
```
Enter number of jobs: 4
Enter job id, deadline, and profit:
A 2 100
B 1 19
C 3 27
D 1 21
Job sequence: D A C 
Total Profit: 148
```
:::

## * Q16. Write program to implement Dynamic Programming algorithm for the Optimal Binary Search Tree Problem.

::: details See Code {open}
```C
#include <stdio.h>
#include <limits.h>
#define MAX 10

int n;
float p[MAX];
float q[MAX];
float e[MAX + 1][MAX + 1];
float w[MAX + 1][MAX + 1];

void optimalBST() {
    int i, j, l, r;
    for (i = 0; i <= n; i++) {
        e[i][i] = q[i];
        w[i][i] = q[i];
    }
    for (l = 1; l <= n; l++)
        for (i = 0; i <= n - l; i++) {
            j = i + l;
            e[i][j] = INT_MAX;
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j];
            for (r = i + 1; r <= j; r++) {
                float cost = e[i][r - 1] + e[r][j] + w[i][j];
                if (cost < e[i][j])
                    e[i][j] = cost;
            }
        }
    printf("Minimum expected cost of Optimal BST: %.2f\n", e[0][n]);
}
void main() {
    int i;
    printf("Enter number of keys: ");
    scanf("%d", &n);
    printf("Enter successful search probabilities p[1..%d]:\n", n);
    for (i = 0; i < n; i++) {
        printf("p[%d]: ", i + 1);
        scanf("%f", &p[i]);
    }
    printf("Enter unsuccessful search probabilities q[0..%d]:\n", n);
    for (i = 0; i <= n; i++) {
        printf("q[%d]: ", i);
        scanf("%f", &q[i]);
    }
    optimalBST();
}
```
:::

::: details Show Output
```
Enter number of keys: 3
Enter successful search probabilities p[1..3]:
p[1]: 0.2
p[2]: 0.5
p[3]: 0.1
Enter unsuccessful search probabilities q[0..3]:
q[0]: 0.1
q[1]: 0.2
q[2]: 0.3
q[3]: 0.1
Minimum expected cost of Optimal BST: 3.20
```
:::

## * Q17. Write a program that implements Prim’s algorithm to generate Minimum Cost Spanning Tree.

::: details See Code {open}
```C
#include <stdio.h>
#define MAX 10
#define INF 1000000

int n;
int graph[MAX][MAX];
int selected[MAX];

void prim() {
    int i, j, edges = 0;
    int totalCost = 0;
    selected[0] = 1;
    printf("\nEdges in MST:\n");
    while (edges < n - 1) {
        int min = INF;
        int x = -1, y = -1;
        for (i = 0; i < n; i++)
            if (selected[i])
                for (j = 0; j < n; j++)
                    if (!selected[j] && graph[i][j])
                        if (graph[i][j] < min) {
                            min = graph[i][j];
                            x = i;
                            y = j;
                        }
        printf("%d - %d : %d\n", x, y, min);
        totalCost += min;
        selected[y] = 1;
        edges++;
    }
    printf("\nTotal cost of MST: %d\n", totalCost);
}

void main() {
    int i, j;
    printf("Enter number of vertices (max %d): ", MAX);
    scanf("%d", &n);
    printf("Enter adjacency matrix (0 if no edge):\n");
    for (i = 0; i < n; i++) {
        selected[i] = 0;
        for (j = 0; j < n; j++)
            scanf("%d", &graph[i][j]);
    }
    prim();
}
```
:::

::: details Show Output
```
Enter number of vertices (max 10): 4
Enter adjacency matrix (0 if no edge):
0 3 1 0
5 1 2 4
5 2 3 0
9 3 1 0

Edges in MST:
0 - 2 : 1
2 - 1 : 2
1 - 3 : 4

Total cost of MST: 7
```
:::

## * Q18. Write a program that implements Kruskal’s algorithm to generate Minimum Cost Spanning Tree.

::: details See Code {open}
```C
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct {
    int u;
    int v;
    int weight;
} Edge;

int n, e;
Edge edges[MAX];
Edge result[MAX];
int parent[MAX];

int find(int i) {
    while (parent[i] != i)
        i = parent[i];
    return i;
}

void union_set(int u, int v) {
    int set_u = find(u);
    int set_v = find(v);
    parent[set_u] = set_v;
}

int compare(const void *a, const void *b) {
    Edge *edge1 = (Edge *)a;
    Edge *edge2 = (Edge *)b;
    return edge1->weight - edge2->weight;
}

void kruskal() {
    int count = 0;
    int i = 0;
    for (int v = 0; v < n; v++)
        parent[v] = v;
    qsort(edges, e, sizeof(Edge), compare);
    while (count < n - 1 && i < e) {
        Edge current = edges[i++];
        int set_u = find(current.u);
        int set_v = find(current.v);
        if (set_u != set_v) {
            result[count++] = current;
            union_set(set_u, set_v);
        }
    }
    printf("\nEdges in Minimum Spanning Tree:\n");
    int totalCost = 0;
    for (int i = 0; i < count; i++) {
        printf("%d - %d : %d\n", result[i].u, result[i].v, result[i].weight);
        totalCost += result[i].weight;
    }
    printf("\nTotal cost of MST: %d\n", totalCost);
}

void main() {
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter number of edges: ");
    scanf("%d", &e);
    printf("Enter each edge in format: u v weight (vertices numbered 0 to %d)\n", n - 1);
    for (int i = 0; i < e; i++)
        scanf("%d %d %d", &edges[i].u, &edges[i].v, &edges[i].weight);
    kruskal();
}
```
:::

::: details Show Output
```
Enter number of vertices: 4
Enter number of edges: 3
Enter each edge in format: u v weight (vertices numbered 0 to 3)
3 1
0 1
1 1
0 2
2 1

Edges in Minimum Spanning Tree:
3 - 1 : 0
0 - 2 : 2

Total cost of MST: 2
```
:::

> [!IMPORTANT]
> End of Lab Record.