# Route Table

## What is Routing?
Routing is the process of path decision through the destination and forwarding the packets through this path. With routing process, routers decide where to send the packets. In other words, routing is one of the intelligent parts of networking. Because, according to some metrics, available paths are determined through a destination and the best path is selected between these paths.

## Routing Table
Routing table is basically a data list stored in Routers. Routers stores the available routes and the best routes in this routing tables. They are built with directly connected nodes, with static routing and with routing protocols like OSPF, BGP, EIGRP, etc. With this routing information, a list is created and this list is called *Routing Table*.

Each router maintains a routing table and stores it in RAM. A routing table is used by routers to determine the path to the destination network. Each routing table consists of the following entries:
* **Network destination and subnet mask**
   * Specifies a range of IP addresses
* **Remote router**
   * IP address of the router used to reach that network
* **Outgoing interfaces**
   * Outgoing interface the packet should go out to reach the destination network

There are three different methods for populating a routing table:
* Directly connected subnets
* Using static routing
* Using dynamic routing

A routing table uses static and dynamic Internet Protocol or IP address to identify devices, and works with an ARP cache that holds these addresses. The the routing table is commonly referred to as a resource for finding the next hop, or subsequent route for a data packet. Static or dynamic routes may be compared to find the best path for data.

## Reference
* [IP Routing](https://study-ccna.com/what-is-ip-routing/)
* [Routing Table](https://ipcisco.com/lesson/routing-table/)
* [Routing Table](https://www.techopedia.com/definition/15720/routing-table)