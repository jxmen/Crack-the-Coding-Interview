class RecentCounter {
    Queue<Integer> queue = new LinkedList<>();

    public RecentCounter() {
    }
    
    // 새로운 요청이 t초에 주어질 때 최근 3초간의 요청들의 개수를 리턴하라. (새 요청 포함)
    public int ping(int t) {
        int pollCount = 0;

        // 큐에서 시간이 지난 것들의 개수를 구한 후 그것만큼 큐에서 꺼낸다
        for (int it: queue) {
            if ((it + 3000) < t) pollCount++;
        }
        IntStream.rangeClosed(1, pollCount).forEach(_ -> queue.poll());

        queue.offer(t);
        return queue.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
