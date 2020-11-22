import collections

def groupAnagrams(strs):
    grouped_anagrams = collections.defaultdict(list)
    for word in strs:
        grouped_anagrams[tuple(sorted(word))].append(word)
    return grouped_anagrams.values()
        


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
