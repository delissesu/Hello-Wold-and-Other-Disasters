// The total price of order is 52.92 USD and estimated tax is 5.29

// Here, i want to calculate order total, which is total price + tax

// Total price of all products
let total_price_of_products = 
5292

// 10% Tax
let estimated_tax = 529

// Calculate total price and tax first and convert to usd by dividing with 100
let order_total = (total_price_of_products + estimated_tax) / 100

console.log("Order total is:", order_total)
