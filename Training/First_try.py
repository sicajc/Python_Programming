
def palindrome(word):
    if word[0] != word[-1] :
        return False
    if len(word) <=2:
        return True
    
    return palindrome(word[1:-1])        


print("----------------Test_palindrome----------------")

s1 = "acbda"
print(palindrome(s1))

