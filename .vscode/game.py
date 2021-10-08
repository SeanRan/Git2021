'''一个小游戏'''
#引入随机函数库
import random
answer = random.randint(1,10)
counts = 3

while counts > 0:
    temp = input("猜猜现在的数字是多少\n")
    guess = int(temp)

    if guess == answer:
        print("答对啦")
        break
    else:
        if guess < answer:
            print("小了哟\n")
        else:
            print('大了\n')
        counts -= 1
print("GAME OVER!")
