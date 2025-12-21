// Best practices to calculate money with floating numbers
// Calculate in cents and convert back to dollars
let cents = (2095 + 799);
let convert = cents / 100; // because in every 100 cents is one dollar
console.log(convert);

// Working with tax and use round method
let price_with_tax = cents * 0.1
let convert_without_round = price_with_tax / 100
let convert_with_round = Math.round(price_with_tax) / 100

// Without round
console.log("without round", convert_without_round)

// With round
console.log("with round", convert_with_round)
