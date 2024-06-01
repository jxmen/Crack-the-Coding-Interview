class Solution {
    private val cache = mutableMapOf<Int, Int>()
    
    fun climbStairs(n: Int, count: Int = 0): Int {
        if (n == 0 || n == 1) return count + 1
        if (cache.containsKey(n)) return cache.get(n)!!
        
        val answer1 = climbStairs(n - 1, count)
        cache[n-1] = answer1
        
        val answer2 = climbStairs(n - 2, count)
        cache[n-2] = answer2
        
        return answer1 + answer2
    }
}