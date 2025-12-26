class Solution:
    def bestClosingTime(self, customers: str) -> int:
        lowest_penalty = len(customers) + 1
        penalty = sum([(1 if customer == "Y" else 0) for customer in customers])
        closing_time = None
        for i in range(len(customers) + 1):
            if (penalty < lowest_penalty):
                lowest_penalty = penalty
                closing_time = i
            if (i < len(customers)):
                penalty += (-1 if customers[i] == "Y" else 1)
        return closing_time
    

s = Solution()
print("Result", s.bestClosingTime("YYNY"))