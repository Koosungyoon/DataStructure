from typing import Any

class FixedStack:
    #고정 길이 스택 클래스
    class Empty(Exception):
        #비어 잇는 FixedStack에 팝 또는 피크할 떄 내보내는 예외 처리
        pass

    class Full(Exception):
        #가득 찬 FixedStack에 푸쉬 할 때 내보내는 예외 처리 
        pass
    
    def __init__(self,capacity:int=256)->None:
        #스택 초기화
        self.ptr=0
        self.capacity=capacity
        self.stk=[None]*capacity
    
    def __len__(self)->int:
        #스택에 쌓여 있는 테이터 개수 반환
        return self.ptr
    
    def is_empty(self)->bool:
        #스택에 데이터가 비어있는지 판단
        return self.ptr<=0
    
    def is_full(self)->bool:
        #스택에 데이커가 가득 차있는지 판단
        return self.ptr>=self.capacity     

    def push(self,value:Any)->None:
        #데이터를 추가합니다\
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr]=value
        self.ptr+=1
    
    def pop(self)->Any:
        #제일 위의 데이터를 반환합니다
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr-=1
        return self.stk[self.ptr]

    def peek(self):
        #스택세어 데이터를 피크 (꼭대기 데이터를 들여다봄)
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    
    def clear(self)->None:
        #스택을 비움 (모든 데이터 삭제)
        self.ptr=0

    def find(self,value:Any)->Any:
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i]==value:
                return i
        return -1
    
    def count(self,value:Any)->bool:
        cnt=0
        for i in range(self.ptr):
            if self.stk[i]==value:
                cnt+=1
        return cnt

    def __contains__(self,value:Any)->bool:
        return self.count(value)

    def dump(self)->None:
        if self.is_empty():
            print("스택이 비어있습니다.")
        else:
            print(self.stk[:self.ptr])
            