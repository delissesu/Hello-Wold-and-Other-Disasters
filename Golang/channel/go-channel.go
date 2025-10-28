/*
Channels are a typed conduit through which you can send and receive values with the channel operator, <-.

ch <- v    // Send v to channel ch.
v := <-ch  // Receive from ch, and
           // assign value to v.
(The data flows in the direction of the arrow.)

Like maps and slices, channels must be created before use:

ch := make(chan int)
By default, sends and receives block until the other side is ready. This allows goroutines to synchronize without explicit locks or condition variables.
*/

package main

import "fmt"

type Person struct{}

func sum(s []int, c chan int) {
	sum := 0

	for _, v := range s {
		sum += v
	}
	// send sum ke c
	c <- sum
}

func main() {
	// Call run
	run()

	// Cara inisiasi channel dengan menggunakan built in function make
	// c:=make(chan int)
	// Hasil kembalian dari channel adalah sebuah address
	// c := make(chan Person) // Tiped atanya juga bisa menggunakan struct
	// fmt.Println(c)

	// Cara untuk send dan receive value dari sebuah channel
	s := []int{12, 21, 35, 65, 34, 80, 32, 45, 87, 90}

	c := make(chan int)
	go sum(s[len(s)/2:], c)
	go sum(s[:len(s)/2], c)

	// terima value dari c
	x, y := <-c, <-c

	fmt.Println(x, y)

}
