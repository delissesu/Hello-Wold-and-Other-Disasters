// In here, i want to calculate the 10% tax exactly
// I know the total before tax is 52.92 USD, so if the total get calculate by the tax 10%, the tax is 5.29

// Price before tax
let total_before_tax = 52.92

// Tax
let tax = 10 / 100

// Estimated tax
let estimated_tax = total_before_tax * tax

console.log(estimated_tax) // 5.292000000000001

// The problem is the result not 5.29, but 5.292000000000001
// To avoid this problem, i use math round method

let any_total_before_tax = Math.round((total_before_tax * 100) * tax) / 100

console.log("Estimated 10% tax is:", any_total_before_tax)