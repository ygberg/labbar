var input = ['12', 'John', '15', 'Alfred', '9']
var minage = parseInt( input[0])

for(i=1;i!=input.length;i++){
    if(parseInt (input[i])> minage)
    console.log(i)
    agepos = i
    break
}

console.log("name = "+input[i]+" age = "+input[i+1])