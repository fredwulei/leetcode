class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums = sorted(nums)
        length = len(nums)
        res = []
        for i in xrange(length-3):
            if nums[i] > target/4.0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in xrange(i+1,length-2):
                if nums[j] > (target-nums[i])/3.0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = length-1
                if nums[k] > (target-nums[i]-nums[j])/2.0:
                    continue
                if nums[l] < (target-nums[i]-nums[j])/2.0:
                    continue
                while k < l:
                    sum = nums[i]+nums[j]+nums[k]+nums[l]
                    # print nums[i], nums[j], nums[k], nums[l], sum
                    if sum == target:
                        a = (nums[i], nums[j], nums[k], nums[l])
                        res.append(a)
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        l -= 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sum > target:
                        l -= 1
                    else:
                        k += 1
        return res