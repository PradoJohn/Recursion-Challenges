factorial = function(num) {
    if(num==0){
        return 1
    }
    return num * factorial(num-1)
};

palindrome = function(str) {
    console.log(str)
    if (str.length == 0){
        return true
    }
    if (str.charAt(0) != str.charAt(str.length-1)){
        return false
    }
    return palindrome(str.slice(1,-1))
    // console.log()
};

bottles = function(num) {
    
    if (num ==1){
        return `${num} beer bottle left.`

    }
    
    return console.log(`${num} beer bottle, pass arround  ${num-1}`), bottles(num-1)
};

romanNum = function(num) {
    numerals = {
		'M':1000,
		'CM':900,
		'D':500,
		'CD':400,
		'C':100,
		'XC':90,
		'L':50,
		'XL':40,
		'X':10,
		'IX':9,
		'V':5,
		'IV':4,
		'I':1,
	}
    if (num==0){
        return ''
    }
    for([key, value] of Object.entries(numerals)){
        if (num >= value){
            return key + romanNum(num-value)
        }
        
    }
};



// console.log(factorial(5))
console.log(palindrome('radar'))
// console.log(bottles(6))
// console.log(romanNum(1997))