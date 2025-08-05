/**
 * @param {number[]} fruits
 * @param {number[]} baskets
 * @return {number}
 */
var numOfUnplacedFruits = function(fruits, baskets) {
    var result = 0;

    fruits.forEach(fruit => {
        var isPlaced = false;
        for(var i = 0; i<baskets.length; i++){
            if (baskets[i] >= fruit) {
                isPlaced = true;
                baskets[i] = 0;
                break;
            }
        }
        if (!isPlaced) result += 1;
    });

    return result;
};