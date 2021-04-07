age = int(input('How old are you? \n'))
decades = int(age/10)
years = age % 10
print ('You are {}'.format(decades) + ' decades and ' + str(years) + ' old')