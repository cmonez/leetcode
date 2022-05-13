class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] tuple = new int[2];
        HashMap<Integer, Integer> indexMap = new HashMap();
        indexMap.put(new Integer(nums[0]), new Integer(0));
        for(int i = 1; i < nums.length; i++) {
            int difference = target - nums[i];
            if(indexMap.containsKey(difference)) {
                tuple[0] = i;
                tuple[1] = indexMap.get(difference);
            }
            indexMap.put(new Integer(nums[i]), new Integer(i));
        }
        return tuple;
    }
}