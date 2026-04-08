class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res, n = [], len(nums)
        for i in range(n):
            for j in range(i+1, n):
                l, r = j+1, n-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        quad = [nums[i], nums[j], nums[l], nums[r]]
                        if quad not in res:
                            res.append(quad)
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res