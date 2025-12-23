// Same like other, but here is to get the 10% tax of total order

// Basketball price and how many ball
let basketball_price = 2095
let basketball = 2
const basketball_final_price = basketball * basketball_price

// Shirt price and shirt piece
let shirt_price = 799
let shirt = 2
const shirt_final_price = shirt * shirt_price

// Total order
const total_order = basketball_final_price + shirt_final_price

// Shipping order
let shipping = 499
let shipping_for_final_order = shipping * 2

// Total before tax, int first (cause i dont want miss calculate after tax)
const total_before_tax = total_order + shipping_for_final_order
console.log(total_before_tax)

// Tax
const tax = 10 / 100

console.log(total_before_tax * tax)
console.log(Math.round(total_before_tax * tax))

console.log(`Estimated tax (10%): $${Math.round(total_before_tax * tax) / 100}`)