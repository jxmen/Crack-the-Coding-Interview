import java.util.HashMap;
import java.util.Map;

class Solution {
	public boolean isAnagram(String s, String t) {
		Map<String, Integer> anagramMap = new HashMap<>();

		// O(N)
		for (int i = 0; i < s.length(); i++) {
			String key = String.valueOf(s.charAt(i));
			if (anagramMap.containsKey(key)) {
				anagramMap.put(key, anagramMap.get(key) + 1);
			} else {
				anagramMap.put(key, 1);
			}
		}

		// O(N)
		for (int i = 0; i < t.length(); i++) {
			String key = String.valueOf(t.charAt(i));
			if (!anagramMap.containsKey(key)) {
				return false;
			}

			anagramMap.put(key, anagramMap.get(key) - 1);
		}

		// O(N). Total time complexity is O(N)
		return anagramMap.values().stream()
				.allMatch(value -> value == 0);
	}
}
