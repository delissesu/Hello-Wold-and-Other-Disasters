package main

import (
	"fmt"
)

type DaftarBelanja struct {
	Add    func(string) []string
	Remove func(int) []string
}

func buatDaftarBelanja2() DaftarBelanja {
	listBelanja := []string{}

	daftarBelanja := DaftarBelanja{
		Add: func(item string) []string {
			listBelanja = append(listBelanja, item)
			return listBelanja
		},
		Remove: func(index int) []string {
			if index < 0 || index >= len(listBelanja) {
				return listBelanja
			}
			listBelanja = append(listBelanja[:index], listBelanja[index+1:]...)
			return listBelanja
		},
	}

	return daftarBelanja
}

func main4_3() {
	belanja1 := buatDaftarBelanja2()

	println("Daftar Belanja 1:")
	fmt.Println(belanja1.Add("Apel"))
	fmt.Println(belanja1.Add("Pisang"))
	fmt.Println(belanja1.Add("Jeruk"))
	fmt.Println(belanja1.Remove(1))
}
