class Solution(object):
    def twoSum(self, nums, target):
        indexMap = {}
        indexMap[nums[0]] = 0
        list = []
        for idx in range(1, len(nums)):
            difference = target - nums[idx]
            if difference in indexMap:
                list.append(idx)
                list.append(indexMap[difference])
            indexMap[nums[idx]] = idx
        return list
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        