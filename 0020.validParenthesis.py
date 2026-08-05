class Solution:
    def validParenthesis(self, s: str) -> bool:

        a = []

        for i in range(len(s)): # iterate through each character in the string
            if s[i] == '(' or s[i] == '[' or s[i] == '{': # if the character is an opening bracket, push it onto the stack
                a.append(s[i])

            else:
                if not a: # If the stack is empty, return False, because there is no matching opening bracket for the closing bracket
                    return False

                top = a.pop() # pop the top element from the stack, which is the last opening bracket that was added


                # check if the popped element matches the current closing bracket. If it doesn't match, return False
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False

            return len(a) == 0 # After iterating through the entire string, if the stack is empty, it means that all opening brackets have been matched with their corresponding closing brackets, and we return True. If the stack is not empty, it means there are unmatched opening brackets, and we return False.