class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();

        for(String word: strs){
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sWord = new String(chars);

            if(!map.containsKey(sWord)){
                map.put(sWord, new ArrayList<>());
            }

            map.get(sWord).add(word);
        }
        return new ArrayList<>(map.values());
    }
}