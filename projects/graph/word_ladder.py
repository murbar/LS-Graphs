# https://leetcode.com/problems/word-ladder/

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# recognize this is a graph problem
# comes from practice and intuition
# problem statement mentions "sequence", "relationships"
# often get graphs problems in interview setting,
# STEPS TO SOLVE(almost) ANY GRAPHS PROBLEM!
# * Translate the problem into graph terminology
# * Build your graph
# * Traverse your graph

# Looking for shortest path - indicates BFS
# Looking for sequence - need the BFS path
# word -> vertex
# one letter change -> edge

# 1. implement traversal
# 2. get neighbors


class Solution:
    def get_neighbors(self, word, word_list):
        neighbors = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        word_chars = list(word)

        for i in range(len(word_chars)):
            for l in letters:
                chars = word_chars.copy()
                chars[i] = l
                candidate = "".join(chars)

                if candidate != word and candidate in word_list:
                    neighbors.append(candidate)

        return neighbors

    def ladderLength(self, begin_word, end_word, word_list):
        word_set = set(word_list)
        visited = set()
        sequence_queue = []
        sequence_queue.append([begin_word])

        while sequence_queue:
            sequence = sequence_queue.pop(0)
            word = sequence[-1]

            if word not in visited:
                visited.add(word)

                if word == end_word:
                    return len(sequence)
                for n in self.get_neighbors(word, word_set):
                    s = sequence.copy()
                    s.append(n)
                    sequence_queue.append(s)

        return 0
