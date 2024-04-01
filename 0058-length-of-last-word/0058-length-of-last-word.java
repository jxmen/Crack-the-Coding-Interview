class Solution {
	public int lengthOfLastWord(String s) {
		List<String> strings = Arrays.stream(s.split(" "))
				.map(it -> it.trim())
				.filter(it -> it != "")
				.toList();

		String last = strings.get(strings.size() - 1);

		return last.length();
	}
}
