// Always rounded up any floating number

// Use ceil method
let number = 5.1
let round_number = Math.ceil(number)

console.log(round_number)

// Use bitwise, same case like rounding down, but use trick (playin w negative symbol)
let number_two = 9.2
let round_up_number_two = -(-number_two | 0)

console.log(round_up_number_two)

// Use ternary
let number_three = 4.2
let round_up_number_three = number_three % 1 == 0 ? num : (number_three | 0) + 1

console.log(round_up_number_three)