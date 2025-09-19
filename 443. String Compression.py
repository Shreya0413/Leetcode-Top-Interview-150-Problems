class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Pointer to write the compressed string
        read = 0   # Pointer to read through the original array
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count the number of occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character to the write position
            chars[write] = char
            write += 1
            
            # If the character count is more than 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
