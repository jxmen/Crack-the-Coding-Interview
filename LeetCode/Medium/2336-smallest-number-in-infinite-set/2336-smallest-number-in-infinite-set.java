class SmallestInfiniteSet {
	private PriorityQueue<Integer> minHeap;
	private HashSet<Integer> removedSet;

	public SmallestInfiniteSet() {
		minHeap = new PriorityQueue<>();
		removedSet = new HashSet<>();
		IntStream.rangeClosed(1, 1000).forEach(minHeap::add);
	}

	// Removes and returns the smallest integer contained in the infinite set.
	public int popSmallest() {
		Integer smallest = minHeap.poll();
		removedSet.add(smallest);

		return smallest;
	}

	// Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
	public void addBack(int num) {
		if (removedSet.contains(num)) {
			removedSet.remove(num);
			minHeap.add(num);
		}
	}
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */
