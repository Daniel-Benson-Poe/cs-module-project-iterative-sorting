# Write a recursive solution to determine if a string is a valid palindrome. 
# A palindrome is a word that reads the exact same backwards as it does forwards, 
# like "racecar" for example. If the word is a valid palindrome, it should return 
# True, otherwise it should return False.

# Casing can be ignored, so "RaCeCAr" should still return True.

# None recursive solution:
def is_palindrome(x_string):
    return x_string.lower() == x_string[::-1].lower()

if __name__ == "__main__":
    print(is_palindrome("racecar"))
    print(is_palindrome("RaCeCAr"))
    print(is_palindrome("palindrome"))