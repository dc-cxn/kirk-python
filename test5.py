#!/usr/bin/env python

with open("file1.py": encoding="utf-8") as f:
    output = f.read()
    
print(output)


with open("new file3.py", mode="w") as w:
    output = w.write("replaced and destroyed file\n")
    
print (output)

