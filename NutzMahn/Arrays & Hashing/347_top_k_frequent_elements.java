
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                map.replace(nums[i], map.get(nums[i]) + 1);
            }
            else{map.put(nums[i], 1);}
        }

        List<Integer> keys = new ArrayList<>(map.keySet());

        keys.sort((a,b) -> map.get(b) - map.get(a));

        int[] topk = new int[k];

        for(int i = 0; i < k; i++){
            topk[i] = keys.get(i);
        }

        return topk;
    }
}