class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            # Get value of current symbol
            curr_value = roman_map[s[i]]

            # Check if there's a next symbol and it's larger
            if i + 1 < len(s) and curr_value < roman_map[s[i + 1]]:
                total -= curr_value  # Subtract if smaller than next
            else:
                total += curr_value  # Otherwise, add it

        return total
