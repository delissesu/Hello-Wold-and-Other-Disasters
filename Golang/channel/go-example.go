// package main

// import (
//     "fmt"
//     "time"
// )

// func foo() {
//     for i := 0; i < 5; i++ {
//         fmt.Println("foo:", i)
//         time.Sleep(100 * time.Millisecond)
//     }
// }

// func bar() {
//     for i := 0; i < 5; i++ {
//         fmt.Println("bar:", i)
//         time.Sleep(200 * time.Millisecond)
//     }
// }

// func main() {
//     go foo() // Memulai goroutine untuk fungsi foo
//     bar()    // Memanggil fungsi bar secara normal

//     time.Sleep(1000 * time.Millisecond) // Menunggu goroutines selesai
// }