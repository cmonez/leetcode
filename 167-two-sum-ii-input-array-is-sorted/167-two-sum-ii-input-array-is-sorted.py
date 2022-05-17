class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        result = []
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            
# Two pointer solution
# Use a while loop
# left at 0 right at the end
# if number[left] + number[right] is less than target increment left -> go up
# if number[left] + number[right] is greater than target decrement right -> go down
# if number[left] + number[right] equals target return left+1, right+1
        