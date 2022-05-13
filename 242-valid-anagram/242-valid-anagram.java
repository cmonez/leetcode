class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap freqMapStringS = getCharacters(s);
        HashMap freqMapStringT = getCharacters(t);
        return freqMapStringS.equals(freqMapStringT);
    }
    
    public HashMap<Character, Long> getCharacters(String str) {
        HashMap<Character, Long> freqMap = new HashMap();
        for (char letter : str.toCharArray()){
            if(!freqMap.containsKey(letter)) {
                freqMap.put(letter, 1L);
            } else {
                freqMap.put(letter, freqMap.get(letter) + 1);
            } 
        }
        return freqMap;
    }    
}