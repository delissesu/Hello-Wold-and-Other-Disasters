// Calculate the total cost of a toaster with price 18.50 USD and 2 shirts with 7.50 USD for each shirt

// Toaster price
let toaster_price = 18.50

// Shirts price
let shirts = 2
// Calculate in cents
let shirts_price = shirts * 750
// Convert to dollars
let shirts_final_price = shirts_price / 100

console.log(shirts_price)
console.log(shirts_final_price)

// Total cost
let total_cost = toaster_price + shirts_final_price
console.log("The total cost is:", total_cost)