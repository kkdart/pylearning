from typing import List

def search(nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1    
        while l <= r:
            p = l + (r-l)//2
            if nums[p] == target:
                return p
            if target <nums[p]:
                r = p-1
            else:
                l = p +1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))

nums = [-1,0,3,5,9,12]
target = 2
print(search(nums,target))