using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

Solution s = new();
System.Console.WriteLine(s.MinimumDeleteSum("delete","leet"));

public class Solution {
    public int MinimumDeleteSum(string s1, string s2) {
        int[,] n = new int[s1.Length + 1,s2.Length + 1];
        MemoryMarshal.CreateSpan(ref Unsafe.As<byte, int>(ref MemoryMarshal.GetArrayDataReference(n)), n.Length).Fill(int.MaxValue);
        n[0, 0] = 0;
        for (int i = 0; i <= s1.Length; i++)
        {
            for (int j = 0; j <= s2.Length; j++)
            {
                if (i + 1 <= s1.Length)
                {
                    if (j + 1 <= s2.Length && s1[i] == s2[j])
                    {
                        n[i + 1, j + 1] = Math.Min(n[i + 1, j + 1], n[i, j]);
                    }
                    n[i + 1, j] = Math.Min(n[i + 1, j], n[i, j] + (int)s1[i]);
                }
                if (j + 1 <= s2.Length)
                {
                    n[i, j + 1] = Math.Min(n[i, j + 1], n[i, j] + (int)s2[j]);
                }
            }
        }
        return n[s1.Length,s2.Length];
    }
}