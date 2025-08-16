/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    var numStr = String(num);
    var replaced = false;
    var result = ""
    for(var char of numStr){
        if (replaced == false && char == "6"){
            result += "9";
            replaced = true;
        } else {
            result += char;
        }
    }
    return result;
};

console.log(maximum69Number(69))