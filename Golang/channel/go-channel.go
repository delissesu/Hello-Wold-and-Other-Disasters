// /*
// Channels are a typed conduit through which you can send and receive values with the channel operator, <-.

// ch <- v    // Send v to channel ch.
// v := <-ch  // Receive from ch, and
//            // assign value to v.
// (The data flows in the direction of the arrow.)

// Like maps and slices, channels must be created before use:

// ch := make(chan int)
// By default, sends and receives block until the other side is ready. This allows goroutines to synchronize without explicit locks or condition variables.
// */

// package main

// import "fmt"

// type Person struct{}

// func sum(s []int, c chan int) {
// 	sum := 0

// 	for _, v := range s {
// 		sum += v
// 	}
// 	// send sum ke c
// 	c <- sum
// }

// func main() {
// 	// Call run
// 	// run()

// 	// Cara inisiasi channel dengan menggunakan built in function make
// 	// c:=make(chan int)
// 	// Hasil kembalian dari channel adalah sebuah address
// 	// c := make(chan Person) // Tiped atanya juga bisa menggunakan struct
// 	// fmt.Println(c)

// 	// Cara untuk send dan receive value dari sebuah channel
// 	s := []int{12, 21, 35, 65, 34, 80, 32, 45, 87, 90}

// 	c := make(chan int)
// 	go sum(s[len(s)/2:], c)
// 	go sum(s[:len(s)/2], c)

// 	// terima value dari c
// 	x, y := <-c, <-c

// 	fmt.Println(x, y)

// }

package main

import (
	"log"
	"math/rand"
	"os"
	"os/signal"
	"sync"
	"syscall"
	"time"
)

type Customer struct {
	id int
}

type Teller struct {
	id int
}

type Bank chan Teller
type Queue chan Customer

func (b Bank) ServerCustomers(queue Queue, spv *sync.WaitGroup) {
	// Jika semua antrian sudah dilayani sampai selesai, maka melaporkan ke Supervisor bahwa sudah selesai.
	defer spv.Done()

	// Setiap Teller akan selalu mendengarkan antrian yang masuk.
	for customer := range queue {
		// Teller yang sedang kosong akan mengambil antrian.
		tellerID := <-b
		log.Print("Customer #", customer.id, " serve by Teller #", tellerID)

		// Setiap nasabah memiliki masalah bervariasi, maka kita buat durasi yang random.
		time.Sleep(time.Second*3 + time.Duration(rand.Intn(16)))
		log.Print("Customer #", customer.id, " done by Teller #", tellerID)

		// Setelah selesai melayani, Teller akan kembali menerima antrian selanjutnya terhadap Bank.
		b <- tellerID
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())

	// Kita akan membuat sebuah Bank dengan membuka 10 Teller.
	bank := make(Bank, 10)

	// Selnjutnya Teller akan ditempatkan pada meja pelayanan masing-masing.
	for tellerID := 0; tellerID < cap(bank); tellerID++ {
		bank <- Teller{id: tellerID}
	}

	// Inisiasi Supervisor
	spv := &sync.WaitGroup{}

	// Setelah Teller siap pada mejanya, kita akan membuat antrian nasabah dan setiap Teller siap melayani antrian.
	queue := make(Queue)
	for i := 0; i < cap(bank); i++ {
		// Setiap teller akan didaftarkan kepada supervisor bahwa tugas siap dimulai.
		spv.Add(1)
		go bank.ServerCustomers(queue, spv)
	}

	// Mendaftarkan signal ketika program diinterupsi (Ctrl-C)
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)

	// Setelah semua Teller dan Antrian siap, maka nasabah dipersilakan masuk sesuai antrian.
	// Nasabah akan selalu berdatangan, karena tidak ada kondisi perulangan berhenti.
	for customerID := 0; ; customerID++ {
		select {
		case <-c:
			// Jika mendapatkan sinyal interupsi, maka channel antrian akan ditutup.
			log.Print("Bank akan segera tutup, antrian dihentikan...")
			close(queue)

			// Namun, supervisor akan tetap menunggu sampai semua teller selesai melayani yang tersisa.
			spv.Wait()

			log.Println("Terimakasih, bank sudah tutup.")
			return
		default:
		}

		// Jika antrian sedang penuh, maka nasabah akan menunggu.
		log.Print("Customer #", customerID, " is waiting...")
		queue <- Customer{id: customerID}
	}
}