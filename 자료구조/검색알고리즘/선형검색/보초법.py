'''
선형검색의 종료조건은 두가지인데,
1.찾고자 하는 key가 존재하거나
2.찾고자 하는 key가 존재하지 않아 실패하거나
보초법은 key를 맨 뒤배열에 추가함으로써 종료조건 2를 판단하지 않아도 된다! '''


import sys
from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a=copy.deepcopy(seq)
    a.append(key)
    
    i=0
    while True:
        if a[i]==key:
            break
        i+=1
    return -1 if i==len(seq) else i #존재는 하나 주목하고 있는 인덱스가 보초자리(마지막 인덱스)인가 판단 O->-1 X->i

if __name__ =='__main__':
    num=int(sys.stdin.readline().strip())
    X=[None]*num
    for j in range(num):
        X[j]=int(sys.stdin.readline().strip())

    print("검색할 키:" )
    ky=int(sys.stdin.readline().strip())
    idx=seq_search(X,ky)

    if idx==-1:
        print("값이 존재 하지 않습니다!")
    else:
        print(f'검색값은 x[{idx}]에 있습니다')

