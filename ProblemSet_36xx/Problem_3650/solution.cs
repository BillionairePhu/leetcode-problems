Solution s = new();
System.Console.WriteLine(s.MinCost(4, [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]));

public class Solution {
    public int MinCost(int n, int[][] edges) {
        int[] startToICost = new int[n];
        Array.Fill(startToICost, int.MaxValue);
        startToICost[0] = 0;
        bool[] done = new bool[n];
        PriorityQueue<int, int> availablePos = new();
        availablePos.Enqueue(0, 0);
        List<(int, int)>[] pathForward = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) pathForward[i] = [];
        foreach (int[] edge in edges)
        {
            pathForward[edge[0]].Add((edge[1], edge[2]));
            pathForward[edge[1]].Add((edge[0], edge[2] * 2));
        }

        while (availablePos.TryDequeue(out int Pos, out int Min))
        {
            if (done[Pos]) continue;
            
            foreach ((int, int) path in pathForward[Pos])
            {
                if (done[path.Item1]) continue;
                startToICost[path.Item1] = Math.Min(startToICost[path.Item1], Min + path.Item2);
                availablePos.Enqueue(path.Item1, startToICost[path.Item1]);
            }
            done[Pos] = true;
        }
        return startToICost[n - 1] == int.MaxValue ? -1 : startToICost[n - 1];
    }
}