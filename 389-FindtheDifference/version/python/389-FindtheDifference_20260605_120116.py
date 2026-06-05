# Last updated: 6/5/2026, 12:01:16 PM
1class Solution:
2    def findTheDifference(self, s: str, t: str) -> str:
3        ans = 0
4        
5        # XOR ASCII values of all characters in s
6        for char in s:
7            ans ^= ord(char)
8            
9        # XOR ASCII values of all characters in t
10        for char in t:
11            ans ^= ord(char)
12            
13        # The remaining value is the ASCII code of the added letter
14        return chr(ans)
15