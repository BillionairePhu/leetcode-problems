public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int[] result = new int[nums.Count];
        for (int i = 0; i < nums.Count; i++)
        {
            int countOf1 = 0;
            int temp = nums[i];
            while (temp % 2 == 1)
            {
                temp >>= 1;
                countOf1++;
            }

            if (countOf1 == 0)
            {
                result[i] = -1;
                continue;    
            }

            int pow2 = 1 << (countOf1 - 1);
            result[i] = (nums[i] ^ pow2) | (pow2 - 1);
        }
        return result;
    }
}