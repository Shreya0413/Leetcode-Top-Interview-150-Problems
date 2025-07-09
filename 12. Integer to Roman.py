class Solution:
    def intToRoman(self, num: int) -> str:
        i_to_r =  [(1000, 'M'), (900,'CM'), (500, 'D'), (400,'CD'), (100, 'C'),
           (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), 
           (5, 'V'), (4, 'IV'), (1, 'I')]
        r = ''
        for k,v in i_to_r: #k=value , v= symbol for example num=3749 value = 1000 so 1000<=3749 true then add the symbol to r and substract the value from there fore 3749-1000=2749 again from here same loop begins.
            while k <= num:
                r += v
                num -= k
        return r  
        
