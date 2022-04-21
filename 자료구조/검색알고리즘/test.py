'''
해시법을 사용하는데 해시 충돌이 일어나는 경우 ->  체인법(오픈 해시법) 으로 해결 
'''
from __future__ import annotations
from logging import captureWarnings
from re import A
from typing import Any, Type
import hashlib

class Node:
    # 해시를 구성하는 노드

    def __init__(self,Key:Any, Value:Any, Next: Node) ->None:
        self.Key=Key #키
        self.Value=Value #값
        self.Next=Next #뒤쪽 노드 참조

class ChainedHash:
    #체인법으로 해시 클래스 구현

    def __init__(self,capacity:int)->None:
        self.capcity=capacity   #해시테이블 크기 지정
        self.table=[None]*self.capcity  #해시테이블(리스트)선언

    def hash_value(self,Key:Any)->int:
        if isinstance(Key,int): #정수이면 -> 나눠서 해쉬값 리턴
            return Key%self.capcity
        return (int(hashlib.sha256(str(Key).encode()).hexdigest(),16)%self.capcity)

    '''
    search()함수 구현
    1.해시함수를 사용하여 키를 해시값으로 변환
    2.해시값을 인덱스로 하는 버킷에 주목
    3.버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 스캔 -> 키와 같은 값이 발견되면 검색 성공, 맨끝에 도달했는데도 못찾으면 실패
    '''
    def search(self,Key:Any)->Any:

        hash = self.hash_value(Key)
        p=self.table[hash] #해시 값을 인덱스로 하는 버킷임!!!

        while p is not None: #버킷이 None이 아니면 실행
            if p.Key==Key:   #버킷이 참조하는 수가 지금 찾고자 하는 키와 같은면 그 노드의 Value값을 리턴
                return p.Value
            p=p.Next

        return None          #만약 존재 하지 않으면 None 리턴
    
    def add(self,Key:Any, Value:Any)->bool:
        
        hash=self.hash_value(Key)
        p=self.table[hash]

        while p is not None:
            if p.Key==Key:
                return False #이미 존재하는 값을 추가하므로 실패 임 
            p=p.next
        
        temp = Node(Key,Value,self.table[hash])
        self.table[hash]= temp
        return True

    '''
    일단 삭제하고자 하는 키값을 입력 받고 그놈의 해시값의 버킷에 주목하여 
    건너 뛰어서 참조하면 된다
    즉, 삭제하고자 하는 값의 이전노드에 삭제하고자 하는 값이 참조하는 것을 대입
    '''
    def remove(self, Key:Any)->bool:
        
        hash = self.hash_value(Key) #키의 해시값 구함
        p=p.table[hash]             #해당하는 버킷을 주목
        pp=None                     #이전 노드 주목
        while p is not None:
            if p.Key==Key:
                if pp is None:  #이전의 노드가 해시테이블 이라면 ! 
                    self.table[hash]=p.next
                else:
                    pp.next=p.next
                return True 
            pp=p
            p=p.next
        return False

    def dump(self)->None:
        for i in range(self.capcity):
            p=self.table[i]
            print(i,end='')
            while p is not None:
                print(f'->{p.Key} ({p.Value})',end='')
                p=p.next
            print()

            



                    
