class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> groupedAnagrams = new ArrayList<List<String>>();
        HashMap <HashMap<Character, Integer>,ArrayList<String>> hashMapOfAnagrams = new HashMap<>();
        for(String word : strs) {
            HashMap<Character, Integer> hashy = getFreqMap(word);
            if(hashMapOfAnagrams.containsKey(hashy)) {
                ArrayList<String> oldList = hashMapOfAnagrams.get(hashy);
                oldList.add(word);
                hashMapOfAnagrams.put(hashy, oldList);
            } else {
                hashMapOfAnagrams.put(hashy, new ArrayList<>(Arrays.asList(word)));
            }
        }
        for(List<String> wordList : hashMapOfAnagrams.values()) {
            groupedAnagrams.add(wordList);
        }
        return groupedAnagrams;
    }
    
    
    public HashMap<Character, Integer> getFreqMap(String str) {
        char[] charArray = str.toCharArray();
        HashMap<Character, Integer> freqMap = new HashMap<>();
        for(int i = 0; i < charArray.length; i++) {
            if (freqMap.containsKey(Character.valueOf(charArray[i]))) {
                Integer newFreqCount = freqMap.get(Character.valueOf(charArray[i])) + 1;
                freqMap.put(Character.valueOf(charArray[i]), newFreqCount);
            } else {
                freqMap.put(Character.valueOf(charArray[i]), 1);
            }
        }
        return freqMap;
    }
    
    
    
}