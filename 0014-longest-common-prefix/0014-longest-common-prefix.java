class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        
        String[] newStrs = Arrays.copyOf(strs, strs.length);
        Arrays.sort(newStrs);

		String first = newStrs[0];
        String last = newStrs[newStrs.length - 1];
        
        int i = 0;
        while (i < first.length() && i < last.length() && first.charAt(i) == last.charAt(i)) {
            i++;
        }

        return first.substring(0, i);
    }
}