class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i<nums.length; i++)
        {
            int count = 0;
            if(map.get(nums[i]) != null)
                count = map.get(nums[i]);
            map.put(nums[i], ++count);
        }



        Integer[] keys = map.keySet().toArray(new Integer[0]);
        Arrays.sort((keys), (a, b) -> map.get(b) - map.get(a));

        int[] result = new int[k];

        for(int i = 0; i< k; i++)
        {
            result[i] = keys[i];
        }

        return result;
              
    }
}