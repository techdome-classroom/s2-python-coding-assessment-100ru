class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_values[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    
    return total

# Test example
roman_number = "mcmxciv"  # Equivalent to 1994
print(f"The integer value of the Roman numeral '{roman_number}' is {roman_to_int(roman_number)}.")



