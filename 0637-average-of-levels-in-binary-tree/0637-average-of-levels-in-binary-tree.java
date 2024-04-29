/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

	// 트리 레벨의 평균 값을 array로 담아 리턴한다. (bfs)
	public List<Double> averageOfLevels(TreeNode root) {
		List<Double> averages = new ArrayList<>();
		Queue<TreeNode> queue = new LinkedList<>();

		queue.offer(root);
		while (!queue.isEmpty()) {
			int size = queue.size();

			List<TreeNode> queueNodes = new ArrayList<>();
			while (!queue.isEmpty()) {
				queueNodes.add(queue.poll());
			}
			double sum = getSum(queueNodes);

			averages.add(sum / size);
			addToQueue(queueNodes, queue);
		}

		return averages;
	}

	private void addToQueue(List<TreeNode> queueNodes, Queue<TreeNode> queue) {
		queueNodes.forEach(node -> {
			if (node.left != null) {
				queue.offer(node.left);
			}
			if (node.right != null) {
				queue.offer(node.right);
			}
		});
	}

	private double getSum(List<TreeNode> queueNodes) {
		double sum = 0;
		for(TreeNode node : queueNodes) {
			sum += node.val;
		}

		return sum;
	}


}
