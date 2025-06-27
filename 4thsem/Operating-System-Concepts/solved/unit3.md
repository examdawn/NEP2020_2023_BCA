---
order: 4
title: OSC - Unit 3 Solved
---

# Operating System Concepts - Unit 3 Solved


## Q1. What are the types of Processes? How are they related to Race Conditions?
Processes in an operating system are broadly classified into two types: `independent processes` and `cooperating processes`

### Independent Processes
- Independent processes operate in isolation, meaning their execution does not affect or get affected by other processes in the system
- They do not share data or resources with others, so there is no need for synchronization between them

### Co-operating Processes
- In contrast, cooperating processes can influence and be influenced by other processes
- They often share data or resources and require communication mechanisms like interprocess communication (IPC) to coordinate their activities effectively
- They can cause race conditions if not co-ordinated correctly

[Linkedin Pulse](https://www.linkedin.com/pulse/understanding-types-processes-operating-systems-paolo-gomez-bvylc/)


## Q2. What is a mutex, and a semaphore? Explain the types of Semaphores

Semaphores are used to implement `critical sections`, which are regions of code that must be executed by only one process at a time
- By using semaphores, processes can coordinate access to shared resources, such as shared memory or I/O devices.

Semaphores use a counter to control access, allowing synchronization for multiple instances of a resource

The process of using Semaphores provides two operations:
- wait (P): The wait operation decrements the value of the semaphore
- signal (V): The signal operation increments the value of the semaphore.


### Types of Semaphores
- Binary Semaphore: 
    - This is also known as a mutex lock, as they are locks that provide mutual exclusion 
    - It can have only two values - 0 and 1 - Its value is initialized to 1
    - It is used to implement the solution of critical section problems with multiple processes and a single resource.
- Counting Semaphore: 
    - Counting semaphores can be used to control access to a given resource consisting of a finite number of instances
    - The semaphore is initialized to the number of resources available
    - Its value can range over an unrestricted domain

[GeeksForGeeks](https://www.geeksforgeeks.org/operating-systems/semaphores-in-process-synchronization/)



## Q3. How is the kernel responsible for managing race conditions?
The kernel, as the core of an operating system, is fundamentally responsible for managing race conditions to ensure system stability and data integrity
- Modern kernels are inherently concurrent environments, meaning multiple threads of execution can be active within the kernel simultaneously
- This concurrency arises from several sources like Interrupt Handlers, Symmetric Multiprocessing(SMP), etc, making race condition management a critical task.


[people.cs.pitt.edu](https://people.cs.pitt.edu/~ouyang/20150225-kernel-concurreny.html)


## Q4. What is the critical section problem? How to solve it?
### Critical Section Problem
The critical section problem is a fundamental challenge in concurrent programming that involves designing a protocol to ensure that when one process is executing in its critical section, no other process is allowed to do so
- A critical section is a segment of code where a process accesses shared resources, such as common variables, data structures, or files
- This prevents data inconsistencies that can arise when multiple processes or threads access and manipulate shared resources simultaneously.
- When multiple processes attempt to modify these shared resources concurrently without proper coordination, it can lead to a race condition, an undesirable situation where the system's output depends on the unpredictable sequence or timing of operations

### Requirements for a Solution

Any valid solution to the critical section problem must satisfy three essential requirements:
- Mutual Exclusion: This is the core requirement, ensuring that if one process is executing within its critical section, no other process can be executing in its own critical section
    - Any other process that needs to enter must wait until the section is free
- Progress: If no process is currently in a critical section and there are processes wishing to enter, the selection of the next process to enter cannot be postponed indefinitely
    - This ensures the system does not halt when resources are available
- Bounded Waiting: There must be a limit on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted
    - This condition prevents "starvation," where a process could be denied access indefinitely.

### Solutions
- Software-Based Solutions
    - Peterson's Solution: 
        - A classic software-based algorithm that solves the problem for two processes. 
        - It uses two shared variables, a boolean array flag to indicate if a process is ready to enter the critical section, and an integer turn to indicate whose turn it is to enter
- Hardware-Supported Solutions
    - Test-and-Set: 
        - This is an atomic instruction that tests and modifies a memory location in a single step. 
        - It allows a process to check a "lock" variable and set it to "true" without being interrupted, effectively locking the critical section
    - Compare-and-Swap: 
        - This atomic instruction compares the content of a memory location to an expected value and, if they match, modifies the content. 
        - It is another way to implement locks for mutual exclusion
- Operating System and Synchronization Primitives
    - Mutex Locks: 
        - A `mutex` (short for `mutual exclusion`) is a locking mechanism that ensures only one thread can acquire the lock at a time. 
        - A process must `acquire()` the lock before entering a critical section and `release()` it upon exiting
    - Semaphores: 
        - Semaphores are integer variables used to control access to shared resources. 
        - They are manipulated using two atomic operations: `wait()` (which decrements the semaphore value, potentially blocking the process if the value becomes negative) and `signal()` (which increments the value, potentially unblocking a waiting process)
        - A mutex is often considered a binary semaphore.
[Dev.to](https://dev.to/harshm03/critical-section-problem-process-synchronization-310d)

## Q5. What is the Producer/Consumer problem? How to solve it with semaphores?
### Producer/Consumer Problem

The Producer-Consumer problem is a classic synchronization issue in operating systems. 
- It involves two types of processes: `producers`, which generate data, and `consumers`, which process that data. 
- Both share a common buffer. The challenge is to ensure that the producer doesn't add data to a full buffer and the consumer doesn't remove data from an empty buffer while avoiding conflicts when accessing the buffer. 


### Problem Statement
- We have a buffer of fixed size. A producer can produce an item and can place it in the buffer. 
- A consumer can pick items and consume them. We need to ensure that when a producer is placing an item in the buffer, then at the same time consumer should not consume any item. 
- In this problem, the buffer is the critical section. 

### Solution for Producer
To solve this problem, we need two counting semaphores - `Full` and `Empty`. "Full" keeps track of some items in the buffer at any given time and "Empty" keeps track of many unoccupied slots. 

```
mutex = 1 
Full = 0 // Initially, all slots are empty. Thus full slots are 0 
Empty = n // All slots are empty initially 
```

```pseudocode
do{

//produce an item

wait(empty);
wait(mutex);

//place in buffer

signal(mutex);
signal(full);

}
while(true)
```
When producer produces an item then the value of "empty" is reduced by 1 because one slot will be filled now. The value of mutex is also reduced to prevent consumer to access the buffer. Now, the producer has placed the item and thus the value of "full" is increased by 1. The value of mutex is also increased by 1 because the task of producer has been completed and consumer can access the buffer. 
### Solution for Consumer

```pseudocode
do{

wait(full);
wait(mutex);

// consume item from buffer

signal(mutex);
signal(empty);


}while(true)
```

As the consumer is removing an item from buffer, therefore the value of "full" is reduced by 1 and the value is mutex is also reduced so that the producer cannot access the buffer at this moment. 

Now, the consumer has consumed the item, thus increasing the value of "empty" by 1. The value of mutex is also increased so that producer can access the buffer now. 

[GeeksForGeeks](https://www.geeksforgeeks.org/operating-systems/producer-consumer-problem-using-semaphores-set-1/)


## Q6. Explain the difference between a pre-emptive and non-pre-emptive kernel



| Aspect                         | Preemptive Kernel                                                                 | Non-Preemptive Kernel                                                      |
|-------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Definition**                | Allows a process running in kernel mode to be interrupted and replaced by another process | Does not allow a process running in kernel mode to be interrupted; runs until it exits kernel mode, blocks, or yields CPU |
| **Process Scheduling**        | Scheduler can forcibly preempt a running process to allocate CPU to higher priority tasks | A running process keeps the CPU until it voluntarily releases it or blocks |
| **Responsiveness**            | More responsive; suitable for real-time systems where deadlines are critical      | Less responsive; may cause delays if a process runs for a long time without yielding |
| **Complexity**                | More complex to design due to need for fine-grained locking and handling race conditions | Simpler to design; fewer race conditions on kernel data as only one process runs in kernel at a time |
| **Race Condition Risk**       | Higher risk of race conditions in kernel data structures; requires careful synchronization | Lower risk of race conditions since kernel code is not preempted mid-execution |
| **Use Cases**                 | Used in modern OS kernels that require multitasking and real-time capabilities (e.g., Linux 2.6+, Solaris) | Used in traditional UNIX, Windows 2000, early Linux kernels                |
| **Overhead**                  | Higher overhead due to frequent context switches and synchronization mechanisms   | Lower overhead as context switches happen less frequently and cooperatively |
| **Handling Interrupts**       | Can interrupt kernel mode processes on timer or higher priority task readiness   | Kernel mode process runs to completion or voluntary yield before switching |


[Tutorialspoint](https://www.tutorialspoint.com/preemptive-and-non-preemptive-kernel)


## Q7. Give an overview on resource allocation graph
The resource allocation graph is a visual depiction of a system’s current status. The resource allocation graph, as its name implies, contains all the information about all of the activities that are holding or waiting for resources.

It also provides information on all instances of all resources, whether available or in use by processes. The process is represented by a circle in the Resource Allocation Graph, whereas the resource is represented using a rectangle. Let’s take a closer look at the various types of vertices and edges.

![Vertices and Edges Demo RAG](https://cdn1.byjus.com/wp-content/uploads/2022/08/resource-allocation-graph-in-operating-system.png)

[Byjus](https://byjus.com/gate/resource-allocation-graph-in-operating-system-notes/)


## Q8. Explain Deadlock, Conditions Required for a Deadlock and Deadlock Recovery

### Deadlock

A deadlock is a critical situation in an operating system where two or more processes become blocked indefinitely. 
- This occurs because each process involved is holding onto a resource that another process in the set needs, while simultaneously waiting for a resource held by another process in the same set
- This creates a cycle of dependencies, preventing any of the involved processes from proceeding with their execution
- Deadlocks can lead to system performance degradation, unresponsiveness, and even complete system failure if not handled properly

For instance, consider two processes, `Process 1` and `Process 2`, and two resources, `Resource A` and `Resource B`. If `Process 1` holds `Resource A` and requests `Resource B`, while `Process 2` holds `Resource B` and requests `Resource A`, both processes will be stuck in a deadlock, unable to proceed

### Conditions Required for a Deadlock

For a deadlock to occur, four specific conditions, often referred to as the Coffman conditions, must simultaneously be met:

*   **Mutual Exclusion**: 
    - At least one resource involved must be non-shareable, meaning that only one process can use it at any given time. 
    - If another process requests the same resource, it must wait until the resource is released. For example, a printer can only be used by one process at a time.
*   **Hold and Wait**: 
    - A process is currently holding at least one resource and is simultaneously waiting to acquire additional resources that are being held by other processes. 
    - This means a process does not release its held resources while waiting for new ones.
*   **No Preemption**: 
    - Resources cannot be forcibly taken away from a process that is holding them. 
    - A resource can only be released voluntarily by the process that is holding it, once it has finished using it. 
    - The operating system cannot force a process to give up a resource it holds, even if another process needs it.
*   **Circular Wait**: 
    - A set of processes forms a circular chain where each process in the set is waiting for a resource held by the next process in the chain. 
    - For example, Process A waits for a resource held by Process B, Process B waits for a resource held by Process C, and Process C waits for a resource held by Process A, forming a closed loop.

## Deadlock Recovery

Once a deadlock is detected, recovery techniques are implemented to break the deadlock and restore the system to a functional state. Recovery strategies generally involve either terminating processes or preempting resources.

Common deadlock recovery methods include:

*   **Process Termination**:
    *   **Kill one process**: 
        - One or more processes involved in the deadlock are terminated to release their held resources. 
        - The goal is to choose a process whose termination has the least impact or cost to the system. 
        - After termination, the system checks if the deadlock is resolved; if not, another process may be terminated.
    *   **Kill all processes**: 
        - All processes involved in the deadlock are terminated. 
        - This is often a last resort, applied when it's difficult to determine which specific process to terminate or when immediate recovery is necessary. 
        - However, it can lead to significant system inefficiencies as all processes will need to restart.
*   **Resource Preemption**:
    *   Resources are forcibly taken away from a process that holds them and allocated to a waiting process. 
        - This breaks the "no preemption" condition and helps resolve the circular wait. 
        - This method requires careful consideration to avoid disrupting the executing processes.
*   **Process Rollback**:
    *   A deadlocked process is returned to a previously saved safe state (e.g., via checkpoints) where it did not hold the resources causing the deadlock. 
        - This involves the process releasing all resources acquired after that saved state, which can then be allocated to other waiting processes. 
        - Rollback can be resource-intensive and may not be feasible for all applications.
*   **Wait-Die and Wound-Wait Schemes**:
    *   These are more specific strategies where processes are preempted based on their age. 
        - In the **Wait-Die** scheme, an older process requesting a resource held by a younger process will wait, but a younger process requesting a resource held by an older process will be terminated (die). 
        - In the **Wound-Wait** scheme, an older process requesting a resource held by a younger process will preempt (wound) the younger process, forcing it to release the resource, while a younger process requesting a resource held by an older process will wait.


<!-- Bag of questions



Explain Peterson's Solution, Dining Philosopher's Solution and Banker's Solution

(use semaphores for dining)


-->