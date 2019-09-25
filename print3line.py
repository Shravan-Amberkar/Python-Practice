'''
Write a Python program that reads input
The input will consist of some number of lines of text. 
The input will be terminated by a blank line.
Your program should print every 3rd  line
'''

data=input()
l=[]
l.append(data)
while data:
    data=input()
    if data=="":
        break
    l.append(data)
for i in range(2,len(l),3):
    print(l[i])
