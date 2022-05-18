class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setOfNums = set()
        l = 0
        longestSub = 1
        if (len(s) == 1) or (len(s) == 0):
            return len(s)
        for r in range(len(s)):
            while s[r] in setOfNums:
                setOfNums.remove(s[l])
                l += 1
            setOfNums.add(s[r])
            longestSub = max(r-l+1, longestSub)
        return longestSub
             
            