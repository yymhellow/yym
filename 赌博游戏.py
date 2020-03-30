# @Time    : 2020/3/30 10:44 上午
# @Author  : yym
# @Site : 
# @File    : 程序逻辑.py
# @Software: PyCharm
from random import randint
money = 1000        #假设有1000元
while money > 0:
    print(f"你的资产有{money}")
    next_game = False
    while True:
        debt = int(input("请下注"))
        if 0 < debt <= money:
            break
        else:
            print(f"你只有{money},请重新下注")
    num = randint(1,6) + randint(1,6)               #摇骰子
    print(f"开始摇骰子，点数为{num}")
    if num==7 or num==11:
        money += debt
        print(f"玩家胜利，获得{debt}元，现有{money}")
    elif num==2 or num==3 or num==12:
        money -= debt
        print(f"庄家胜利，减去{debt}元，现在有{money}")
    else:
        next_game = True
        while next_game:
            next_game = False
            num2 = randint(1,6) + randint(1,6)
            print(f"开始重新摇骰子,点数为{num2}")
            if num2 == 7:
                money -= debt
                print(f"庄家获胜，减去{debt}，现在还有{money}")
            elif num2 == num:
                money += debt
                print(f"玩家胜利，获得{debt}元，现有{money}")
            else:
                next_game = True

print("你没钱了，游戏结束")
