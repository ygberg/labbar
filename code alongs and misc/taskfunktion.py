#doubleChar('The') -->'TThhee'

def Dc(str1):
    result = ''
    for char in str1:
        result +=char *2
        print(char)
    return result
print(Dc('test'))