# 🔥 Leetcode Problem (2092)

> **Problem:** [Find All People With Secret](https://leetcode.com/problems/find-all-people-with-secret/description/?envType=daily-question&envId=2025-12-19)<br />
> **Difficulty:** Hard<br/>
> **Tags:** `Depth-first-search`

---

### ✅ Intuition

First, we need to sort the meetings by the time it is happening first so that we can process the secret-spreading time-wise.

We have a `secret_keepers` array to mark whether or not a person is currently holding the secret.

Then for each time frame, we will process the meetings such that each person will have a list of `related` persons (with whom a person is having a meeting with). Finally, for each time frame, we depth-first-search the secret-holders via their related persons and mark all persons on the way to be secret keepers.

Remember to do depth-first-search one more time for the last time frame.

After that, just iterate through all person to get the list of secret keepers.

---

### 💡Implementation

For implementation, we use object-oriented `Person` so that the code is easily readable. Each `Person` instance will have a `hasAlreadySharedSecret` to flag if the person has been reached before while searching so that we do not loop forever.

---

### 🧪 Complexity

Let M be the number of meetings and N be the number of persons.

- **Time:** O(M x log(M) + M x N)
- **Space:** O(M + N)