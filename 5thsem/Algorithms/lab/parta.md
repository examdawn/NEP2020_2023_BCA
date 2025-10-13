---
order: 1
title: DAA Lab - Part A
---
# Design & Analysis Of Algorithms - Lab Part A

## Q1. write a program to sort a list of N element using selection Sort techique using C.

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

## Q2: Write a program to perform Travelling Salesman Problem.
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

## Q3: Write program to implement Dynamic programming Algorithm for the 0/1 Knapsack problem.

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

## Q5. Write a program to implement the dfs and bfs algorithm for a graph.

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

## Q6. Write a program to find minimum and maximum value in an array using divide and conquer.

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

## Q8: Write a program to implement merge sort algorithm for sorting a list of integers in ascending order.

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

