# program to check string is palindrome

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("nitin"))
print(is_palindrome("suman"))
