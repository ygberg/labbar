var input = ['3.12', '5', '18', '19.24', '1953.2262', '0.001564', '1.1445']

var sum = 0
for(i=0;i!=input.length;i++){
    sum = sum + parseFloat(input[i])
    
}
var vat = sum *0.20
var tot = sum + vat
console.log("Sum ="+sum)
console.log("VAT ="+vat)
console.log("total = "+tot)

