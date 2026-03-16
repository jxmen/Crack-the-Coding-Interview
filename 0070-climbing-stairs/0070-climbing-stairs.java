// TODO: 점화식을 먼저 세우자

/*
    dp[1] = 1 (step1)
    dp[2] = 2 (step1, step2)
    dp[3] = 3 = d[i-1] + dp[i-2]
    
    dp[4] = 5
*/        

class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;

        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];
    }
}
