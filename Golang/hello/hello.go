package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("Sekarang anda memiliki %g masalah.\n", math.Round(108.3))

	fmt.Println(multiplyNumber(10, 2)) 

	arr := []int{2, 5, 8, 20, 21, 43, 49, 50}
	target := 49

	numFound := false

	result, _ := binarySearch(arr, len(arr), target, numFound)
	fmt.Println("Number position is in ", result)
}

func multiplyNumber(number_one int, number_two int) int {
	return number_one * number_two
}

func binarySearch(a []int, field int, search int, numFound bool) (result int, searchCount int) {
	searchCount, i := 0, 0

	for i <= field {
		searchCount++
		mid := i + (field-i)/2

		if search == a[mid] {
			return mid, searchCount
		} else if search > a[mid] {
			i = mid + 1
		} else {
			field = mid - 1
		}
	}

	return -1, searchCount // Return -1 if the target is not found
}