def subsets(nums):
    def subset_helper(nums,curr=[],res=[]):
        if nums == []:
            res.append(curr)
            return
        for i in range(len(nums)):
            subset_helper(nums[:i]+nums[i+1:],curr+[nums[i]],res)
        subset_helper(nums[:i]+nums[i+1:],curr,res)
        return res
    return subset_helper(nums)   
        
print(subsets([1,2,3]))
