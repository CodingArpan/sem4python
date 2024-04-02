import re
word = "Hello... good morning <3"
p1 = re.sub(pattern='\w', repl='**', string=word)
print(p1)
