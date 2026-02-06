public class Solution {
    public long MinimumCost(string source, string target, char[] original, char[] changed, int[] cost) {
        long[,] map = new long[26, 26];
        for (int i = 0; i < 26; i++)
            for (int j = 0; j < 26; j++)
                if (i != j) map[i, j] = -1;
        
        for (int i = 0; i < original.Length; i++)
        {
            if (cost[i] < map[original[i] - 'a', changed[i] - 'a'] || map[original[i] - 'a', changed[i] - 'a'] == -1)
            map[original[i] - 'a', changed[i] - 'a'] = cost[i];

        }

        for (int k = 0; k < 26; k++)
            for (int i = 0; i < 26; i++)
                for (int j = 0; j < 26; j++)
                {
                    if (map[i, k] != -1 && map[k, j] != -1)
                    {
                        if (map[i, k] + map[k, j] < map[i, j] || map[i, j] == -1)
                        map[i, j] = map[i, k] + map[k, j];
                    }
                }

        long totalcost = 0;
        for (int i = 0; i < source.Length; i++)
        {
            long price = map[source[i] - 'a', target[i] - 'a'];
            if (price >= 0) totalcost += price;
            else return -1;
        }
        return totalcost;
    }
}