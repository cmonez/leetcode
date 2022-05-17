class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueSet = set(nums)
        longestConsecutiveSequence = 0
        for num in nums:
            if (num - 1) not in uniqueSet:
                length = 0
                while (num + length) in uniqueSet:
                    length += 1
                if length > longestConsecutiveSequence:
                    longestConsecutiveSequence = length
        return longestConsecutiveSequence
                
                
        
        
        
        
        
# Create a set of the numbers
# Determine what the start of a sequence is
# Determine: is number - 1 in the set?
# if YES continue
# else beginning of sequence
# while loop
# increment set