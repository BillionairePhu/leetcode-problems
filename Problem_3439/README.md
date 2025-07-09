## Intuitive

This problem is actually simple, when shifting 1 meeting to maximize the continuous freetime, it's actually finding the 2 consecutive freetime slots that combines being the largest freetime (by shifting the meeting between them to the leftmost or rightmost)

## Approach

Convert the given data to an array of freetimes. Then iterate through those freetimes to find **k+1** consecutive freetimes that combines the largest.