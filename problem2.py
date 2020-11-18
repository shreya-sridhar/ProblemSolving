from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping=defaultdict(list)
        for index,number in enumerate(nums):
            mapping[number].append(index)
        for first_num,first_index_list in mapping.items():
            second_num=target-first_num
            if second_num in mapping and (first_index_list[0]!=mapping[second_num][0] or len(mapping[second_num])>1):
                second_index = mapping[second_num][0] if first_index_list[0]!=mapping[second_num][0] else mapping[second_num][1]
                first_index=first_index_list[0]
                return [first_index,second_index]
            
                                                