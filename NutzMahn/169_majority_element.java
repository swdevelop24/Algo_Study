class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int last = 0;
        int count = 0;
        int maxCount = 0;
        int maxDigit = 0;

        if(nums.length == 1){
            return nums[0];
        }

        for(int i = 0; i<nums.length; i++){
            if(nums[i] == last){
                count++;
                if(count > maxCount){
                    maxCount = count;
                    maxDigit = last;
                }
            }else if(nums[i] != last){

                last = nums[i];
                count = 1;

            }

        }
        return maxDigit;
    }
}