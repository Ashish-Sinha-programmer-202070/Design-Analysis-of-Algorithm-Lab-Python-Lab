''' Write a function which return all the unique palindromes from a given string '''

# function To exapnd left and right pointers to find the longest palindrome
def expand(s, l, r):
    len_s = len(s)
    while l >= 0 and r < len_s and s[l] == s[r]:
        l -= 1
        r += 1
    return l+1, r-1


# function to find all unique palindromes
def get_unique_palin(s):
    length = len(s)
    # using set, so that only unique palindromes will be returned
    result = set()  
    for i in range(length):
        l1, r1 = expand(s, i, i)
        l2, r2 = expand(s, i, i+1)

        # condition to avoid single letters in odd palindrome case
        if l1 != r1:
            result.add(s[l1:r1+1])

        # condition to check for even palindrome case
        if l2 < r2:
            result.add(s[l2:r2+1])

        # returns set as a list
    return list(result)


# run this code if this file is executed directley in the terminal
# function To exapnd left and right pointers to find the longest palindrome
def expand(s, l, r):
    len_s = len(s)
    while l >= 0 and r < len_s and s[l] == s[r]:
        l -= 1
        r += 1
    return l+1, r-1


# function to find all unique palindromes
def get_unique_palin(s):
    len_s = len(s)
    result = set()  # using set, so that only unique palindromes will be returned
    for i in range(len_s):
        l1, r1 = expand(s, i, i)
        l2, r2 = expand(s, i, i+1)

        # condition to avoid single letters in odd palindrome case
        if l1 != r1:
            result.add(s[l1:r1+1])

        # condition to check for even palindrome
        #  case
        if l2 < r2:
            result.add(s[l2:r2+1])

        # returns set as a list
    return list(result)


# run this code if this file is executed directley in the terminal
if __name__ == '__main__':
    string = input("Enter a Word: ")
    print(f"All unique palindromes are :{get_unique_palin(string)}")