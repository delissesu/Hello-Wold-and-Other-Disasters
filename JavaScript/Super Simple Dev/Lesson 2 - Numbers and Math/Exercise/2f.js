// In cart, i have 3 products. The product is 1 basketball, 1 shirt, and 1 toaster. Only for toaster choose shipping with 4.99USD

// Calculate the cost of the products before shipping and tax

// Basketball price
let basketball_price = 2095

// Shirt price
let shirt_price = 799

// Toaster price
let toaster_price = 1899

// Total price of all products and divide with 100 becayse 1 usd is 100 cent
let total_price_of_products = (basketball_price + shirt_price + toaster_price) / 100

console.log(total_price_of_products) // 47.93

// Compare without calculate in cent, only in float
let total_price_in_float = (basketball_price/100) + (shirt_price/100) + (toaster_price/100)

console.log(total_price_in_float) // 47.92999999999999