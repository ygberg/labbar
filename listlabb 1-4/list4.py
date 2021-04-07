numlist = input('type numbers seperated by space: ')
numlist = list(map(int,numlist.split()))
numrem = int(input('how many numbers shall be removed?:  '))
nulists = numlist.sort()

del numlists[0:numrem]


print(numlists)