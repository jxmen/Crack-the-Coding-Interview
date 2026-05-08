class Solution {
    static List<long[]>[] graph; // graph[node] = {next, weight}

    public int networkDelayTime(int[][] times, int n, int k) {
        graph = new ArrayList[n+1];
        for (int i=0; i<=n; i++) graph[i] = new ArrayList<>();
        
        for (int[] time: times) {
            int u = time[0], v = time[1], w = time[2];
            graph[u].add(new long[]{v, w});
        }

        long[] dist = dijkstra(n, k);

        long ans = Arrays.stream(dist).skip(1).max().getAsLong();
        return ans == Long.MAX_VALUE ? -1 : (int) ans;
    }

    long[] dijkstra (int n, int start) {
        long[] dist = new long[n+1];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[start] = 0;

        // cost 기준 오름차순
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[1], b[1]));
        pq.offer(new long[]{start, 0});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            int node = (int) cur[0];
            long cost = cur[1];

            if (cost > dist[node]) continue;

            for (long[] edge: graph[node]) {
                int next = (int) edge[0];
                long nextCost = edge[1] + dist[node];

                if (nextCost < dist[next]) {
                    pq.offer(new long[] {next, nextCost});
                    dist[next] = nextCost;
                }
            }
        }
 
        return dist;
    }
}