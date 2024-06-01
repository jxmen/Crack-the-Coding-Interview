class Solution:

    # implement bottom-up
    def climbStairs(self, n: int) -> int:

        # tabulation
        tabular = {1:1, 2:2}
        for i in range(3, n+1):
            tabular[i] = tabular[i-1] + tabular[i-2]

        return tabular[n]
