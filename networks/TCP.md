# [Transmission Control Protocol (TCP)](https://study-ccna.com/tcp-explained/)

### What is a TCP?
It is a connection-based, which means that, before data is sent, a connection between two hosts must be established. The process used to establish a TCP connection is known a *three-way handshake*. After the data is transmitted, the connection is terminated.

TCP uses sequence numbers to identify the order of the bytes sent from each computer so that the data can be reconstructed in order. If any data is lost during the transmission, the sender can retransmit the data. The TCP header is up to 24 bytes long and consists of the following fields:

<img src = "https://603168-1953132-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2016/03/tcp_header.webp"  alt = "tcp_header" width = "450"/>


## [TCP three-way handshake](https://study-ccna.com/tcp-three-way-handshake/)

<img src = "https://603168-1953132-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2018/09/tcp_three_way_handshake_numbers-360x130.avif"  alt = "tcp_three_way_handshake" width = "450"/>

Three-way handshake process consists of three steps:

1. Host A initiates the connection by sending the TCP SYN packet to the destination host. The packet containts the random sequence number (e.g. 5432) which marks the beginning of the sequence numebrs for data that the Host A will transmit.
2. The Server receives the packet and responds with its own sequence number. The response also includes acknowledgement number, whihc is Host A's sequence incremented by 1 (in our case, that would be 5433).
3. Host A acknowledges the response of the Server by sending the acknowledgement number, which is the Server's sequence number incremented by 1.

After the data transmission process is finished, TCP will terminate the conenction between two endpoints.

<img src = "https://603168-1953132-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2018/09/tcp_connection_termination-360x130.avif"  alt = "tcp_three_way_handshake_termination" width = "450"/>

1. The client application that wants to close the connection sends a TCP segment with the FIN (Finished) flag set to 1.
2. The server receives the TCP segment and acknolwedges it with the ACK segment.
3. Server sends its own TCP segment with the FIN flag set to 1 to the client in order to terminate the connection.
4. The client acknowledges the server's FIN segment and closes the connection.

<br /><br />
<!-- blank line -->

**[Table of Contents](https://github.com/rmarasigan/notes#table-of-contents) | [Next](Firewall.md)**