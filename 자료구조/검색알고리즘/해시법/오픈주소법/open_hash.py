from __future__ import annotations
from typing import Any,Type
from enum import Enum
import hashlib

class Status(Enum):
    OCCUPIED=0
    EMPTY=1
    DELETE=2

class Bucket:

    def __init__(self,key:Any=None,value:Any=None,stat:Status=Status.EMPTY)->None:
        self.key=key
        self.value=value
        self.stat=stat
    
    def set(self,key:Any,value:Any,stat:Status)->None:
        self.key=key
        self.value:value
        self.stat=stat

    def set_status(self,stat:Status)->None:
        self.stat=stat

class Openhash:
    def __init__(self,capacity:int)->None:
        self.capacity=capacity
        self.table=[Bucket()]*capacity
    
    def hash_value(self,key:Any)->int:
        if isinstance(key,int): #정수이면 -> 나눠서 해쉬값 리턴
                return key%self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(),16)%self.capcity)

    #재해시 
    def rehash_value(self,key:Any)->int:
       return (self.hash_value(key)+1)%self.capacity
    
    def search_node(self,key:Any)->Any:
        hash=self.hash_value(key)
        p=self.table[hash]
        for i in range(self.capacity): #버킷을 일일이 다 돌아봅!
            if p.stat==Status.OCCUPIED and  p.key==key: #찾았다면 p가 참조하고 있는 버킷을 리턴
                return p
            elif p.stat==Status.EMPTY:                  #그렇지 않다면 탈출
                break
            hash=self.rehash_value(hash)                #만약 찾는 키의 해시값이 가지는 버킷의 속성이 occupied가 아니라면
            p=self.table[hash]                          #재해시

    #탐색하고자 하는 키의 값을 리턴해준다
    def search(self,key:Any)->Any:
        p=self.search_node(key)
        if p is None:
            return None
        else:
            return p.value   

    #add 함수 수정 그리고  search 함수 구현 하기 
    def add(self,key:Any,value:Any)->bool:
        
        if self.search(key) is  not None:           #추가하고자 하는 녀석이 있다면 실패
            return False
        hash=self.hash_value(key)
        p=self.table[hash]
        for i in range(self.capacity):
            if  p.stat==Status.EMPTY or p.stat==Status.DELETE:
                self.table[hash]=Bucket(key,value,Status.OCCUPIED) #키와 값을 추가하고 상태=occupied
                return True                        
            hash=self.rehash_value(hash)            #추가하고자 하는 녀석이 없지만 버킷이 occupied상태라면 
            p=self.table[hash]                      #재해시를 통해서 빈곳에 추가한다
        return False
    
    def remove(self,key:Any)->bool:
        if self.search(key) is None:                #삭제하고자 하는 버킷이 이미 비어있으면 실패
            return False
        self.set_status(Status.DELETE)              #상태만 delete속성 부여
        return True

    def dump(self)->None:
        for i in range(self.capacity):
            print(f'{i:2}',end=' ')
            if self.table[i].stat==Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat==Status.DELETE:
                print('----delete----')
            else:
                print('----empty---')