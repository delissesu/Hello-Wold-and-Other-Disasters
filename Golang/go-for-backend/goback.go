package main

import (
	"fmt"
	"log"
	"net/http"
)

func about(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Ini adalah halaman About")
}

// func main() {
// 	http.HandleFunc("/", func (w http.ResponseWriter, r *http.Request)  {
// 		fmt.Fprintf(w, "Halo, ini Backend Golang!")
// 	})

// 	http.HandleFunc("/about", about)

// 	fmt.Println("Server berjalan di Port 8080")
// 	log.Fatal(http.ListenAndServe(":8080", nil))
// 	fmt.Println("Sever Berhenti!")
// }


func loggingMiddleware(next http.HandlerFunc) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        log.Printf("%s %s\n", r.Method, r.URL.Path)
        next(w, r) // panggil handler asli
    }
}

func main() {
    http.HandleFunc("/", loggingMiddleware(func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Halo, ini Backend Golang!")
    }))

    http.HandleFunc("/about", loggingMiddleware(about))

    fmt.Println("Server berjalan di Port 8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
    fmt.Println("Sever Berhenti!")
}
