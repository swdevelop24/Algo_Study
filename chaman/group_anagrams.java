/* # Time Complexity -> O(n * k log k), where n is the number of strings in the input array and k is the maximum length of a string.
# Space Complexity -> O(n * k), where n is the number of strings in the input array and k is the maximum length of a string.
# Approach:
# 1. Check if the input array is null or empty. If so, return an empty list.
# 2. Create a HashMap to store anagrams where the key is the sorted version of each string, and the value is a list of anagrams.
# 3. Iterate through the input array:
#    - Convert each string to a char array and sort it.
#    - Convert the sorted char array back to a string, which represents the sorted version of the original string.
#    - Check if the sorted string exists as a key in the HashMap:
#        - If it does not exist, create a new key-value pair with the sorted string as the key and a new list containing the original string as the value.
#        - If it exists, append the original string to the corresponding list.
# 4. After processing all strings, return a list containing the values (lists of anagrams) of the HashMap. */

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        if(strs == null || strs.length == 0)
            return new ArrayList<>();

        Map<String, List<String>> map = new HashMap<>();

        for(String s: strs)
        {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String keyStr = String.valueOf(ca);

            if(!map.containsKey(keyStr))
               
                map.put(keyStr, new ArrayList<>());
                map.get(keyStr).add(s);
        }

        return new ArrayList<>(map.values());
    }
}