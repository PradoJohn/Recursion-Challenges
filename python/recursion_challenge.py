

# factorial target = 5
# 1 * 2 * 3 * 4 * 5 = 120
def factorial(x):
	
	if x == 0:
		return 1
	
	return x * factorial(x-1)
# String is plandrome 
# 
def palindrome(string): # radar
	
	#base case
	if len(string) == 0:
		return True
	
	if string[0] != string[-1]:
		return False
	
	#recursion
	return palindrome(string[1:-1]) # ada # d
	


#
def bottles(num):
	
	if num == 1:
		return "1 last beeer"
	else:
		print(f"{num} bottles of beer. pass it around nowbecomes {num-1}")
		return bottles(num-1)

	#
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

def roman_num(num):
	# result = ""
	#base case
	if num == 0:
		return ''
	for key, value in numerals.items():
		if num >= value:
			# result += key
			# times = num//value
			# result += key*times
			return key + roman_num(num-value) #97
		
# M +'CM'
# print(roman_num(1997))




# print(bottles(5))


# print(factorial(5))
print(palindrome('Not A Palindrom')) # True

