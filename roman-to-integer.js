/**
 * @param {string} s
 * @return {number}

Main rules:
I -> 1
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1000

Execpetions:
IV: 
IX:
XL:
XC:
CD:
CM:

Dictionary:
x -> y



15char max
always valid values
valid string

 */
var romanToInt = function (s) {
    const dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    let result = 0

    for (let i = 0; i < s.length; i++) {
        if(s[i] < s[i+1]) {
           result += dictionary[`${s[i]}${s[i+j]}`]
        } else {
            result += dictionary[s[i]]
        }
    }

    return result
};