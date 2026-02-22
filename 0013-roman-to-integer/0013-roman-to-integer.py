class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in s:
            value = roman_numerals[char]
            if prev_value < value: 
                # If the previous value is less than the current value, 
                # it means we have a subtractive combination (e.g., IV, IX, etc.)
                # We need to subtract the previous value from the total and add the current value.
                total += value - 2 * prev_value # IV : 5 - 2*1 = 3, IX : 10 - 2*1 = 8
            else:
                total += value
            prev_value = value

        return total
    