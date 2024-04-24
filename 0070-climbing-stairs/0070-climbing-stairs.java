class Solution {
    private Map<Integer, Integer> cache = new HashMap<>();
    
    public int climbStairs(int n) {
        return climbStairsHelp(n, 0);
    }
    
    private int climbStairsHelp(int n, int count) {
        if (n == 0 || n == 1) return count + 1;
            
        if (cache.containsKey(n)) {
            return cache.get(n);
        }
        
        int answer1 = climbStairsHelp(n - 1, count);
        cache.put(n-1, answer1);
        
        int answer2 = climbStairsHelp(n - 2, count);
        cache.put(n-2, answer2);
        
        return answer1 + answer2;
    }
}