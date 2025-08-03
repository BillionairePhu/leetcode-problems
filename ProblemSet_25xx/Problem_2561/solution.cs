[TestClass]
public class Solution
{
    [TestMethod]
    public void MinCostTest()
    {
        Console.WriteLine(MinCost([4, 2, 2, 2], [1, 4, 1, 2]));
        Console.WriteLine(MinCost([2, 3, 4, 1], [3, 2, 5, 1]));
        Console.WriteLine(MinCost([4, 4, 4, 4, 3], [5, 5, 5, 5, 3]));
    }
    public long MinCost(int[] basket1, int[] basket2)
    {
        List<int> needtomovefromb1 = [];
        List<int> needtomovefromb2 = [];
        Array.Sort(basket1);
        Array.Sort(basket2);
        int min = Math.Min(basket1[0], basket2[0]);
        int ptr1 = 0; int ptr2 = 0;
        while (ptr1 < basket1.Length && ptr2 < basket1.Length)
        {
            if (basket1[ptr1] > basket2[ptr2])
            {
                if (ptr2 + 1 < basket1.Length && basket2[ptr2++] == basket2[ptr2++])
                    needtomovefromb2.Add(basket2[ptr2 - 2]);
                else return -1;
            }
            else if (basket1[ptr1] == basket2[ptr2])
            {
                ptr1++; ptr2++;
            }
            else
            {
                if (ptr1 + 1 < basket1.Length && basket1[ptr1++] == basket1[ptr1++])
                    needtomovefromb1.Add(basket1[ptr1 - 2]);
                else return -1;
            }
        }
        while (ptr1 < basket1.Length)
        {
            if (ptr1 + 1 < basket1.Length && basket1[ptr1++] == basket1[ptr1++])
                needtomovefromb1.Add(basket1[ptr1 - 2]);
            else return -1;
        }
        while (ptr2 < basket1.Length)
        {
            if (ptr2 + 1 < basket1.Length && basket2[ptr2++] == basket2[ptr2++])
                needtomovefromb2.Add(basket2[ptr1 - 2]);
            else return -1;
        }
        int score = 0;
        for (int i = 0; i < needtomovefromb1.Count; i++)
        {
            int value = Math.Min(needtomovefromb1[i], needtomovefromb2[needtomovefromb1.Count - i - 1]);
            if (value > min * 2) value = min * 2;
            score += value;
        }
        return score;
    }
}