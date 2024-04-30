class Solution {
    public String longestCommonPrefix(String[] strs) {
        String[] newStrs = Arrays.copyOf(strs, strs.length);
        Arrays.sort(newStrs);

		String first = Optional.ofNullable(newStrs[0]).orElse("");
		String last = Optional.ofNullable(newStrs[newStrs.length - 1]).orElse("");
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Math.min(first.length(), last.length()); i++) {
            if (first.charAt(i) != last.charAt(i)) return sb.toString();
            
            sb.append(first.charAt(i));
        }

        return sb.toString();
    }
}