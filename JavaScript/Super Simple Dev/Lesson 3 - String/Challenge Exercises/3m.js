// Calculate the total price in 3l before tax
// Just add the basket final price, shirt final price, and shipping for each item (2 item rn hehe)

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

console.log(`Total before tax: $${(total_order + shipping_for_final_order) / 100}`)
