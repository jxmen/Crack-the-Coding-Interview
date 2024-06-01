class Solution {

    // (즉, 'ace'는 'abcde'의 하위 수열이지만 'aec'는 그렇지 않습니다.)
    public boolean isSubsequence(String s, String t) {
       
      // 문자가 겹칠 수도 있어 s에 대한 hashSet은 안된다. acc, accc -> true
      
      // acce abcde 
      // two pointer로 이동?
      // 문자가 같으면 p1, p2 같이 이동
      // 문자가 다를 경우 p2만 이동, p2가 벗어난다면 false 리턴
      // p1과 p2가 같고 모두 각각 문자열의 끝이라면 true를 리턴
      
      char[] sChars = s.toCharArray();
      char[] tChars = t.toCharArray();
      
      int p1 = 0, p2 = 0;
      while (p1 < s.length() && p2 < t.length()) {
        if (sChars[p1] == tChars[p2]) {
          if (p1 == s.length() - 1 && p2 == t.length() - 1) return true;

          p1++;
          p2++;
          continue;
        }

        p2++;                
      } 
      
      return p1 >= s.length();
    }
}
