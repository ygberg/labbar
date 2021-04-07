start = int(input('ASCII start for tripplets: '))
num =  3
for i in range (0,num):
    for j in range(0,num):
         for k in range(0,num):
            print(f"{chr(start + i)} {chr(start + j)} {chr(start + k)} ")
