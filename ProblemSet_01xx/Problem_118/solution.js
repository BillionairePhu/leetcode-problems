/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    const results = [[1]];

    var row = [1]
    for(var i = 1; i<numRows; i++){
        var newRow = row.concat(1);
        for(var j = 1; j<newRow.length-1; j++){
            newRow[j] = row[j-1] + row[j];
        }
        results.push(newRow);
        row = newRow;
    }

    return results;
};

console.log("Result", generate(5))