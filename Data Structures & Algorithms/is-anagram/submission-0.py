class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for letter in s:
            if letter not in hashS:
                hashS[letter] = 0
            hashS[letter] += 1

        for letter in t:
            if letter not in hashT:
                hashT[letter] = 0
            hashT[letter] += 1

        return hashS == hashT