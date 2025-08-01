# Write your solution here
def generate(numRows: int):
    results = []
    currRow = [1]
    for _ in range(numRows):
        newRow = currRow.copy()
        newRow.append(1)
        for j in range(1, len(newRow)-1):
            newRow[j] = currRow[j-1] + currRow[j]
        results.append(currRow)
        currRow = newRow
    return results

print("Result", generate(5))