// Total price of all products is 47.93
// In here, i want to calculate total price + shipping and handling where have 4.99 USD to get total before tax

// Total price
let total_price_of_products = 4793

// Tax
let tax_of_order = 499

// Calculate total before tax
let total_before_tax = (total_price_of_products + tax_of_order) / 100

console.log("Total price before tax is:", total_before_tax)