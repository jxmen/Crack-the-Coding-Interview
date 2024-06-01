import java.util.ArrayDeque;
import java.util.Deque;
import java.util.stream.IntStream;

class BrowserHistory {

	private Deque<String> stack1 = new ArrayDeque<>();
	private Deque<String> stack2 = new ArrayDeque<>();

	public BrowserHistory(String homepage) {
		visit(homepage);
	}

	public void visit(String url) {
		stack1.push(url);
        stack2.clear();
	}

	public String back(int steps) {
		for (int i = 0; i < steps; i++) {
			if (stack1.size() <= 1) break;

			stack2.push(stack1.pop());
		}

        return stack1.peek();
	}

	public String forward(int steps) {
		for (int i = 0; i < steps; i++) {
			if (stack2.isEmpty()) break;
			
			stack1.push(stack2.pop());
		}

		return stack1.peek();
	}
}


/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */
