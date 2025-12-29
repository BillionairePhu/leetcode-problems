public class Solution {
    public bool CanAliceWin(int n) {
        int k = 10;
        bool turn = false;
        while (n >= k)
        {
            turn = !turn;
            n -= k;
            k--;
        }
        return turn;
    }
}