class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set = {}
        for num in nums:
            if num in set:
                return True
            else:
                set[num] = True
        return False
            
        