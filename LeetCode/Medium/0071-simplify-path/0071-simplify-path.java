class Solution {

    public String simplifyPath(String path) {
      Deque<String> stack = new ArrayDeque<>();
      
      for (String str : path.split("/")) {
        if ("".equals(str) || ".".equals(str)) continue;

        if ("..".equals(str)) {
          if (!stack.isEmpty()) stack.pop();
        } else {
          stack.push(str);
        }
      }

      StringBuilder sb = new StringBuilder();
      while (!stack.isEmpty()) {
        sb.insert(0, "/" + stack.pop());
      }
      return sb.length() == 0 ? "/" : sb.toString();
    }
}
