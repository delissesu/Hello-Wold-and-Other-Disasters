// #include <iostream>
// using namespace std;

// int main() {
//     int luas[4][3] = {
//         {225 * 335, 299 * 278, 300 * 250},
//         {215 * 394, 144 * 718, 300 * 290},
//         {200 * 400, 240 * 333, 142 * 619},
//         {314 * 298, 411 * 198, 333 * 222}
//     };

//     int harga_jual[3] = {100, 120, 150};

//     cout << luas[0] << endl;

//     for (int merek = 0; merek <3; merek++) {
//             int total = 0;
//             for (int toko = 0; toko < 4; toko++) {
//                 total += luas[toko][merek] * harga_jual[merek];
//             }

//             cout << total << endl;
//     }
// }

// package main
// import "fmt"

// type Kandang struct {
//     panjang int
//     lebar int
// }

// func hitungLuas(kandang []Kandang, kalkulasiLuas func(Kandang) int) []int {
//     var jumlahKandang int = len(kandang)
//     luasKandang := make([]int, jumlahKandang)

//     for i, k := range kandang {
//         fmt.Println(i, k)
//         luasKandang[i] = kalkulasiLuas(k)
//     }

// 	fmt.Println(luasKandang)

//     return luasKandang
// }

// func hitungTotalPenjualan(luasKandang []int, hargaPerCm int) int {
//     var totalHarga int = 0
// 	fmt.Println(totalHarga)
//     for _, luas := range luasKandang {
//         totalHarga += luas * hargaPerCm
// 		fmt.Println(totalHarga)
//     }
//     return totalHarga
// }

// func main() {
//     dataKandang := [][]Kandang{
//         {
//             {panjang: 225, lebar: 335},
//             {panjang: 215, lebar: 394},
//             {panjang: 200, lebar: 400},
//             {panjang: 314, lebar: 298},
//         },
//         {
//             {panjang: 299, lebar: 278},
//             {panjang: 144, lebar: 718},
//             {panjang: 240, lebar: 333},
//             {panjang: 411, lebar: 198},
//         },
//         {
//             {panjang: 300, lebar: 250},
//             {panjang: 300, lebar: 290},
//             {panjang: 142, lebar: 619},
//             {panjang: 333, lebar: 222},
//         },
//     }

//     hargaPerMerek := []int{100, 120, 150}

//     kalkulasiLuas := func(k Kandang) int {
//         return k.panjang * k.lebar
//     }

//     for merek, kandangPerMerek := range dataKandang {
//         luasKandang := hitungLuas(kandangPerMerek, kalkulasiLuas)
//         totalPenjualan := hitungTotalPenjualan(luasKandang, hargaPerMerek[merek])
//         fmt.Printf("Total Penjualan per Kandang: %v\n", totalPenjualan)
//     }
// }

// // package main

// // import (
// //  "fmt"
// //  "net/http"
// //  "time"
// // )

// // // A higher-order function to create middleware
// // func loggingMiddleware(next http.HandlerFunc) http.HandlerFunc {
// //  return func(w http.ResponseWriter, r *http.Request) {
// //   start := time.Now()
// //   fmt.Printf("Request started: %s %s\n", r.Method, r.URL.Path)
// //   next.ServeHTTP(w, r) // Call the wrapped handler
// //   fmt.Printf("Request completed in %v\n", time.Since(start))
// //  }
// // }

// // func mainHandler(w http.ResponseWriter, r *http.Request) {
// //  w.Write([]byte("Hello, World!"))
// // }

// // func main() {
// //  // Wrap the main handler with logging middleware
// //  http.HandleFunc("/", loggingMiddleware(mainHandler))
// //  http.ListenAndServe(":8080", nil)
// // }

// http://localhost:8080/

// package main

// import (
// 	"fmt"
// 	"strconv"
// )

// func tambahSaldo(saldo_sekarang int, jumlah_setoran int) int {
//     var total_saldo int = saldo_sekarang + jumlah_setoran
//     return total_saldo
// }

// func main() {
//     menabung := tambahSaldo // ilmu baru jirlah
//     var saldo int = 12000
//     fmt.Println("Saldo awl: " + strconv.Itoa(saldo))

//     saldoBaru := menabung(saldo, 60000)
//     fmt.Println("Saldo sekarang: ", strconv.Itoa(saldoBaru))
// }


// Online Go compiler to run Golang program online
// Print "Try programiz.pro" message

package main
import "fmt"

func applyOperation(x int, y int, operation func(int, int) int) int {
	return (operation(x, y))
}

func main() {
    add := func(a, b int) int {return a + b}
    multiply := func(a, b int) int {return a * b}
    
    fmt.Println("Ini pertama")
    fmt.Println(applyOperation(12, 2, add))

    fmt.Println("Ini kedua")
    fmt.Println(applyOperation(7, 5, multiply))
}