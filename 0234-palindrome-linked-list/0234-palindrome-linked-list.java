/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    // TOOD: 공간복잡도를 O(1) 만큼만 사용하기 위해 two pointer를 활용해야 함
    public boolean isPalindrome(ListNode head) {
        return isPalindromeHelpTwoPointer(head);
    }
    
    private boolean isPalindromeHelpTwoPointer(ListNode head) {
        // slow, fast pointer 선언 - slow는 middle까지, slow와 fast를 뒤집어서 비교한다.
        ListNode slow = head, fast = head, prev, temp;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        prev = slow;
        slow = slow.next;
        prev.next = null;
        
        while (slow != null) {
            temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }
        
        fast = head;
        slow = prev;
        while (slow != null) {
            if (fast.val != slow.val) return false;
            slow = slow.next;
            fast = fast.next;
        }
        
        return true;
    }
    
    private boolean isPalindromeHelpTwoStacks(ListNode head) {
        // st1 넣는 과정
        Deque<ListNode> stack = new ArrayDeque<>();
        ListNode node = head;
        while (node != null) {
            stack.push(node);
            node = node.next;
        }
        
        // 12321 같은 케이스도 true를 리턴해야 함
        // 절반만큼 새로운 스택에 넣고 비교해서 같을 경우 true를 리턴한다.
        Deque<ListNode> stack2 = new ArrayDeque<>();
        int size = stack.size(); 
        for (int i = 0; i < size / 2; i++) {
            stack2.push(stack.pop());
        }
        
        // 절반으로 나눌때 홀수일경우 st1에 한개가 남으므로 하나 비워준다.
        if (stack.size() > stack2.size()) {
            stack.pop();
        }
        
        // 비교
        size = stack.size();
        for (int i = 0; i < size; i++) {
            ListNode st1 = stack.pop();
            ListNode st2 = stack2.pop();
            
            if (st1.val != st2.val) return false;
        }
        
        return true;
    }
}