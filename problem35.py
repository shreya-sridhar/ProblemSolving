# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.

# Note:

# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Test Cases:
# wordList = ["hot","dot","dog","lot","log","cog"]
# 1. beginWord = "hit", endWord = "cog" -> 5
# 2. beginWord = "hat", endWord = "zar" -> 0
# 3. wordList = [], beginWord = "hit", endWord = "cog" -> 0
# 4. wordList = ["hat"] beginWord = "hit", endWord = "cog" -> 0  beginWord = "cat", endWord = "hat" -> 2
# 5. wordList = ["too","top","cop"]  ,beginWord = "moo", endWord = "coo" -> 5, beginWord = "moo", endWord = "poo" -> 0

# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# brute -> hit dot cog n = 1
# o(nm) + o(mn^2) + o(n^3) + .. + -> o(n^n/2) 

# 1. start with beginWord
# 2. define another function inputy of 2 words - word_diff - 0/1
# 3. run a loop over all dict elements and create a mapping hash from beginWord to all other dict words where word_diff == 1  (map[beginWord] = []) -> if map[beginWord] is empty return False
# 4. run through every 2 elements dictionary using loops i,j map[i] = [j,k...]
# 5. check if path exists using bfs from begin to end word -> increment length 

# time -> i,j (n^2 + nlogn) -> n^2

# map = {hit:[],hot :[],...}

# hit >  h_t map.keys[0] == 'h' and 
#        _it 
#        hi_

from collections import deque
import string

def shortest_transformation(beginWord, endWord, wordList):
    def mapping(beginWord, endWord, wordList):
        dict_map = {}
        for word in wordList :
            dict_map[word] = []
        dict_map[beginWord] = []
        for word in wordList + [beginWord] :
            for index in range(len(word)) :
                for letter in string.ascii_lowercase:
                    temp_word = word[:index]+ letter +word[index+1:]
                    if temp_word in dict_map and temp_word != word:
                        dict_map[word].append(temp_word)
        return dict_map

    def bfs(beginWord, endWord, dict_map):
        if not dict_map:
            return 0
        q = deque()
        level = 1
        q.append(beginWord)
        q.append(None)
        is_visited = [beginWord, None]
        while len(q) > 1:
            popped_ele = q.popleft()
            if popped_ele == None:
                level += 1
                q.append(None)
            else:
                for neighbor in dict_map[popped_ele]:
                    if neighbor == endWord:
                        return level+1
                    if neighbor not in is_visited:
                        q.append(neighbor)
                        is_visited.append(neighbor)
        return 0            
    dict_map = mapping(beginWord, endWord, wordList)
    return bfs(beginWord, endWord, dict_map)


wordList = ["hot","dot","dog","lot","log"]
beginWord = "hit"
endWord = "cog"
print(shortest_transformation(beginWord,endWord,wordList))


# 2. beginWord = "hat", endWord = "zar" -> 0
# 3. wordList = [], beginWord = "hit", endWord = "cog" -> 0
# 4. wordList = ["hat"] beginWord = "hit", endWord = "cog" -> 0  beginWord = "cat", endWord = "hat" -> 2
# 5. wordList = ["too","top","cop"]  ,beginWord = "moo", endWord = "coo" -> 5, beginWord = "moo", endWord = "poo" -> 0





