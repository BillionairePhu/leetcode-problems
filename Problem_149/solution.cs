namespace LeetCode;

public class Solution149
{
    public int MaxPoints(int[][] points)
    {
        if (points.Length == 1) return 1;
        int max = 0;
        for (int i = 0; i < points.Length; i++)
        {
            bool[] check = new bool[points.Length];
            var pointa = points[i];
            for (int j = i + 1; j < points.Length; j++)
            {
                if (check[j]) continue;

                var pointb = points[j];
                int numpoints = 2;
                for (int k = j + 1; k < points.Length; k++)
                {
                    var pointc = points[k];
                    if ((pointa[0] - pointb[0]) * (pointb[1] - pointc[1]) == (pointa[1] - pointb[1]) * (pointb[0] - pointc[0]))
                    {
                        numpoints++;
                        check[k] = true;
                    }
                }
                max = Math.Max(numpoints, max);
            }
        }
        return max;
    }
}