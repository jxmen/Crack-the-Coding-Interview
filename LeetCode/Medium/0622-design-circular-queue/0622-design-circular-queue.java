class MyCircularQueue {
	private int front;
	private int rear;
    private int[] data;
    private int k;
    private int size;

	public MyCircularQueue(int k) {
        this.data = new int[k];
        for (int i = 0; i < k; i++) {
            this.data[i] = -1;
        }

        this.front = 0;
        this.rear = -1;
        this.size = 0;
        this.k = k;
	}

	public boolean enQueue(int value) {
        if (isFull()) return false;

        // rear가 k-1을 넘을 경우 다시 0으로 이동
        rear = (rear + 1) % k;
		this.data[rear] = value;
        size++;
        return true;
	}

	public boolean deQueue() {
        if (isEmpty()) return false;

        // front가 k-1을 넘을 경우 다시 0으로 이동
        front = (front + 1) % k;
        size--;
        return true;
	}

	public int Front() {
        if (isEmpty()) return -1;

        return data[front];
	}

	public int Rear() {
        if (isEmpty()) return -1;

        return data[rear];
	}

	public boolean isEmpty() {
        return size == 0;
	}

	public boolean isFull() {
        return size == k;
	}
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
