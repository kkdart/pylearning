def twoSum(nums, target):
    d = {}
    for i,n in enumerate(nums):
        m = target-n
        if m in d:
            return [d[m],i]
        else:
            d[n]=i
    

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

nums = [3,2,4]
target = 6
print(twoSum(nums,target))

nums = [3,3]
target = 6
print(twoSum(nums,target))