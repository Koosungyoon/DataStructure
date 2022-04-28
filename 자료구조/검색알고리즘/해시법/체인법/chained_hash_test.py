from enum import Enum
from chained_hash import ChainedHash

Menu=Enum('Menu',['추가','삭제','검색','덤프','종료'])

def select_menu()->Menu:

    s=[f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n=int(input(": "))
        if 1<=n<=len(Menu):
            return Menu(n)
        

hash=ChainedHash(13)

while True:
    menu=select_menu()

    if menu==Menu.추가:
        Key=int(input('추가할 키를 입력하세요.: '))
        Val=input('추가할 값을 입력하시오: ')
        if not hash.add(Key,Val):
            print('추가를 실패했습니다!')

    elif menu==Menu.삭제:
        Key=int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(Key):
            print('삭제를 실패했습니다!')

    elif menu==Menu.검색:
        Key=int(input('검색할 키를 입력하세요.: '))
        t=hash.search(Key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print("검색할 데이터가 없습니다.")
    
    elif menu==Menu.덤프:
        hash.dump()
    
    else:
        break

