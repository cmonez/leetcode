class Solution(object):
    def groupAnagrams(self, strs):
        anagramFreqMapWordListHash = {}
        for word in strs:
            sorty = ''.join(sorted(word))
            if sorty not in anagramFreqMapWordListHash:
                anagramFreqMapWordListHash[sorty] = []
            anagramFreqMapWordListHash[sorty].append(word)
        return anagramFreqMapWordListHash.values() 
        
            
        
        
        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        