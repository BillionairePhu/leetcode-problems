public class Solution {
    public bool WinnerSquareGame(int n) {
        bool[] win = new bool[n + 1];
        for (int i = 0; i < win.Length; i++)
        {
            if (!win[n])
                for (int j = 1; i + j * j <= n; j++)
                    win[i + j * j] = true;
        }
        return win[n];
    }
}