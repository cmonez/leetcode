class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
                
            l, r = i+1, len(nums) - 1
             
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num,  nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1       
        return res
                    
                
            
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]
# iterate through each value
# init left to be current value plus 1, right is length
# while left is less than left
# add values
# if values equals zero push
# increment and decrement left right respectively
            
        
        