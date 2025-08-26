/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}

[a,b,h]
subseq 
[a,h,b,c,d,c]

 */
var isSubsequence = function(s, t) {
    if(!s.length) return true
    if(!t.length) return false

    let lettersQueue = [...s]

    for(let i = 0; i < t.length; i++) {
        if(!lettersQueue.length) return true
        if(lettersQueue.length && t[i] === lettersQueue[0]){
            lettersQueue.shift()
        }        
    }

    return lettersQueue.length ? false : true;
};