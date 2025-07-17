package main

import (
	"fmt"
	"net"
	"time"
)

func scanPort(protocol, hostname string, port int, results chan<- int) {
	address := fmt.Sprintf("%s:%d", hostname, port)
	conn, err := net.DialTimeout(protocol, address, 1*time.Second)
	if err != nil {
		results <- 0 // Port is closed or unreachable
		return
	}
	conn.Close()
	results <- port // Port is open
}

func main() {
	target := "localhost"
	startPort := 1
	endPort := 1024
	results := make(chan int)

	for port := startPort; port <= endPort; port++ {
		go scanPort("tcp", target, port, results)
	}

	for i := startPort; i <= endPort; i++ {
		port := <-results
		if port != 0 {
			fmt.Printf("Port %d is open\n", port)
		}
	}
}