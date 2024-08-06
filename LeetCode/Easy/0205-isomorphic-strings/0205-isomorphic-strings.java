import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;

class Solution {
	public boolean isIsomorphic(String s, String t) {
		return isIsomorphicWithCounter(s, t);
	}

	public boolean isIsomorphicWithCounter(String s, String t) {
		Map<Character, Integer> map1 = new HashMap<>();
		List<Integer> list1 = new ArrayList<>();

		// paper/title의 경우 01023/01023 둘의 형태가 같을 경우 true를 리턴하도록 한다.
		int count = 0;
		for (char c : s.toCharArray()) {
			if (!map1.containsKey(c)) {
				map1.put(c, count++);
			}
			list1.add(map1.get(c));
		}

		count = 0;
		Map<Character, Integer> map2 = new HashMap<>();
		for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
			if (!map2.containsKey(c)) {
				map2.put(c, count++);
			}
            
            // list2를 만들지 않고, 인덱스를 비교해서 다르다면 바로 false를 리턴한다. 
			if (list1.get(i) != map2.get(c)) { // O(1)
                return false;
            }
		}

		return true;
	}

	public boolean isIsomorphicWithLinkedList(String s, String t) {
		// {b:3} -> {a:1} -> {b:1} -> {a:1}
		List<Map.Entry<Character, Integer>> entries = new LinkedList<>();
		Character prev = null;
		int count = 0;
		for (char c : s.toCharArray()) {
			if (prev == null) {
				prev = c;
				count = 1;
				continue;
			}

			if (Objects.equals(c, prev)) {
				count += 1;
			} else {
				entries.add(Map.entry(prev, count));
				prev = c;
				count = 1;
			}
		}

		if (count != 0) {
			entries.add(Map.entry(prev, count));
		}

		prev = null;
		count = 0;
		// {b:c} , {a:d} 형태로 문자열을 담는다. 기존에 키가 있는데 value가 다르다면 false를 리턴한다.
		Map<Character, Character> map = new HashMap<>();
		Iterator<Map.Entry<Character, Integer>> iterator = entries.iterator();
		for (char c : t.toCharArray()) {
			if (prev == null) {
				prev = c;
				count = 1;
				continue;
			}

			if (Objects.equals(c, prev)) {
				count += 1;
			} else {
				// 카운트가 다르면 바로 false
				if (!iterator.hasNext()) return false;
				Map.Entry<Character, Integer> next = iterator.next();
				Character key = next.getKey();
				Integer value = next.getValue();

				if (count != value) return false;
				if (map.containsKey(key) && map.get(key) != prev) return false;

				map.put(key, prev);
				prev = c;
				count = 1;
			}
		}

		// 마지막에 남은 값이 있는지 확인한다.
		if (!iterator.hasNext()) return false;

		Map.Entry<Character, Integer> next = iterator.next();
		Character key = next.getKey();
		Integer value = next.getValue();
		if (map.containsKey(key) && map.get(key) != prev) return false;
		return value == count;
	}

	// 실패
	public boolean isIsomorphicWithHashMap(String s, String t) {
		// a -> b로 대체될 수 있지만 동일한 문자에 대해 다른 문자로 대체될 수 없다.
		// aaa -> aaa는 어떤 케이스인가? a가 a로 변경되었다고 가정해야 하나?
		// hashmap을 2개 만들고, 두개의 value가 모두 동일하다면 true를 리턴한다.
		Map<String, Integer> map1 = new HashMap<>(); // LinkedHashMap??
		Map<String, Integer> map2 = new HashMap<>();
		Arrays.stream(s.split("")).forEach(c -> map1.put(c, map1.getOrDefault(c, 0) + 1));
		Arrays.stream(t.split("")).forEach(c -> map2.put(c, map2.getOrDefault(c, 0) + 1));

		List<Integer> values = map1.values().stream().sorted().collect(Collectors.toList());
		List<Integer> values2 = map2.values().stream().sorted().collect(Collectors.toList());

		//  bba/bab
		// bbbaba / abbbba
		// b:4, a:2

		for (int i = 0; i < values.size(); i++) {
			Integer i1 = values.get(i);
			Integer i2 = values2.get(i);
			if (i1 != i2) {
				return false;
			}
		}

		return true;
	}
}
