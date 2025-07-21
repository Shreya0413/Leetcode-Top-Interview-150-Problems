from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
         merged = ""
         for a, b in zip_longest(word1, word2, fillvalue=""):
            merged += a + b
         return merged

        
