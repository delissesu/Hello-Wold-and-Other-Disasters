// Here, i must create a string interpolation based on setup price

let basketball_price = 2095
let basketball = 2
const basketball_final_price = basketball * basketball_price

let shirt_price = 799
let shirt = 2
const shirt_final_price = shirt * shirt_price

console.log(`Items (${4}): $${(basketball_final_price + shirt_final_price) / 100}`)