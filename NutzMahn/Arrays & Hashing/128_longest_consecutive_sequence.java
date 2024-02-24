class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0){
            return 0;
        }else if(nums.length == 1){
            return 1;
        }

        Arrays.sort(nums);
        int count = 1;
        int max = 0;

        for(int i = 1; i < nums.length; i++){
            if(nums.length == 2 && nums[i] - nums[i-1] == 0){
                max = 1;
            }else if(nums[i] - nums[i-1] == 0){
                continue;
            }else if(nums[i] - nums[i-1] == 1){
                count++;
                if(count > max){
                    max = count;
                }
            }else{
                if(count > max){
                    max = count;
                }
                count = 1;
            }
        }
        return max;
    }
}