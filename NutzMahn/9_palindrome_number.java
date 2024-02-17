class Solution {
    public boolean isPalindrome(int x) {
        boolean ispal = false;
        if(x<0){
            return false;
        }

        int num = x;
        int rev = 0;

        while(num != 0){
            int digit = num % 10;
            rev = rev*10 + digit;
            num /= 10;
        }

        if(x == rev){
            ispal = true;
        }

        return ispal;

    }
}