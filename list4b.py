numlist = input('type numbers seperated by space: ')
numlist = list(map(int,numlist.split()))
numrem = int(input('how many numbers shall be removed?:  '))

for item in numlist:
    