Solution s = new();
Console.WriteLine(s.MaxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]));
Console.WriteLine(s.MaxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]));
Console.WriteLine(s.MaxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]));
public class Solution {
    public int MaxTwoEvents(int[][] events) {
        Array.Sort(events, (a, b) => a[1] - b[1]);
        int[] maxbeforeindex = new int[events.Length];
        maxbeforeindex[0] = events[0][2];
        int max = events[0][2];
        for (int i = 1; i < events.Length; i++)
        {
            int[] e = events[i];
            int left = 0;
            int right = i - 1;
            int index = -1;
            while (left <= right)
            {
                int mid = (left + right) / 2;
                if (events[mid][1] < e[0])
                {
                    index = mid;
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }
            if (index >= 0)
            {
                max = Math.Max(max, maxbeforeindex[index] + e[2]);
            }
            else
            {
                max = Math.Max(max, e[2]);
            }
            maxbeforeindex[i] = Math.Max(e[2], maxbeforeindex[i-1]);
        }
        return max;
    }
}
