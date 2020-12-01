# def subsets(nums):
#     subset_array = [[]]
#     for ele in nums:
#         subset_array += [subset + [ele] for subset in subset_array]
#     return subset_array

# res -> List[list] : list of subsets
# nums -> array : list of numbers
# subset -> list : contains elements already processed 
# index -> int : position of element in nums to process

def subsets2(nums, pre_subset, index,res):
    for i in range(index,len(nums)):
        pre_subset.append(nums[i])
        res.append(pre_subset[:])
        subsets2(nums,pre_subset,i+1,res)
        pre_subset.pop()
    return res

def subsets3(nums):
    all_subsets = []
    for i in range(0,2**len(nums)):
        subset = []
        index = 0
        while i:
            j = 1 << index
            if (i & j) != 0:
                subset += [nums[index]]
                i -= j
            index +=1
        all_subsets.append(subset)
    return all_subsets

nums = [1,2,3]
# print(subsets(nums))
pre_subset = []
index = 0
res = [[]]
# print(subsets2(nums, pre_subset,index,res))
print(subsets3(nums))

