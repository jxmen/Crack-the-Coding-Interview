import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class Solution {
	public boolean closeStrings(String word1, String word2) {
		// 숫자 빈도수를 모두 구하고, 숫사 빈도수에 대한 것을 array로 만들고 정렬 후 비교하자.
		HashMap<Character, Integer> map1 = new HashMap<>();
		HashMap<Character, Integer> map2 = new HashMap<>();
		Set<Character> set = new HashSet<>();
		for (char c : word1.toCharArray()) {
			map1.put(c, map1.getOrDefault(c, 0) + 1);
			set.add(c);
		}

		for (char c : word2.toCharArray()) {
			map2.put(c, map2.getOrDefault(c, 0) + 1);
			if (!set.contains(c)) return false;
		}

		if (map1.size() != map2.size()) return false;
		int[] freq1 = new int[map1.size()];
		int[] freq2 = new int[map2.size()];
		int i = 0;
		for (int freq : map1.values()) {
			freq1[i++] = freq;
		}

		i = 0;
		for (int freq : map2.values()) {
			freq2[i++] = freq;
		}

		Arrays.sort(freq1);
		Arrays.sort(freq2);

		for (int j = 0; j < freq1.length; j++) {
			if (freq1[j] != freq2[j]) return false;
		}

		return true;
	}
}
