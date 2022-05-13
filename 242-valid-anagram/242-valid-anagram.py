class Solution(object):
    def isAnagram(self, s, t):
        freqMapS = self.getFrequency(s)
        freqMapT = self.getFrequency(t)
        return freqMapS == freqMapT
        
    def getFrequency(self, word):
        freqMap = {}
        for char in word:
            if char in freqMap:
                freqMap[char] += 1
            else:
                freqMap[char] = 1
        return freqMap
    
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        