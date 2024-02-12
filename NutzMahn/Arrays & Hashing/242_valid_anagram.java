

class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> smap = new HashMap<>();
        HashMap<Character, Integer> tmap = new HashMap<>();

        char[] schar = s.toCharArray();
        char[] tchar = t.toCharArray();

        boolean b = false;

        for(char c: schar){
            if(smap.containsKey(c)){
                int temp = smap.get(c);
                temp+=1;
                smap.replace(c, temp);
            }else{
                smap.put(c, 1);
            }
        }

        for(char c: tchar){
            if(tmap.containsKey(c)){
                int temp = tmap.get(c);
                temp+=1;
                tmap.replace(c, temp);
            }else{
                tmap.put(c, 1);
            }
        }

        if(smap.equals(tmap)){
            b = true;
            return b;
        }

        return b;
    }
}