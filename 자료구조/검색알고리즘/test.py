#1000이하 소수 구하는 프로그램 !
'''
import sys

space=[None]*500
num=0
space[0]=2
num+=1


#i가 i이하의 소수로 나누어 떨어지지 않으면 소수에 추가!
for i in range(3,1001,2):
    for j in range(1,num):
        if i %space[j]==0:
            break
    else:
        space[num]=i
        num+=1

print(space)
'''
# 알고리즘 개선

# n의 제곱근 이하의 소수로 나누어 떨어지지 않으면 소수에 추가!
space=[None]*500
num=0
space[num]=2
num+=1
space[num]=3
num+=1

for i in range(5,1001,2):
    j=1
    while space[j]*space[j]<=i: #i의 제곱근 보다 작은 소수일 동안 실행 
        if i%space[j]==0:
            break
        j+=1
    else:
        space[num]=i
        num+=1

print(space)

