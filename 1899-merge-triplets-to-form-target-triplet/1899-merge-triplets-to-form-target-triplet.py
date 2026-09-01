class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = False

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                a |= x == target[0]
                b |= y == target[1]
                c |= z == target[2]

        return a and b and c