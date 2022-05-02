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
        for i in range(self.capacity):
            if p.stat==Status.OCCUPIED and  p.key==key:
                return p
            elif p.stat==Status.EMPTY:
                break
            hash=self.rehash_value(hash)
            p=self.table[hash]

    def search(self,key:Any)->Any:
        p=self.search_node(key)
        if p is None:
            return None
        else:
            return p.value   

    #add 함수 수정 그리고  search 함수 구현 하기 
    def add(self,key:Any,value:Any)->bool:
        
        if self.search(key) is  not None:
            return False
        hash=self.hash_value(key)
        p=self.table[hash]
        for i in range(self.capacity):
            if  p.stat==Status.EMPTY or p.stat==Status.DELETE:
                self.table[hash]=Bucket(key,value,Status.OCCUPIED)
                return True
            #조건이 만족 하지 않는다면 ->재해시
            hash=self.rehash_value(hash)
            p=self.table[hash]
        return False
    
    def remove(self,key:Any)->bool:
        if self.search(key) is None:
            return False
        self.set_status(Status.DELETE)
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