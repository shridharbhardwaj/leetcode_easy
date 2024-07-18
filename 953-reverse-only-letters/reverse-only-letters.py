class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s= list(s)
        left, right = 0, len(s)-1

        while left < right:
            while not s[left].isalpha() and left < right:
                left += 1
            while not s[right].isalpha() and left < right:
                right -= 1
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        
        return "".join(s)
        