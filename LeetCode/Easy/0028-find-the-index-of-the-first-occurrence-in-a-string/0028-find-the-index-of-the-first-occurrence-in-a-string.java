class Solution {
    public int strStr(String haystack, String needle) {
        if (Objects.equals(haystack, needle)) return 0;

        // sliding window로 needle과 haystack이 같다면 i 인덱스 리턴
        for (int i = 0; i < haystack.length() - needle.length() + 1; i++) {
            String subStrings = haystack.substring(i, i + needle.length());
            if (Objects.equals(needle, subStrings)) return i;
        }

        return -1; // 없다면 -1
    }
}