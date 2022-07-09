from typing import Any
from collections import deque

class Stack:
    #고정 길이 스택 클래스(collection.deque를 사용)

    def __init__(self,maxlen: int =256)-> None:
        #스택 초기화
        self.capacity=maxlen
        self.__stk=deque([],maxlen)
    
    def __len__(self)->int:
        #스택에 쌓여 있는 갯수 출력
        return len(self.__stk)

    def is_empty(self)->bool:
        #스택이 비어있는지 판단
        return not self.__stk

    def is_pull(self)->bool:
        #스택이 가득 차 있는지 판단
        return len(self.__stk)==self.__stk.maxlen
    
    def push(self,value:Any)->None:
        #스택에 value추가 
        self.__stk.appned(value)

    def pop(self)->Any:
        #스택에서 데이터를 팝
        return self.__stk.pop()

    def peek(self)->Any:
        #스택에서 데이터를 피크(가장 앞쪽 데이터 확인)
        return self.__stk[-1]

    def clear(self)->None:
        #스택 clear
        self.__stk.clear()
    
    #try except구문으로 -> 예외 구현 
    def find(self,value:Any)->Any:
        #스택에서 value를 찾아 인덱스를 반환(찾지 못하면 -1)
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self,value:Any)->int:
        return self.__stk.count(value)
    
    def __contain__(self,value:Any)->bool:
        return self.count(value)

    def dump(self)->int:
        #스택안에 있는 모든 데이터를 나열(바닥에서 꼭댜기 순으로 출력)
        print(list(self.__stk))

