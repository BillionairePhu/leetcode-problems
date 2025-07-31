var subarrayBitwiseORs = function(arr) {
    const result = new Set();
    let currSet = new Set();

    for (const num of arr) {
        const newSet = new Set();

        for (const val of currSet) {
            const orVal = val | num;
            newSet.add(orVal);
            result.add(orVal);
        }

        newSet.add(num);
        currSet = newSet;

        result.add(num);
    }

    return result.size;
};