class Solution 
{
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] result = new int[length];
        
        // Calculate the product of all elements on the left side
        int leftProduct = 1;
        for (int i = 0; i < length; i++) {
            result[i] = leftProduct;
            leftProduct *= nums[i];
        }
        
        // Calculate the product of all elements on the right side
        int rightProduct = 1;
        for (int i = length - 1; i >= 0; i--) {
            result[i] *= rightProduct;
            rightProduct *= nums[i];
        }
        
        return result;
    }
}
