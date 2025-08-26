/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    // Dictionary for Roman numeral values
    const values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    
    let result = 0;
    
    // Iterate through the string
    for (let i = 0; i < s.length; i++) {
        // Get current and next values (next is 0 if undefined)
        const current = values[s[i]];
        const next = i + 1 < s.length ? values[s[i + 1]] : 0;
        
        // If current value is less than next, subtract current
        if (current < next) {
            result -= current;
        } else {
            // Otherwise, add current
            result += current;
        }
    }
    
    return result;
};