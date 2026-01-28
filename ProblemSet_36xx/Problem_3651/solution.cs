Solution s = new();
int a = s.MinCost([[1,3,3],[2,5,4],[4,3,5]], 2);
System.Console.WriteLine(a);
public class Solution {
    public int MinCost(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[,] minCost = new int[m, n];
        HashSet<int> all = [];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                minCost[i, j] = int.MaxValue;
                all.Add(grid[i][j]);
            }
        }
        MinCostValue[] minCostAtValue = all.Select(i => new MinCostValue(i, -1)).ToArray();
        Array.Sort(minCostAtValue);
        minCost[m - 1, n - 1] = 0;
        // BFS
        for (int i = m - 1; i >= 0; i--)
            for (int j = n - 1; j >= 0; j--)
            {
                if (i < m - 1) minCost[i, j] = Math.Min(minCost[i, j], minCost[i + 1, j] + grid[i + 1][j]);
                if (j < n - 1) minCost[i, j] = Math.Min(minCost[i, j], minCost[i, j + 1] + grid[i][j + 1]);

                int index = Array.BinarySearch(minCostAtValue, new MinCostValue(grid[i][j], -1));
                if (minCostAtValue[index].MinCost < 0 || minCostAtValue[index].MinCost >= minCost[i, j]) minCostAtValue[index].MinCost = minCost[i, j];
            }

        for (int t = 0; t < k; t++)
        {
            int[,] minCostBeforeTeleport = (int[,])minCost.Clone();

            for (int i = 1; i < minCostAtValue.Length; i++)
            {
                minCostAtValue[i].MinCost = Math.Min(minCostAtValue[i].MinCost, minCostAtValue[i - 1].MinCost);
            }

            for (int i = m - 1; i >= 0; i--)
                for (int j = n - 1; j >= 0; j--)
                {
                    int index = Array.BinarySearch(minCostAtValue, new MinCostValue(grid[i][j], -1));
                    minCost[i, j] = Math.Min(minCostBeforeTeleport[i, j], minCostAtValue[index].MinCost);
                    
                }
            

            for (int i = m - 1; i >= 0; i--)
                for (int j = n - 1; j >= 0; j--)
                {
                    if (i < m - 1) minCost[i, j] = Math.Min(minCost[i, j], minCost[i + 1, j] + grid[i + 1][j]);
                    if (j < n - 1) minCost[i, j] = Math.Min(minCost[i, j], minCost[i, j + 1] + grid[i][j + 1]);
                    
                    int index = Array.BinarySearch(minCostAtValue, new MinCostValue(grid[i][j], -1));
                    if (minCostAtValue[index].MinCost < 0 || minCostAtValue[index].MinCost >= minCost[i, j]) minCostAtValue[index].MinCost = minCost[i, j];
                }
        }
        return minCost[0, 0];
    }
}

public class MinCostValue(int value, int minCost) : IComparable<MinCostValue>
{
    public int Value = value;
    public int MinCost = minCost;
    public int CompareTo(MinCostValue other)
    {
        return Value.CompareTo(other.Value);
    }
}
