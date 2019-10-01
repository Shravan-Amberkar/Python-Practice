'''
Different Methods to take user input testcases
'''


for tc in range(int(input())):
    print (factorial(int(input())))
    
###############
testcase = int(input())
while(testcase):
    testcase-=1
    print (factorial(int(input())))
    
################
testcase = int(input())
for i in range(0, testcase):
    print (factorial(input()))
    
#################
t=10
while t>0:
    print(factorial(input()))
    t-=1
