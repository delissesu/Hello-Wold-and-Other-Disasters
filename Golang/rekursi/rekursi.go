package main

import "fmt"

func factorialRecursive(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorialRecursive(n-1)
}

func factorialIterative(n int) int {
    result := 1
    for i := 1; i <= n; i++ {
        result *= i
    }
    return result
}

func main() {
    fmt.Println("Iteratif:", factorialIterative(100000)) // 0
    fmt.Println("Rekursif:", factorialRecursive(100000)) // 0
}
