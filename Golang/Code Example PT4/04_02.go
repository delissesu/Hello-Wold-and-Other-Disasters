package main

import "fmt"

func buatDaftarBelanja() (func(string) []string, func(int) []string) {
	listBelanja := []string{}
	add := func(item string) []string {
		listBelanja = append(listBelanja, item)
		return listBelanja
	}

	remove := func(index int) []string {
		if index < 0 || index >= len(listBelanja) {
			return listBelanja
		}
		listBelanja = append(listBelanja[:index], listBelanja[index+1:]...)
		return listBelanja
	}

	return add, remove
}

func main4_2() {
	tambahBelanja1, hapusBelanja1 := buatDaftarBelanja()
	// tambahBelanja2, hapusBelanja2 := buatDaftarBelanja()

	fmt.Println("Daftar Belanja 1:")
	fmt.Println(tambahBelanja1("Apel"))
	fmt.Println(tambahBelanja1("Pisang"))
	fmt.Println(tambahBelanja1("Jeruk"))
	fmt.Println(hapusBelanja1(1))
}
