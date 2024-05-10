class Solution {
    fun romanToInt(s: String, sum: Int = 0): Int {
        if (s.isEmpty()) return sum

        return when {
            s.startsWith("M") -> romanToInt(s.substring(1), sum + 1000)
            s.startsWith("CM") -> romanToInt(s.substring(2), sum + 900)
            s.startsWith("D") -> romanToInt(s.substring(1), sum + 500)
            s.startsWith("CD") -> romanToInt(s.substring(2), sum + 400)
            s.startsWith("C") -> romanToInt(s.substring(1), sum + 100)
            s.startsWith("XC") -> romanToInt(s.substring(2), sum + 90)
            s.startsWith("L") -> romanToInt(s.substring(1), sum + 50)
            s.startsWith("XL") -> romanToInt(s.substring(2), sum + 40)
            s.startsWith("X") -> romanToInt(s.substring(1), sum + 10)
            s.startsWith("IX") -> romanToInt(s.substring(2), sum + 9)
            s.startsWith("V") -> romanToInt(s.substring(1), sum + 5)
            s.startsWith("IV") -> romanToInt(s.substring(2), sum + 4)
            s.startsWith("I") -> romanToInt(s.substring(1), sum + 1)
            else -> sum
        }
    }
}