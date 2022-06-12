# Simple Client and Server TCP connection
This tutorial is a simple client and server TCP communication where the client receive and send a message to the server and vice versa.

### Connecting to a TCP socket
To establish a connection, the client uses the `DialTCP` in the net package and it returns a `TCPConn` object.  When a connection is established, the client and server begin exchanging data: the client sends a request to the server through a TCPConn object, the server parses the request and sends a response, and the TCPConn object receives the response from the server.

<img src = "https://yalantis.com/uploads/ckeditor/pictures/4266/tcp-socket.png"  alt = "tcp_socket" width = "500"/>

## Client Set-up
Basic operation for the client:
* Establish connection to remote host
* Check if any connection error has occured or not
* Send and receive bytes of information
* Close the connection

```go
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
```

## Server Set-up
Basic operation of the server socket:
* Create a socket on a specific port
* Listen to any attempt of connection
* If the connection is successful, communication can begin between client and server

```go
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
```

### `go`
A Goroutine is a lightweight thread managed by the Go runtime. It is a function or method which executes independently and simultaneously in connection with any other Goroutines present in your program.

Syntax:
```go
// using go keyword as the prefix of your function call
go name()
```

### `WaitGroup`
To wait for the function to finish, you can use a [WaitGroup](https://pkg.go.dev/sync#WaitGroup). The WaitGroup primitive works by counting how many things it needs to wait for using the `Add`, `Done` and `Wait` functions.
* `Add`: increases the count by the number provided to the function (`wg.Add(1)`)
* `Done`: decreases the count by one (`wg.Done()`)
* `Wait`: can then be used to wait until the count reaches zero, meaning that `Done` has been called enough times to offset the calls to `Add`.

### `os.Exit`
`os.Exit` is used when you need to abort the program *immediately*, with no possibility of recovery or running a deferred clean-up statement. This can also be used when your program has done everything it needed to do, and now just needs to exit, i.e. after printing a help message.

### `defer`
A `defer` statement defers the execution of a function until the surrounding function returns.

The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.

## Reference
* [When to use os.Exit and panic](https://stackoverflow.com/questions/28472922/when-to-use-os-exit-and-panic)
* [How to build websockets in Go](https://yalantis.com/blog/how-to-build-websockets-in-go/)
* [Intro to Socket Programming in Go](https://www.developer.com/languages/intro-socket-programming-go/)
* [How to run multiple functions concurrently in Go](https://www.digitalocean.com/community/tutorials/how-to-run-multiple-functions-concurrently-in-go)