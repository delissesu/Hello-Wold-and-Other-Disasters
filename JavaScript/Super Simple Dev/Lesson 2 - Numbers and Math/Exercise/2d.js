// Calculate a 10% tax for total price in 2c
// The last price we got is 33.5
// Remember the 10% is 0.1 because 10/100 is 1/10 and the result is 0.1

let cost = 33.5
let tax_of_cost = cost * 0.1
console.log("The tax is:", tax_of_cost)

// Or if want to use just one number decimal, i try to use round method
let round_tax = Math.round(cost)
let tax_cost_after_round = round_tax * 0.1
console.log("The tax is:", tax_cost_after_round) // the result have inaccurate calculation, this result nice for me to knowing that just some float calculation will have inaccurate result