
def permutate(str, answer):
	if (len(str) == 0):
		print(answer, end = " ")
		return
	
	for i in range(len(str)):
		ch = str[i]
		left_substr = str[0:i]
		right_substr = str[i + 1:]
		result = left_substr + right_substr
		permutate(result, answer + ch)

# Driver Code
answer = ""

str = input("Enter the string : ")

print(f"All the possible permutation of {str} are : ")
permutate(str, answer)