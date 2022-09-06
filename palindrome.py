#Problem: Palindrome
#Description: Check to see if a given number is a palindrome

def isPalindrome(self, x: int) -> bool:
        testNum = ""
        isPalindrome = False
        for char in reversed(str(x)):
            testNum += char
        
        if testNum == str(x):
            isPalindrome = True
        
        return isPalindrome
