/*
Goroutine adalah fungsi atau metode yang berjalan secara bersamaan (concurrently) dengan goroutine lainnya dalam satu program.

Docs dari web:
"A goroutine is a lightweight thread managed by the Go runtime."

Notes:
Kalau ada function gada klausal relation atau tidak ada sebab akibat, jadi fungsi satu tidak perlu menunggu fungsi lain, maka kemungkinan bisa menggunakan go routines (jalankan di thread yang berbeda).
*/

package main

import (
	"fmt"
	"time"
)

// Contoh
func doSomething() {
	fmt.Println("Do Something...")
	time.Sleep(2*time.Second)
	fmt.Println("Finished!")
}

func main() {
	// go doSomething() // Eksekusi do something di thread yang terpisah.
	// go doSomething()  

	// Proses fungsi diatas tidak akan memblokir fungsi ini
	// doSomething()

	// Seandainya ada dua
	// go doSomething() // Ga ada output yang muncul, karena dua proses jalan di thread yang berbeda.
	// Sehingga thread main ga diblokir dan selesai lebih dahulu daripada fungsi di something

	// Di contoh ini, dua fungsi berarti sekitar 2 detik jika dengan go routine dan 4 detik tanpa go routine
	// time.Sleep(4 * time.Second)

	// Contoh thread berbeda, eksekusi bareng sekaligus
	// for i := 1; i < 50; i++ {
	// 	go doSomething()
	// }
	
	// time.Sleep(4*time.Second)
	
	// Bisa juga dengan fungsi anonim
	for i := 0; i < 100; i++ {
		go func(i int) {
			// Go routine bisa menggunakan shared memory address
			// Sehingga bisa idpakai di thread yang berbeda
			fmt.Println(i)
			}(i)
		}
		
	time.Sleep(4*time.Second)
	
}