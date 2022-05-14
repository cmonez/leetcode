class Solution(object):
    def topKFrequent(self, nums, k):
        freqMap = {}
        topk_els = []
        freq = [[] for i in range(len(nums) + 1)]
        for idx in range(len(nums)):
            if nums[idx] not in freqMap:
                freqMap[nums[idx]] = 1
            else:
                freqMap[nums[idx]] += 1 
        for key, value in freqMap.items():
            freq[value].append(key)
            
        for x in range(len(freq) - 1, 0, -1):
            for y in freq[x]:
                topk_els.append(y)
                if len(topk_els) == k:
                    return topk_els
        
        
        
        
        

                
 