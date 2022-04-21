from typing import Any,Sequence
import sys

def bsearch(a:Sequence,key:Any)->int:
    
    pl=0
    pr=len(a)-1
    

    while True:
        pc=(pl+pr)//2
        if key==a[pc]:
            return pc
        elif key>a[pc]:
            pl=pc+1
        else:
            pr=pc-1
        if pl>pr:
            break
    return -1

if __name__ =='__main__':
    num=int(sys.stdin.readline().strip())
    X=[None]*num

    for i in range(num):
        X[i]=int(sys.stdin.readline().strip())
        
    print("검색할 키:")
    ky=int(sys.stdin.readline().strip())

    idx=bsearch(X,ky)

    if idx==-1:
        print("값이 존재 하지 않습니다!")
    else:
        print(f'검색값은 x[{idx}]에 있습니다')

