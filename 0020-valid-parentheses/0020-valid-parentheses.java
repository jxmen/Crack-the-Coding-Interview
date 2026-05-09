class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = Map.of(
            ')', '(', 
            '}', '{',
            ']', '['
        );
        
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (!map.containsKey(c)) {
                stack.add(c);
                continue;
            }

            // TODO:
            if (stack.isEmpty()) return false;
            if (!map.get(c).equals(stack.peekLast())) return false;

            stack.pollLast();
        }

        return stack.isEmpty();
    }
}