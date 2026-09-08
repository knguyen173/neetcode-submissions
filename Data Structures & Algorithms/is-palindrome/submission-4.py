class Solution:
    def isPalindrome(self, s: str) -> bool:

        sNoSpace = re.sub(r"[^a-zA-Z0-9]", "", s)
        sNoSpace = sNoSpace.lower()
        left = 0
        right = len(sNoSpace) - 1
        
        while left < right:
            if sNoSpace[left] != sNoSpace[right]:
                print(sNoSpace[left])
                print(sNoSpace[right])
                return False
            else:
                left+=1
                right-=1
        
        return True