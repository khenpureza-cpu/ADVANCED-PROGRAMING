# Activity 7: Regular expression
import re
text = input()

numbers = re.findall(r'\d', text)
print(numbers)
words = re.findall(r'[a-zA-Z]+', text)
print(words)
