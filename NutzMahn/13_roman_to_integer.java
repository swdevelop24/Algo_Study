class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int total = 0;
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        for(int i = 0; i < s.length()-1; i++){
            if(map.get(s.charAt(i)) >= map.get(s.charAt(i+1))){
                total += map.get(s.charAt(i));
            }else{
                total -= map.get(s.charAt(i));
            }
        }

        return total += map.get(s.charAt(s.length() - 1));

    }
}