class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numDrinks = numBottles
        numEmpty = numBottles
        
        while numEmpty >= numExchange:
            # Exchange
            numEmpty -= numExchange
            
            # Drink the exchanged bottle
            numDrinks += 1
            numEmpty += 1
            
            numExchange += 1
            
        return numDrinks