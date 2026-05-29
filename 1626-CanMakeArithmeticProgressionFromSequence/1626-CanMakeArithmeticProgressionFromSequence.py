# Last updated: 5/29/2026, 3:34:42 PM
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        
        return True


# Create object
sol = Solution()

print(sol.canMakeArithmeticProgression([3, 5, 1]))  # True
print(sol.canMakeArithmeticProgression([1, 2, 4]))  # False