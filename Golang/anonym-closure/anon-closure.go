package main
import "fmt"

func closureKasir() func(int) int {
	total := 0
	return func(harga int) int {
		total += harga
		return total
	}
}

func main() {
	hargaBarang := map[string]int{
		"Beras" : 5000,
		"Minyak" : 7000,
		"Gula" : 6000,
	}

	kasir := closureKasir()

	barangBelanjaan := []string{"Beras", "Minyak", "Gula"}

	for _, item := range barangBelanjaan {
		func(namaBarang string) {
			harga := hargaBarang[namaBarang]
			totalBelanjaan := kasir(harga)
			fmt.Printf("Beli %-6s | Harga %d | Total Belanjaan: %d\n", namaBarang, harga, totalBelanjaan)
		}(item)
	}
}