class Solution:
	def calculate(self, s):
		stack = []
		curr = 0
		op = "+"
		for i in range(0, len(s)):
			if s[i].isdigit():
				curr = curr*10 + ord(s[i]) - ord("0")
			if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
				if op == "-":
					stack.append(-curr)
				elif op == "+":
					stack.append(curr)
				elif op == "*":
					stack.append(stack.pop()*curr)
				else:
					temp = stack.pop()
					if temp//curr < 0 and temp%curr != 0:
						stack.append(temp//curr + 1)
					else:
						stack.append(temp//curr)
				op = s[i]
				curr = 0
		return sum(stack)