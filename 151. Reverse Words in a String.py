class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        rev_words=words[::-1]
        reverse_str=' '.join(rev_words)
        return(reverse_str)

        
