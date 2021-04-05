# 2 strings , return True if either of strings appears in the very end
#  of the other string

 #end_other('Hiabc', 'abc') --> true
 #end_other('AbC','HiaBc') --> True
 #ignore upper and lower case
a = 'Hiabc'
b = 'abc'
c = 'AbC'
d = 'HiaBc'

def checkString(a,b):
     #make a and b lower case
     #return true or false
    aa =  a.lower()
    bb = b.lower()
    for i in a:
        
        if aa[i-1] == bb[i-1] and aa [i-2] == bb[i-2] and aa[i-3] == bb[i-3]:
            return True
        else: return False

print(checkString(a,b))
print(checkString(c,d))