class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sl=s.split()
        return len(sl[-1]) #it is used to return the last word split used to split the words and sl[-1] returns last word
        
