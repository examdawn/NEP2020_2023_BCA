# Computer Communications and Networks 
# 2nd Internal Exams - Important Questions
## 2 Marks
### Q1. What is a "Computer Network"?
A computer network is a system that connects many independent computers to share information (data) and resources. The integration of computers and other different devices allows users to communicate more easily. A computer network is a collection of two or more computer systems that are linked together. 
[(GeeksForGeeks)](https://www.geeksforgeeks.org/what-is-computer-networking/)
### Q2. What is a "topology"?
Network Topology refers to the arrangement or layout of different elements (links, nodes, etc.) in a computer network. 
- It defines how devices are interconnected and how data flows within the network. 
- Understanding network topology is essential for designing and managing networks effectively.
### Q3. What is the Physical Layer?
The Physical Layer consists of physical networking Hardware and methods to use it.
- The physical layer sends data bits from one or more devices to other device(s). 
- The physical Layer defines the types of encoding(how the 0’s and 1’s are encoded in a signal)
- The physical Layer is responsible for the communication of the unstructured raw data streams over a physical medium.

[(GeeksForGeeks)](https://www.geeksforgeeks.org/physical-layer-in-osi-model/)
### Q4. What is "switching"?
Switching is a technique used in computer networking to direct data packets between devices on a network. 
- It involves receiving incoming packets and determining the best path for them to reach their destination.
### Q5. What is "multiplexing"?
Multiplexing is a technique used to combine and send the multiple data streams over a single medium. The process of combining the data streams is known as multiplexing and hardware used for multiplexing is known as a multiplexer.  
- Multiplexing is achieved by using a device called Multiplexer (MUX) that combines n input lines to generate a single output line. 
- Multiplexing follows many-to-one, i.e., n input lines and one output line.
[(JavatPoint)](https://www.javatpoint.com/multiplexing-in-computer-network)  
<img src="https://images.javatpoint.com/tutorial/computer-network/images/concept-of-multiplexing.png" alt="Multiplexing" width="400" />

### Q6. What is the Data Link Layer?
The Data Link Layer is responsible for transmitting data from the higher layers, through the hardware from the lower Physical layer.
- It is responsible for the node-to-node delivery of data. Its major role is to ensure error-free transmission of information. 
- It is also responsible for encoding, decoding, and organizing the outgoing and incoming data.
- This is considered the most complex layer of the OSI model as it hides all the underlying complexities of the hardware from the other above layers. 

[(GeeksForGeeks)](https://www.geeksforgeeks.org/data-link-layer/)
### Q7. What is "Error Correction"?
The error simply means any flaw or deviation that occurs while the information is transmitted from the source to the destination in a computer network. 
- In other words, if the message or data transmitted by the source is not identical to the one received at the destination, we can say that there is some Error in the data received.

Data Correction is the process of detecting and correcting these errors. Error Correction can be handled in two ways:

- ***Backward error correction***: 
    - Once the error is discovered, the receiver requests the sender to retransmit the entire data unit.
- ***Forward error correction***: 
    - In this case, the receiver uses the error-correcting code which automatically corrects the errors.

    [(GeeksForGeeks)](https://www.geeksforgeeks.org/error-correction-in-computer-networks/)

    [(Javatpoint)](https://www.javatpoint.com/computer-network-error-correction)
### Q8. What is "Error Detection"?

If the message or data transmitted by the source is not identical to the one received at the destination, we can say that there is some Error in the data received. 
- To detect errors, a common technique is to introduce redundancy bits that provide additional information. 
- Various techniques for error detection include:
    - Simple Parity Check
    - Two-Dimensional Parity Check
    - Checksum
    - Cyclic Redundancy Check (CRC)

### Q9. Mention any 4 applications of Computer Networks
Computer networking has a wide range of applications across various fields. Here are some key areas where it plays a crucial role:

- **Internet Connectivity**: The most obvious application is connecting devices to the internet, enabling access to online resources, communication, and services.

- **Communication**: Networking facilitates email, instant messaging, video conferencing, and VoIP, allowing for real-time communication across the globe.

- **Web Services**: Networking is essential for hosting and accessing websites, web applications, and services, driving e-commerce and online businesses.

- **IoT (Internet of Things)**: Computer networking connects smart devices, enabling automation and data exchange in homes and industries, improving efficiency and control.

- **Cloud Computing**: Networking underpins cloud services, allowing users to access applications and data stored on remote servers rather than on local machines.

- **Social Networking**: Platforms like Facebook, Twitter, and LinkedIn rely on computer networking to connect users, facilitating social interactions and information sharing.

- **Security Systems**: Networking is crucial for connecting surveillance cameras and alarm systems, allowing for remote monitoring and management of security.

- **Healthcare**: In medical settings, networks facilitate electronic health records (EHRs), telemedicine, and real-time patient monitoring, improving patient care.

- **Education**: Educational institutions use networking for e-learning platforms, online classes, and virtual labs, making education more accessible.

### Q10. What is OSI Reference Model?
The OSI (Open Systems Interconnection) Model is a set of rules that explains how different computer systems communicate over a network. OSI Model was developed by the International Organization for Standardization (ISO). The OSI Model consists of 7 layers and each layer has specific functions and responsibilities:
- Physical Layer
- Data Link Layer
- Network Layer
- Transport Layer
- Session Layer
- Presentation Layer
- Application Layer

    
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240615134832/OSI-vs-TCP.png" alt="OSIVsTCPIP" width="400" />

## 4 Marks
### Q11. Explain Any 4 Types of Network Topology with Advantages and Disadvantages
Network Topology refers to the arrangement or layout of different elements (links, nodes, etc.) in a computer network. 

It defines how devices are interconnected and how data flows within the network. Understanding network topology is essential for designing and managing networks effectively. Here are the primary types of network topologies:

#### 1. **Bus Topology**
- All devices share a single communication line (the bus). Data sent by any device travels in both directions along the bus until it reaches its destination.   
<img src="https://media.geeksforgeeks.org/wp-content/uploads/3-55.png" alt="Bus Topology" width="400" />

#### 2. **Star Topology**
- All devices are connected to a central hub or switch. Data is sent from one device to the hub, which then forwards it to the intended recipient.  
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20241028174732747554/Star-Topology.png" alt="Star Topology" width="400" />

#### 3. **Ring Topology**
- Each device is connected to two other devices, forming a circular pathway for data. Data travels in one direction (or both, in some variations) until it reaches its destination.  
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20241028175715256679/Untitled-Diagram-153-1.jpg" alt="Ring Topology" width="400" />

#### 4. **Mesh Topology**
- Every device is connected to every other device, either fully (every device is connected) or partially (some devices are interconnected).  
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20241028174648312121/Mesh-Topology.png" alt="Mesh Topology" width="400" />

#### 5. **Tree Topology**
- A hybrid topology that combines characteristics of star and bus topologies. It has a central hub (like star) with multiple levels of hierarchy, forming a tree-like structure.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240614234036/Tree-topology.png" alt="Tree Topology" width="400" />

 [(GeeksForGeeks)](https://www.geeksforgeeks.org/types-of-network-topology/)  

### Q12. Explain types of Networks with Advantages and Disadvantages
Networks can be classified into several types based on their size, scope, and purpose. Here are the main types of networks, along with their advantages and disadvantages:
#### 1. **Local Area Network (LAN)**

- Definition: A network that covers a small geographic area, like a single building or campus.
- Advantages:
    - High-speed data transfer.
    - Low cost for setting up and maintaining.
    - Easy to connect devices and share resources (like printers and files).
- Disadvantages:
    - Limited range; not suitable for large distances.
    - Security risks if not properly managed.

#### 2. **Wide Area Network (WAN)**

- Definition: A network that spans a large geographic area, such as cities or countries, often using leased telecommunication lines.
- Advantages:  
    - Can connect multiple LANs over long distances.  
    - Facilitates communication across large geographical areas.
- Disadvantages:
    - Higher costs for setup and maintenance.
    - Slower data transfer speeds compared to LANs.
    - More complex management and security considerations.

#### 3. **Metropolitan Area Network (MAN)**

- Definition: A network that covers a city or a large campus, typically larger than a LAN but smaller than a WAN.
- Advantages:
    - Higher speeds than WANs due to shorter distances.
    - Ideal for connecting multiple LANs in a specific area.
- Disadvantages:
    - Can be expensive to set up and maintain.
    - Limited to metropolitan areas.
### Q13. What is the difference between TCP and OSI Model?
TODO
### Q14. Explain Twisted Pair Cable with a Neat Diagram
Twisted Pair Cable is a type of wiring used for transmitting data in telecommunications and networking. 

It was invented by Alexander Graham Bell. Twisted pair cables have two conductors that are generally made up of copper and each conductor has insulation. These two conductors are twisted together, thus giving the name twisted pair cables. [(GeeksForGeeks)](https://www.geeksforgeeks.org/twisted-pair-cable/)
- Twisted Pair Cables are further of two types :
    - Unshielded Twisted Pair Cables (UTP)
    - Shielded Twisted Pair (STP)  
    
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210817095055/cables-660x387.jpg" alt="Twisted" width="400" />

### Q15. Explain Coax Cable with a Neat Diagram
Coaxial Cable is a type of guided media made of Plastics, and copper wires which transmit the signal in electrical form rather than light form. Coaxial cable is also known as coax. 

The core copper conductor is used for the transmission of signals and the insulator is used to provide insulation to the copper conductor the insulator is surrounded by a braided metal conductor which helps to prevent the interference of electrical signals and prevent cross talk. This entire setup is again covered with a protective plastic layer to provide extra safety to the cable.
[(GeeksForGeeks)](https://www.geeksforgeeks.org/what-is-coaxial-cable/)  
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240327120710/CoaxialCable-660x330.jpg" alt="Coaxial" width="400" />

### Q16. Explain Optical Fiber Cable with a Neat Diagram
Optical fiber is a technology used to transmit data by sending short light pulses along a long fiber, which is typically made of glass or plastic. Optical fibers are also resistant to electromagnetic interference.
- Total internal reflection of light is used in the fiber optical cable. Depending on the amount of power needed and the distance needed, the fibers are designed to allow light to travel in parallel with the optical fiber. 
- While multimode fiber is used for transmission over shorter distances, single-mode fiber is used for long-distance transmission. 
- These fibers’ outer covering requires better defense than the core can provide.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20231005184556/Optical-Fiber.png" alt="Optical_Fibre" width="400" />

[(GeeksForGeeks)](https://www.geeksforgeeks.org/optical-fibre-cable/)  


### Q17. Explain Functionality of Data link layer
TODO
### Q18. Explain Checksum with an Example
TODO
### Q19. Explain CRC(Cyclic Redundancy Check) with a Diagram
TODO
### Q20. Explain Hamming Code with an Example
TODO
### Q21. Explain STOP-AND-WAIT ARQ with a Diagram
TODO
### Q22. Explain GO-BACK-N ARQ with a Diagram
TODO
### Q23. Explain Selective Repeat ARQ with a Diagram
TODO