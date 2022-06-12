package main

import (
	"fmt"
	"log"
	"net"
	"os"
	"sync"
)

var (
	protocol = "tcp"
	server   = "0.0.0.0:9000"
	wg       sync.WaitGroup // WaitGroup waits for a collection of goroutines to finish
)

func main() {
	// Resolves address to an address of TCP endpoint
	address, err := net.ResolveTCPAddr(protocol, server)
	if err != nil {
		log.Printf("Error resolving TCP address: %s", err.Error())
		return
	}

	// Connects to a server using a TCP connection
	connection, err := net.DialTCP(protocol, nil, address)
	if err != nil {
		log.Printf("Failed to Dial Server TCP. Error: %s", err.Error())
		return
	}

	// Increment the WaitGroup counter.
	wg.Add(1)
	go func() {
		for i := 0; i < 10; i++ {
			wg.Add(1)

			// Send a message to the server
			message := "Hello!! Register me as one of your sender."
			_, err = connection.Write([]byte(message))
			if err != nil {
				log.Printf("Failed to write data. Error: %s", err.Error())
				return
			}
			fmt.Println("Client connected to ", connection.RemoteAddr().String())

			buffer := make([]byte, 420)
			// Read from TCP buffer
			length, err := connection.Read(buffer)
			if err != nil {
				log.Printf("Failed to read message from TCP server session")
				return
			}
			tmp := buffer[:length]
			fmt.Printf("Server Reply: %s\n", string(tmp))
			fmt.Println("--------------------------------------------------------------------")

			// Decrement the counter when the goroutine completes.
			defer wg.Done()
			// Close the connection
			defer connection.Close()
			// Terminate or exit execution
			defer os.Exit(0)
		}
	}()
	// Wait for it to complete.
	wg.Wait()
}
