class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        index=0
        partial_string=""
        list_of_combinations=[]
        mapping={"2":"abc","3":"def","4":"ghi","5":"jkl",6:"mno",7:"pqrs",9:"tuv",0:"wxyz"}
        def helper(digits,index,partial_string,list_of_combinations,mapping):
            if index == len(digits):
                list_of_combinations.append(partial_string)
                return
            for letter in mapping[digits[index]]:
                helper(digits,index+1,partial_string+letter,list_of_combinations,mapping)
        helper(digits,index,partial_string,list_of_combinations,mapping)
        return list_of_combinations

        