// How to ceiling number like 2.8 to 2? Or 2.5 to 2?

let number = 2.99

// Use floor
let round_down = Math.floor(number)

console.log(round_down)

// Use bitwise or operator with 0 (common trick)
let number_two = 5.24

// Use bitwise with 0
let num_two_round_down = number_two | 0

console.log(num_two_round_down)

// Use double bitwise, ~~
let number_three = 9.99
let num_three_round_down = ~~number_three

console.log(num_three_round_down)

// Use modulo by %1
let number_four = 7.92
let num_four_round_down = number_four - (number_four % 1)

console.log(num_four_round_down)

// Try modulo but in negative number
let neg_number_four = -8.99
let neg_num_four_round_down = neg_number_four - (neg_number_four % 1)

console.log(neg_num_four_round_down)

// Use parseInt
let number_five = 21.99
let num_five_round_down = parseInt(number_five)

console.log(num_five_round_down)