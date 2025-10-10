# 🔥 Leetcode Problem (3494)

> **Problem:** [Find the Minimum Amount of Time to Brew Potions](https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `Array`, `Simulation`, `Prefix Sum`

---

### ✅ Intuition

Intuition
The requirement is that each potion must be brewed by every wizard, and each wizard can brew only one potion at a time. Once the brewing of a potion begins, it cannot be paused midway and must be completed continuously by all wizards.

First, the brewing of the first potion begins at time 0, so the time each wizard takes to brew it is fixed and easy to calculate. However, the starting time for subsequent potions is not immediately clear.

We may allow the brewing process of the j-th potion to be non-continuous (while the first j−1 potions still require continuity) and let the time for the i-th wizard to finish brewing the j-th potion be times[i][j]. Then we have:

times[i][j]=max(times[i−1][j],times[i][j−1])+skill[i]×mana[j]

After one round of recursion, we obtain the completion time of the j-th potion, times[n−1][j]. At this point, we traverse backwards to update the completion times of the j-th potion for the previous wizards, eliminating the gaps introduced by the earlier allowance of discontinuous brewing.

During implementation, times can be optimized to a one-dimensional array.

---

### 🧪 Complexity

- **Time:** O(n * m)
- **Space:** O(n)