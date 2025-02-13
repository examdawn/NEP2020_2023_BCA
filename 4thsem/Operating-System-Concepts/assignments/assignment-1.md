# Operating System Concepts

Assignment 1 (14/02/2025)

# Short answer questions
## Q1.	Differentiate between multiprogramming and multitasking operating systems.
## Q2.	What is a Process?
## Q3.	What are the main objectives of Operating System?
## Q4.	What is an Operating System?
## Q5.	What is a Thread?
# Long answer questions
## Q1.	What are the functions of Operating System? Explain.
An Operating System manages everything related to the allocation of hardware, and software resources. The purpose is to make the computer more convenient to use while efficiently managing hardware and software resources. 

Many of the functions an operating system performs are:
- Controlling System Performance
    - I monitors and observes the delay time between a service being requested and the requested service being served. This delay time is reduced as much as possible to improve the overall performance of the system.
- Memory ManagementI
    - It allocates the main memory for the program execution, and when the program is completed or terminated, then it deallocates the memory. 
    - Operating systems also keep a record that which byte of memory is assigned to which program.
- Device Management
    - The operating system manages the communication between the computer system and the peripheral devices connected to the I/O port of the system. 
    - Peripheral devices use their respective drivers to communicate with the system. 
    - The operating system determines which program or process is accessed by which connection and device
- Process Management
    - The process is a program under the execution. 
    - The operating system manages all the processes so that each process gets the CPU for a specific time to execute itself, and there will be less waiting time for each process. 
    - This management is also called process scheduling.
- Resource Allocation
    - The operating system manages all the resources of the computer system. 
    - It ensures the use of all the resources by managing which resource is used by which process and for how much time.
- Information and Resource Protection
    - All the data and information available on the machine are protected by the operating system. 
    - If any external resource tries to attack the computer resource and steal the data, then the operating system helps to prevent the attack.
- Job Priority:
    - The work of job priority is creation and promotion. 
    - It determines what action should be done first in a computer system.

[TPointTech](https://www.tpointtech.com/functions-of-operation-system)

[GeeksForGeeks](https://www.geeksforgeeks.org/functions-of-operating-system/)
## Q2.	Write a note on computer system organization.
The computer system is a combination of many parts such as peripheral devices, secondary memory, CPU, etc. 

![Computer System Organization](https://www.tutorialspoint.com/assets/questions/media/10792/Computer%20System%20Organisation.PNG)

After this, we can observe that the Motherboard chipset and CPU handle all the things shown here

It is easy to break them into these categories:
- Memory: 
    - This is where data and instructions are stored. 
    - It is a crucial part of the computer system that allows for the storage and retrieval of information.
- Control Unit: 
    - This component manages the operations of the computer. 
    - It directs the flow of data between the CPU and other components.
- Arithmetic Logic Unit (ALU): 
    - The ALU performs arithmetic and logical operations. 
    - It is responsible for calculations and decision-making processes.
- Input: 
    - This refers to the devices or methods through which data is entered into the computer system.
- Output: 
    - This refers to the devices or methods through which data is presented to the user or other systems.
- Processor: 
    - The processor, or CPU, is the central component that carries out the instructions of a computer program. 
    - It includes the ALU and Control Unit.


[TutorialsPoint](https://www.tutorialspoint.com/computer-system-organisation)

[GeeksForGeeks](https://www.geeksforgeeks.org/computer-organization-von-neumann-architecture/)
## Q3.	Write a note on Threading issues.

- The fork() and exec() system calls: The meaning of the fork() and exec() system calls change in a multithreaded program.
    - fork(): It is used to create a duplicate process. 
        - There are scenarios where we want to create a single threaded fork of a thread but also situations where we need to make a duplicate of all the threads related
            - Some UNIX systems have created two versions of fork() to accommodate this
    - exec(): If a thread calls the exec() system call, the program specified in the parameter to exec() will replace the entire process which includes all threads.
    
- Signal Handling
    - All signals, whether synchronous or asynchronous, follow the same pattern as given here −
        - A signal is generated by the occurrence of a particular event.
        - The signal is delivered to a process.
        - Once delivered, the signal must be handled.

- Cancellation
    - Thread cancellation is the task of terminating a thread before it has completed.
    - For example − If multiple database threads are concurrently searching through a database and one thread returns the result the remaining threads might be cancelled.
    - A target thread is a thread that is to be cancelled, cancellation of target thread may occur in two different scenarios −
        - Asynchronous cancellation − One thread immediately terminates the target thread.
        - Deferred cancellation − The target thread periodically checks whether it should terminate, allowing it an opportunity to terminate itself in an ordinary fashion.

- Thread polls
    - Multithreading in a web server, whenever the server receives a request it creates a separate thread to service the request.
        - If all concurrent requests are allowed to be serviced in a new thread, there is no bound on the number of threads concurrently active in the system.
        - Unlimited thread could exhaust system resources like CPU time or memory.

[TutorialsPoint](https://www.tutorialspoint.com/what-are-threading-issues)

[GeeksForGeeks](https://www.geeksforgeeks.org/threading-issues/)
## Q4.	Explain Process state transition diagram in Process Management.

![Process State Transition Diagram](https://www.researchgate.net/publication/332546783/figure/fig3/AS:749937696464896@1555810488119/Process-state-transition-diagram.png)

(The given image along with an explanation given below in quotes is licensed under CC BY-NC 4.0 and was downloaded from [ResearchGate](https://www.researchgate.net/figure/Process-state-transition-diagram_fig3_332546783) and is from a [paper by Sonia Zouaoui, Lotfi Boussaid, Mtibaa Abdellatif](https://www.researchgate.net/publication/332546783_Priority_based_round_robin_PBRR_CPU_scheduling_algorithm))

The sharing of the processor and resources introduced several states for a task as shown in Figure above: 
1. New: the task is not yet activated. 
2. Ready: the task is enabled and has all the resources it needs to run. 
3. Waiting: the task is waiting for resources. 
4. Running: the task runs. 
5. Terminated: the task has no current application, it has terminated. 

The scheduler is  responsible  for the transition  from  one  task state to another.  
    - For  each  invocation, the scheduler updates the list of ready tasks by including all active tasks and who have their resources and removing tasks that ended their performances or blocked by waiting a resource. 
    - Then among the ready tasks, the scheduler selects the highest priority task to run. 
    - Thus, a task in the new state can move to the ready state. 
    - A task in the ready state may go to running state or waiting state. 
    - A task in running status may return to the ready state if it is preempted by another higher-priority task, it can go to the waiting state if it is waiting for resource liberation or has finished executing, it passes in the passive state. 

(Changes: Adjusted formatting to match the rest of the docs)

## Q5.	What is a System call? Explain different categories of System calls.
System Calls are how your User level Applications, abstractions, and APIs interface with the system's resources, hardware or lower levels. This allows you to make use of the services provided by the kernel.

We can break down System Calls into the following large categories:
- File System
    - This basically allows us to access, read, seek through and write to files.
- Process Control
    - This allows us to perform process management operations.
- Memory Management
    - This allows us to allocate and manage system memory.
- Interprocess Communication
    - This allows us to interact with and exchange data between processes and programs.
- Device Management
    - This allows us to handle various low level hardware connected to the system directly.

![GeeksForGeeks](https://media.geeksforgeeks.org/wp-content/uploads/20231017212555/Types-of-System-Calls-(3)-(2).png)