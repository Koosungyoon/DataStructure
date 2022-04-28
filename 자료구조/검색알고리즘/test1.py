#해시법 체인드 해시법을 구현한다
'''
node라는 클래스를 정의 한다! 키,밸류,노드(다음 노들르 참고해야함!)
체인드해시 클래스는 주어진다.
    1.해시테이블 선언
    2.해시값을 리턴해주는 함수! -> 해시값은 키를 테이블의 크기로 나눈 나머지를 말한다.
    ===구현 할 것===
    #키를 통해서 밸류를 찾아주는 함수
    #키와 밸류로 새롭게 해시테이블에 추가해주는 함수
    #키를 통해 해시테이블에서 삭제해주는 함수
    #해시테이블을 출력해주는 함수
'''
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self,key:Any,value:Any,next:Node)->None:
        self.key=key
        self.value=value
        self.next=next

class ChainedHash:
    #체인법으로 해시 클래스 구현

    def __init__(self,capacity:int)->None:
        self.capcity=capacity   #해시테이블 크기 지정
        self.table=[None]*self.capcity  #해시테이블(리스트)선언

    def hash_value(self,Key:Any)->int:
        if isinstance(Key,int): #정수이면 -> 나눠서 해쉬값 리턴
            return Key%self.capcity
        return (int(hashlib.sha256(str(Key).encode()).hexdigest(),16)%self.capcity)

    def search(self,key:Any)->Any:
        hash=self.hash_value(key)
        p=self.table[hash]

        while p is not None:
            if p.key==key:
                return p.value
            p=p.next
        return None
    
    '''
    추가하고자 하는 값이 이미 존재한다면 실패!
    '''
    def add(self,key:Any,value:Any)->bool:
        hash = self.hash_value(key)
        p=self.table[hash]
        #추가하고자 하는 값이 있는지 확인하기 위함
        while p is not None:
            if p.key== key:
                return False
            p=p.next
        
        temp=Node(key,value,self.table[hash])#지금 self.table[hahs]는 초반에 있는 50줄의 저 것이다! 이 것 이 참조하는 것은 추가하기 이전의 해시테이블의 다음 참조하는 놈이고 
        self.table[hash]=temp #이렇게 대입함으로써 추가한 것의 참조하는 다음 값은 추가 이전의 self.table[hahs]가 참조하는 값이다! 
        return True

    def remove(self,key:Any)->bool:
        hash=self.hash_value(key)
        p=self.table[hash]
        pp=None  #바로 앞의노드 

        while p is not None:
            if p.key==key:
                if pp is None:
                    self.table[hash]=p.next
                else:
                    pp.next=p.next
                return True
            pp=p.next
            p=p.next
        return False

    def dump(self)->None:
        for i in range(self.capcity):
            p=self.table[i]
            print(i)
            while p is not None:
                print(f'{p.key}({p.value})')
                p=p.next



    