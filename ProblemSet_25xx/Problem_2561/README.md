# 🔥 Leetcode Problem (2561)

> **Problem:** [Rearranging Fruits](https://leetcode.com/problems/rearranging-fruits/description/?envType=daily-question&envId=2025-08-02)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Array`, `Hash table`, `Greedy`, `Sort`

---

### ✅ Intuition

In order to be able to rearranging both baskets to be equal, the frequencies (in both baskets) of each fruit cost must be even.

Now, supposed that it's possible to rearrange both baskets to be equal. Then, we will find the "result basket" after rearranging. This is easy to calculate, just simply divide the total frequencies of each fruit cost into two.

After that, we try to rearrange basket 1 into that result basket (because rearranging basket 1 will simultaneously rearrange basket 2). 

Note that the problem ask us to rearrange such that the cost of all swaps is minimum. Normally, we would want to swap one small cost fruit with one high cost fruit so that the swap cost is minimum. However, here is a catch: you can swap intermediate fruits to obtain minimum swap cost (for example, we want to swap 5 with 100 but there exists a fruit costing only 1 in the other basket => swap 5 with 1 and then swap that 1 with 100).

OK, now that the method is clearly, we can clearly see that we need to find the list of fruits that need to be swapped (supposed `n`) => The result would be sum of `n/2` lowest-cost fruits except if that fruit has a cost higher than `2 * min_cost`.

---

### 🧪 Complexity

- **Time:** O(n log(n))
- **Space:** O(n)