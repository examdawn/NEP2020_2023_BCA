---
order: 5
title: OSC - Unit 4 Solved
exclude: true
---

> [!WARNING]
> This Page is incomplete and answers will be added soon. 4/7 Remaining.

# Operating System Concepts - Unit 4 Solved

## Q1. Give a brief overview on static, dynamic linking and dynamic loading in the context of memory management
TODO

## Q2. Explain the functions of Memory Management along with Hardware, Address Spaces
- ***Functions of Memory Management***
    - **Allocation & Deallocation**:  
        - Allocates memory to processes when requested (`malloc()`, `new`).  
   - Releases memory after process completion (`free()`, garbage collection).  
    - **Protection & Sharing**:  
        - Prevents unauthorized access using **base-limit registers** (MMU).  
   - Allows shared memory (e.g., IPC, libraries like `glibc`).  
    - **Virtualization & Swapping**:  
        - Extends RAM via disk (**paging**, **swap space**).  
   - Uses **demand paging** (load pages only when needed).  
    - **Fragmentation Handling**:  
        - Solves **external fragmentation** (compaction, paging).  
   - Minimizes **internal fragmentation** (best-fit allocation).  

-  ***Hardware & Address Spaces***:   
    - **Key Hardware**:  
      - **CPU + MMU**: Translates **logical → physical addresses** (TLB cache).  
      - **Registers**: MAR (address), MBR (data), base-limit (protection).  
    - **Logical vs. Physical Address**:  
      - **Logical (Virtual)**: Process-generated (e.g., `0x00400000`).  
      - **Physical**: Actual RAM location (handled by **MMU**).  
    - **Memory Hierarchy**:  
      - **Cache → RAM → Disk** (swapping for virtual memory).  
    - **Address Binding**:  
      - **Compile-time** (static), **Load-time** (relocatable), **Runtime** (MMU).  

- **Example**:  
`Paging divides processes into fixed-size pages (e.g., 4KB) mapped to RAM frames, avoiding external fragmentation.`

## Q3. Explain Shared Pages, Swap and Zram <!--(f--k the syllabus, we ball here)-->
TODO

## Q4. Explain Memory Partition Schemes.
Memory partition schemes are methods used to allocate memory to processes in a computer system. The two common approaches are the **Fixed Size Partition Scheme** and the **Variable Size Partition Scheme**. Each scheme has its own advantages and disadvantages, impacting how efficiently memory is utilized.
#### 1. ***Fixed Size Partition Scheme***:  
In the **Fixed Size Partition Scheme**, memory is divided into fixed-sized partitions, and each process is assigned one partition, regardless of its size. All partitions are of equal size.
- **How It Works**:
    - The system divides the available memory into several partitions of the same size.
    - Each partition is assigned to a process. If a process is smaller than the partition, the remaining space in the partition is wasted (this is called **internal fragmentation**).
    - If a process is larger than a partition, it cannot fit into the fixed-size block, and either the process is not allocated memory, or the system must implement a solution to handle such large processes.
- **Advantages**:
    - **Simplicity**: Easy to implement as memory management is straightforward.
    - **Fast Allocation**: Allocation is quick because the system simply assigns the next available partition.
    - **Low Overhead**: No need for complex data structures to manage memory allocation.
- **Disadvantages**:
    - **Internal Fragmentation**: Processes that do not use the full partition cause wasted space.
    - **Inefficient Memory Usage**: If processes are much smaller than the partition size, a lot of memory goes unused.
    - **Limited Flexibility**: Fixed partition sizes may not match the needs of dynamically changing processes.
- **Example**:  
`Imagine a system with 1GB of RAM divided into 4 fixed-size partitions, each of 250MB. If a process needs 150MB, it will be allocated one partition, leaving 100MB unused. If a process needs 300MB, it will not fit into any partition.`

#### 2. ***Variable Size Partition Scheme***:  
In the **Variable Size Partition Scheme**, memory is divided into partitions of different sizes depending on the size of the process requesting memory. This scheme allocates exactly as much memory as needed for each process.
- **How It Works**:
    - The system dynamically divides memory into partitions that can vary in size based on the needs of the processes.
    - When a process is loaded into memory, the system allocates a partition large enough to accommodate the process.
    - If a process is smaller than the partition, there may be internal fragmentation, but this is generally less of an issue than in fixed-size partitions.
- **Advantages**:
    - **No Wasted Space**: Memory is allocated in the exact amount needed, so there is no wasted space within the partition.
    - **Efficient Memory Usage**: Makes better use of available memory compared to fixed-size partitioning.
    - **Flexibility**: More flexible as memory allocation is based on actual process needs.
- **Disadvantages**:
    - **External Fragmentation**: Over time, as processes are loaded and unloaded, free memory gets scattered in small blocks. This makes it hard to allocate large contiguous blocks of memory.
    - **Complex Management**: The system needs to track variable-sized partitions and handle fragmentation efficiently.
    - **Slower Allocation**: Allocating memory may be slower because the system must search for the best fit for the process.
- **Example**:   
`A system with 1GB of RAM may allocate a 300MB partition to one process, a 500MB partition to another, and a 200MB partition to a third. In this case, the allocation is based on the actual process size, so no memory is wasted within each partition.`
## Q5. Explain First-Fit, Best-Fit and Worst-Fit Memory Allocation Strategies with advantages and disadvantages 
TODO

## Q6. Explanation Fragmentation, Segmentation and Paging (quick advantages vs disadvantages too pliz)
TODO

## Q7. Explain Frame Allocation
Frame allocation refers to the process of assigning physical memory frames (blocks of memory in RAM) to processes that are running in an operating system. Since physical memory is limited, frame allocation determines how memory is divided and assigned to different processes, which is critical for efficient system performance and memory utilization.  

In virtual memory systems, a process does not directly access physical memory but instead uses pages of data. These pages are mapped to physical frames in RAM. The operating system manages the allocation of these frames to processes. 

Example of Frame Allocation:
Imagine a system with 100 frames of physical memory and 4 processes. The operating system needs to
decide how to allocate these frames to the processes. Here are a few methods of allocation:
- Fixed Frame Allocation:
    - The operating system assigns a fixed number of frames to each process.
    - Example: If the system has 100 frames and 4 processes, the OS may allocate 25 frames to each process.
        - Process 1: 25 frames
        - Process 2: 25 frames
        - Process 3: 25 frames
        - Process 4: 25 frames
- Dynamic Frame Allocation:
    - The number of frames allocated to each process can change dynamically based on the process's needs.
    - Example: If Process 1 starts with 20 frames but later needs more memory, it might be
allocated 30 frames, while Process 2 might be reduced from 30 to 20 frames.
- Proportional Allocation:
    - Frames are allocated based on the size or priority of each process.
    - Example: The system may allocate frames proportional to the process size. If Process 1 is larger and needs more memory, it might get 60 frames, while Process 2 gets 40 frames.
<!--
Walk a homie through Page Replacement, why it is needed and its algorithms(FIFO, LIFO, LRU) with neat hood-ready diagrams
-->