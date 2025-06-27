---
order: 3
title: OSC - Unit 2 Solved
exclude: true
---

# Operating System Concepts - Unit 2 Solved

> [!NOTE]
> Algorithm and numericals will be handled in a seperate section, and will be uploaded. [Click here to view.](../CPU-Schedule/index.md)


## Q1. Give an overview on User and Kernel Threads
Multithreading in concurrent programming involves two primary types: 
- user-level threads
- kernel-level threads

User-level threads are managed by thread libraries in user space, while kernel-level threads are managed directly by the operating system kernel

| Aspect                     | User-Level Threads (ULTs)                                        | Kernel-Level Threads (KLTs)                                          |
| :------------------------- | :--------------------------------------------------------------- | :------------------------------------------------------------------- |
| **Management**             | Managed by user-level thread libraries                        | Managed by the operating system kernel                            |
| **Context Switching**      | Lightweight and fast                                          | Involves higher overhead                                          |
| **Parallelism**            | May not fully exploit multicore CPUs                          | Efficiently utilizes multicore processors                         |
| **Synchronization**        | May lack robust kernel-level support                          | Strong support for synchronization mechanisms                     |
| **Resource Management**    | Limited control over system resources                         | Direct access to system resources                                 |
| **Portability**            | More portable across different OS                             | Platform-dependent, less portable                                 |
| **Blocking Operations**    | May cause blocking of the entire process                      | Efficient handling of blocking operations                         |
| **Visibility to OS**       | Independent of kernel, limited visibility                     | Directly interacts with the kernel, full visibility               |
| **Priority Scheduling**    | Limited control over scheduling policies                      | Priority-based scheduling by the kernel                           |
| **Development Complexity** | Simplified, suitable for lightweight apps                     | Requires a deeper understanding of system concepts                |
| **Scalability**            | May face scalability challenges                               | Better scalability with proper kernel support                     |
| **Hardware Access**        | Limited access to low-level operations                        | Direct access to hardware resources                               |
| **Creation Overhead**      | Lower creation overhead                                       | Higher creation overhead (system calls involved)                  |
| **Responsiveness**         | More responsive due to user-space thread switches             | Less responsive due to kernel interaction for management          |
| **Fault Tolerance**        | A bug/crash in one ULT can affect all threads in process      | More isolated; crash in one thread less likely to affect others   |


![user level threads and kernel level threads](https://cdn.educba.com/academy/wp-content/uploads/2023/12/User-Level-Threads-and-Kernel-Level-Threads.jpg)

[EDUCBA](https://www.educba.com/user-level-threads-and-kernel-level-threads/)

## Q2. Explain multitasking, multithreading and multithreading module

### Multitasking
Multitasking in operating systems allows multiple tasks to run in an concurrent (or interleaved) manner, enhancing system performance.
- Multiprogramming ensures that the CPU (a very fast device) is used by other processes when one process becomes busy with IO (very slow compared to CPU). 
- Multitasking further enhances multiprogramming by allocating fixed slot to each process ready to execute. It mainly runs processes in round robin manner. 

### Multithreading
Multithreading allows a program to execute multiple tasks concurrently within a single process. 
- These tasks, called threads, share the same memory space and resources, leading to improved performance and responsiveness. 
- There are three main multithreading models: `many-to-one`, `one-to-one`, and `many-to-many`. 

### Multithreading Models:

- Many-to-One:
    - Multiple user-level threads are mapped to a single kernel thread. 
    - This model is efficient for thread management within a process, but it limits true parallelism, as only one thread can run on the CPU at a time. 
    - Blocking one thread blocks the entire process. 
    - ![Many-to-one multithreading model](https://docs.oracle.com/cd/E19620-01/805-4031/images/nancb6.eps.gif)
- One-to-One: 
    - Each user-level thread is mapped to a separate kernel thread. 
    - This model provides true parallelism and allows for better utilization of multi-core processors.
    - However, it can be resource intensive due to the overhead of creating and managing multiple kernel threads.
    - ![One-to-One Multithreading Model](https://docs.oracle.com/cd/E19620-01/805-4031/images/nancb7.eps.gif) 
- Many-to-Many: 
    - This model combines the advantages of the previous two. 
    - Multiple user threads are mapped to a smaller or equal number of kernel threads. 
    - This allows for concurrency and parallelism while minimizing overhead. 
    - ![Many-to-Many Multithreading Model](https://docs.oracle.com/cd/E19620-01/805-4031/images/nancb8.eps.gif)


[PrepInsta](https://prepinsta.com/operating-systems/multithreading-models/)

[Oracle Java/Solaris 7 Docs](https://docs.oracle.com/cd/E19620-01/805-4031/6j3qv1oej/index.html)

### Single Core Implementation

- Multitasking Implementation: 
    - The operating system (OS) schedules which task runs at a given time through time-slicing. 
    - This involves rapidly switching between different processes or tasks, allocating a small time slice to each in a round-robin fashion
    - This creates the illusion of simultaneous execution, allowing multiple applications to appear to run concurrently 
- Multithreading Implementation: 
    - Multithreading on a single-core processor can simulate multitasking
    - The CPU switches execution resources between different threads within a single process, enabling concurrent execution
    - While only one thread is actively using the core, rapid switching between threads gives the appearance that multiple threads are running simultaneously 
    - This becomes even easier with Simultaneous Multithreading Implementations(SMT), like Intel's Hyper-Threading, where a single core can execute multiple threads concurrently by sharing resources, although only one thread's instructions are executed at a given moment.

### Multi Core Implementation
- Multitasking Implementation: 
    - Multi-core operating systems can truly execute multiple tasks concurrently, as different CPU cores can work independently on different tasks
    - For example, on a dual-core system, two different applications can access separate processor cores simultaneously, leading to improved overall performance
    - The OS distributes different applications (processes) across the available CPU cores
- Multithreading Implementation: 
    - In a multi-core system, each thread within a multithreaded application can run concurrently on a separate processor core, achieving true simultaneous execution (parallelism)
    - This allows for a significant performance boost for CPU-bound operations 

[NI](https://www.ni.com/en/support/documentation/supplemental/07/differences-between-multithreading-and-multitasking-for-programm.html)

## Q3. What are the benefits of a Real Time Operating System(RTOS)?
A Real-Time Operating System (RTOS) is specifically designed for applications that demand precise timing and deterministic behavior, ensuring tasks are completed within strict deadlines.

Key benefits of using an RTOS include:
*   **Predictability and Determinism** 
    - RTOS guarantees that tasks execute within specified time constraints, providing consistent and predictable behavior
    - This is crucial for applications where the correctness of the system depends not only on the logical result but also on the timely execution of tasks
*   **High Performance and Responsiveness** RTOS systems are fast and responsive, often executing actions within a small fraction of the time needed by general-purpose operating systems
    - They are designed for minimal overhead, enabling faster context switching and efficient resource utilization, which leads to quicker responsiveness
    - Task switching can occur in as little as 3 microseconds.
*   **Reliability and Stability** RTOS are built for high reliability, minimizing the risk of system failures and crashes
    - They are designed to be error-free, ensuring that faults are handled effectively and the system operates reliably even under error conditions
    - This makes them suitable for mission-critical and safety-critical environments such as automotive control, medical devices, and aerospace systems.
*   **Efficient Resource Management** An RTOS optimizes resource utilization by ensuring that high-priority tasks are completed first
    - It efficiently manages resource allocation and deallocation, preventing conflicts among tasks and contributing to overall system stability
    - This also translates to efficient memory usage, as RTOS typically have a small footprint compared to general OS counterparts, demanding far less instruction memory and RAM.
*   **Priority-Based Scheduling** RTOS utilizes priority scheduling, ensuring that high-priority actions are executed before lower-priority ones
    - This efficient task scheduling mechanism guarantees that critical tasks are executed in a timely manner, preventing delays.
*   **Reduced Downtime and High Availability** RTOS ensures maximum system uptime by efficiently utilizing resources and keeping all devices in an active state, leading to minimal downtime
    - As a result, RTOS systems are available 24/7, making them ideal for applications that require continuous operation.
*   **Enhanced Product Quality and Safety** By providing deterministic behavior and robust fault tolerance, RTOS contributes to enhanced product quality, making products safer and more secure, particularly in critical systems where failure can have catastrophic consequences.
*   **Scalability** RTOS are designed to be scalable, capable of managing both simple and complex systems. This allows applications to be expanded or integrated with additional resources without compromising real-time performance.
*   **Modularity and Code Reusability** Many RTOS platforms feature a mandatory core kernel with customizable middleware and protocol stacks, allowing developers to build only what is needed
    - This modularity enables the build-up of a code base that can be reused across different devices, making development and deployment more efficient and scalable.
*   **Cross-Platform Support** Many RTOS can run on various microcontroller (MCU) platforms, simplifying the porting of applications from one platform to another.

[windriver](https://www.windriver.com/solutions/learning/rtos)

[rtosx](https://rtosx.com/real-time-operating-system-rtos/)