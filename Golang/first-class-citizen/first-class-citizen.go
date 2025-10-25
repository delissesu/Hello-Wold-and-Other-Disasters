package main

import "fmt"

func main() {
	// Kemampuan untuk memperlakukan fungsi sebagai nilai
	greet := func() {
		fmt.Println("Naveria Works")
	}

	greet()

	myKisah(waifu1)
	myKisah(waifu2)

	double := func(x int) int { return x * 2 }
	execute(double, 5)

	// // Metode 3 : Return dari fungsi lain
	// fungsiYangDipecah := get_nama()
	// fungsiYangDipecah()
}

// Kemampuan untuk meneruskan fungsi sebagai argumen
func waifu1() string {
	return "Chinatsu Kano"
}

func waifu2() string {
	return "Anzu Hanashiro"
}
// Di bahasa lain, "func() yang tidak mengembalikan nilai dan tak memiliki parameter disebut fungsi void"	
func myKisah(waifu func() string) {
	fmt.Println("Halo mY", waifu())
}

// Kemampuan untuk mengembalikan fungsi dari fungsi lain
// func get_nama() func() {
// 	return func() {
// 		fmt.Println("Halo King!")
// 	}
// }


// package main

// import "fmt"
	
// func main() {
// 	my_slice := []string{"Kano", "Anzu", "Naoko"}

// 	fmt.Println(my_slice, len(my_slice), cap(my_slice))

// 	new_slice := make([]int, 4, 10)

// 	fmt.Println(new_slice)
// 	new_slice[0] = 1

// 	fmt.Println(new_slice)

// 	// for i; i < 10; i ++ {
		
// 	// }
// }

// Fungsi yang menerima fungsi lain sebagai parameter
func execute(f func(int) int, val int) {
    fmt.Println("Result:", f(val))
}