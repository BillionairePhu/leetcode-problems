# 🔥 Leetcode Problem (3573)

> **Problem:** [Best Time to Buy and Sell Stock V](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Dynamic Programming`

---

### ✅ Intuition

From the description of the challenge, we can see that this problem could be somewhat related to the knapsack problem.

To solve it, we will use dynamic programming and try to solve max profit for `j` first prices and `i` first transactions (starting from zero and dynamically increases). The only thing left is that we need to find a relationship between the current max profit and the already-discovered max profit.

We can note `dp[i][j] = [r1, r2, r3]` being an array of interested result value at `j` first prices and `i` first transactions.
- `r1` is the max profit if the last transaction ends at price `j` and is a long (normal transaction)
- `r2` is the max profit if the last transaction ends at price `j` and is a short (short transaction)
- `r1` is the max profit up until now (no matter where the last transaction ends and the type of the last transaction).

We can build these relationships:
- `dp[i][j][0] = max(dp[i-1][j-1][0], dp[i-1][j-2][2]) + prices[j] - prices[j-1]`
- `dp[i][j][1] = max(dp[i-1][j-1][1], dp[i-1][j-2][2]) - prices[j] + prices[j-1]`
- `dp[i][j][2] = max(dp[i][j][0], dp[i][j][1], dp[i][j-1][2])`

Just slowly read through the relationships and you will understand.

---

### 🧪 Complexity

- **Time:** O(k*n)
- **Space:** O(k*n)