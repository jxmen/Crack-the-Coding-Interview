class Solution {
    public boolean isPalindrome(String s) {
        char[] lower = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase().toCharArray();
        
        int p1 = 0, p2 = lower.length - 1;
        for (int i = 0; i < (int) lower.length / 2; i++) {
            if (lower[p1] != lower[p2]) return false;
            
            p1++;
            p2--;
        }
        
        
        return true;
    }
}