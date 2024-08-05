import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
	public String kthDistinct(String[] arr, int k) {
		Map<String, Integer> countMap = new HashMap<>();
		Arrays.stream(arr).forEach(s -> countMap.put(s, countMap.getOrDefault(s, 0) + 1));

		// array를 돌면서 key의 value가 하나인 것 중 k번째 key 리턴
		for (String s: arr) {
			if (countMap.get(s) == 1) {
				if (k == 1) {
					return s;
				}
				k--;
			}
		}

		return "";
	}
}
