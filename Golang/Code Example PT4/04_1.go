package main

import "fmt"

func CreateTabungan(saldoAwal int) func(int) int {
	isi := saldoAwal
	return func(setoran int) int {
		fmt.Println("alamat variable isi: ", &isi)
		fmt.Println("nilai mula-mula variable isi: ", isi)
		isi += setoran
		fmt.Println("nilai akhir variable isi: ", isi)
		return isi
	}
}

func main4_1() {
	tabungan1 := CreateTabungan(100)
	tabungan2 := CreateTabungan(100)

	fmt.Println("tabungan1: ", tabungan1(50))
	fmt.Println("tabungan2: ", tabungan2(70))
	// fmt.Println("tabungan1: ", tabungan1(10))
	// fmt.Println("tabungan2: ", tabungan2(5))
}
