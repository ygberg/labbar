# arryCheck([1,1,2,3,1]) retun True
#AC[1,1,2,4,1,]

n = [1,1,2,3,1]
n1 =[1,1,2,4,1]
def arryCheck(nums):
       
    for item in nums:
        if nums[item] == 1 and nums[item + 1] == 2 and nums[item +2] == 3:
            return True
        else:
             return False

print(arryCheck(n))
print(arryCheck(n1))