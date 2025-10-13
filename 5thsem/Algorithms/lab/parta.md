---
order: 1
title: DAA Lab - Part A
---
# Design & Analysis Of Algorithms - Lab Part A

## Q1. write a program to sort a list of N element using selection Sort techique using C.

::: details See code
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

## Q2: Write a program to perform Travelling Salesman Problem

::: details See code
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

## Write program to implement Dynamic programming Algorithm for the 0/1 Knapsack problem.

::: details See code
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

