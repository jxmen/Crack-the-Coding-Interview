class Solution {
    public boolean isPalindrome(String s) {
        char[] parsed = parse(s).toCharArray();
        int n = parsed.length;

        for (int i=0; i<n; i++) {
            int front = parsed[i], back = parsed[n-i-1];
            if (front != back) {
                return false;
            }
        }

        return true;
    }

    private String parse(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c: s.toCharArray()) {
            if (isAlpha(c)) {
                sb.append(toLower(c));
            }
        }

        return sb.toString();
    }

    private char toLower (char c) {
        return (c >= 'A' && c <= 'Z') ? (char)(c+32) : c;
    }

    private boolean isAlpha(char c) {
        // return Character.isLetterOrDigit();
        return (c >= 'a' && c <= 'z') 
            || (c >= 'A' && c <= 'Z')
            || (c >= '0' && c <= '9');
    }
}
