a = int(input('how many people: '))
b = int(input('the capacity of the lift: '))
c = a // b
if a % b != 0:
    c = c + 1
print(str(c) + ' lifts are needed to course all parties ')