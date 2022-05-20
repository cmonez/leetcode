class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element == "+":
                result = stack.append(stack.pop() + stack.pop())
            elif element == "-":
                last_el, second_to_last_el = stack.pop(), stack.pop()
                result = stack.append(second_to_last_el - last_el)
            elif element == "*":
                result = stack.append(stack.pop() * stack.pop())
            elif element == "/":
                last_el, second_to_last_el = stack.pop(), stack.pop()
                result = stack.append(int(second_to_last_el / last_el))
            else:
                stack.append(int(element))

        return stack[0]

        
# iterate through the list
# if the current element is num
# add to the stack
# if its an operator
# pop the last two elements
# do the operator on them
# pop back into the stack
# return the element
        