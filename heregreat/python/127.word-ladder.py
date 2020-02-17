#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
import collections
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList or not wordList):
            return 0
        all_comb_dict = defaultdict(list)
        L = len(wordList[0])
        for word in wordList:
            for i in range(L):
                all_comb_dict[word[:i] + '*' + word[i + 1:]].append(word)
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord:True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                for word in all_comb_dict[intermediate_word]:
                    if(word == endWord):
                        return level + 1
                    if(word not in visited):
                        visited[word] = True
                        queue.append((word, level + 1))
                all_comb_dict[intermediate_word] = []
        return 0
# @lc code=end

