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
	host     = "0.0.0.0:9000"
	wg       sync.WaitGroup // WaitGroup waits for a collection of goroutines to finish
)

func main() {
	fmt.Printf("Server started: %s...\n", host)

	// Resolves address to an address of TCP endpoint
	address, err := net.ResolveTCPAddr(protocol, host)
	if err != nil {
		log.Printf("Error resolving TCP address: %s", err.Error())
		return
	}

	// Setup listener for any incoming TCP connections
	server, err := net.ListenTCP(protocol, address)
	if err != nil {
		log.Printf("Failed to listen to the server. Error: %s", err.Error())
		return
	}
	// Close the connection
	defer server.Close()

	// Accept any new incoming TCP request and returns a connection
	connection, err := server.AcceptTCP()
	if err != nil {
		log.Printf("Failed to accept incoming TCP connection")
		return
	}

	// Increment the WaitGroup counter.
	wg.Add(1)
	go func() {
		for {
			wg.Add(1)

			// Send message to client server
			message := "Hi! Thanks for connecting. I received your message."
			_, err = connection.Write([]byte(message))
			if err != nil {
				log.Printf("Failed to write data. Error: %s", err.Error())
				os.Exit(0)
			}

			buffer := make([]byte, 420)
			// Read from TCP buffer
			length, err := connection.Read(buffer)
			if err != nil {
				log.Printf("Failed to read message from TCP server session. Error: %s", err.Error())
				os.Exit(0)
			}

			tmp := buffer[:length]
			fmt.Println("------------------------------------------------------------")
			fmt.Printf("Client Message: %s\n", string(tmp))
			// Decrement the counter when the goroutine completes.
			wg.Done()
		}
	}()
	// Terminate or exit execution
	defer os.Exit(0)
	// Wait for it to complete.
	wg.Wait()
}
