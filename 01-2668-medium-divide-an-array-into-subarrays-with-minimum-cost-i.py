class Solution:
    def minimumCost(self, A: List[int]) -> int:
        for i in range(1, 3):
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    A[i], A[j] = A[j], A[i]
        return A[0] + A[1] + A[2]
