class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> frequencies = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if(frequencies.contains(nums[i])){
                return true;
            } else {
                frequencies.add(nums[i]);
            }  
        }
        return false;
    }
}