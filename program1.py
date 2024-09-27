class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching_parentheses = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_parentheses:  # It's a closing bracket
                top_element = stack.pop() if stack else '#'
                if matching_parentheses[char] != top_element:
                    return False
            else:
                stack.append(char)  # It's an opening bracket
        
        return not stack  # Stack should be empty if valid

# Example usage:
sol = Solution()
print(sol.isValid("()"))      # Output: True
print(sol.isValid("()[]{}"))  # Output: True
print(sol.isValid("(]"))      # Output: False







    



  

