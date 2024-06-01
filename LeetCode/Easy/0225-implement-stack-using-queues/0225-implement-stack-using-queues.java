class MyStack {

    Queue<Integer> queue1 = new LinkedList<>();
    Queue<Integer> queue2 = new LinkedList<>();

    public MyStack() {
    }
    
    public void push(int x) {
      if (queue1.isEmpty() && queue2.isEmpty()) {
        queue1.offer(x);
        return;
      }

      while(!queue1.isEmpty()) {
        queue2.offer(queue1.poll());
      }
      while(!queue2.isEmpty()) {
        queue1.offer(queue2.poll());
      }

      queue2.offer(x);
    }
    
    public int pop() {
      if (!queue2.isEmpty()) {
        return queue2.poll();
      } else {
        return queue1.poll();
      }
    }
    
    public int top() {
       if (queue2.isEmpty()) {
         return queue1.peek();
       } else {
         return queue2.peek();
       }
    }
    
    public boolean empty() {
      return queue1.isEmpty() && queue2.isEmpty();       
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
