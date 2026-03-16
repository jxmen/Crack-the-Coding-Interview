/*
슬라이딩 윈도우를 어떻게 활용해야 할까?

s = abcabcbb

- n...1 for문을 순회하면서 0부터 i까지의 문자열이 모두 일치하지 않는다면 i 리턴?

*/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        Queue<Character> queue = new ArrayDeque<>();
        int maxLength = 0;

        for (char c : s.toCharArray()) {
            if (!set.contains(c)) {
                queue.offer(c);
                set.add(c);
            } else {
                while (queue.peek() != c) {
                    set.remove(queue.poll());
                }

                queue.poll();
                queue.offer(c);
                set.add(c);
            }

            maxLength = Math.max(maxLength, queue.size());
        }

        return maxLength;
    }
}