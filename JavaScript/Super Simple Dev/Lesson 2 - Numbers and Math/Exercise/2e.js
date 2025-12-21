// Calculate 20% tax in 2c

// Total cost in 2c
let cost = 33.5

// Tax, becuase 20%, the tax is 0.2
let tax = 0.2

// Cost tax
let cost_tax = cost * tax
console.log(cost_tax)

// But how if i use cost 335 instead 33.5?
let any_cost = 335
let any_tax = 0.2

// I think because 33.5 have one point decimal, it is must divide by 10?
let any_cost_tax = any_cost * any_tax / 10

console.log(any_cost_tax)