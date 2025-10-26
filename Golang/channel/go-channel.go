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

type Person struct {}

func main() {
    // Cara inisiasi channel dengan menggunakan built in function make
    // c:=make(chan int)
    // Hasil kembalian dari channel adalah sebuah address
    c := make(chan Person) // Tiped atanya juga bisa menggunakan struct
    fmt.Println(c) 
}