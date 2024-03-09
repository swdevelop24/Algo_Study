class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int start = 0;
        int length = 1;
        int maxLength = 0;


        for(int i=0; i<nums.length; i++)
            set.add(nums[i]);

        for(int s:set)
        {
            if(!set.contains(s-1))
            {

                start = s;
                length = 1;
                while(set.contains(start+1))
                {
                    start++;
                    length++;
                }
                        maxLength = Math.max(maxLength, length);
            }

        }
    
        System.out.println(set);
        return maxLength;
        
    }
}