# -*- coding:utf-8 -*-
from sys import exit

def gold_room():
    print("This room is full of gold.How much do you take? 这里有一屋子的金子，你想拿走多少？")

    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number. 你的数学是体育老师教的吗？写数字！！")

    if how_much < 50:
        print("Nice, you're not greedy, you win! 你还不算太贪心，恭喜你可以带着黄金走了")
    else:
        dead("You greedy bastard! 你真是个贪心鬼！！！")


def bear_room():
    print("""
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of anther door.
How are you going to move the bear?
这里有一头大熊
它有一堆蜂蜜
这头肥熊正在另一扇门前挡着
你怎么赶走这头熊呢？
""")
    bear_moved = False

    while True:
        choice = input(">")

        if choice == "take honey" or choice == "拿走蜂蜜":
            dead("The bear looks at you then slaps your face off.哈哈，熊看了看你，然后拍扁了你的脑袋")
        elif choice =="taunt bear" or choice =="大吼一声" and not bear_moved:
            print("The bear has moves from the door.You can go though it now.熊从门口走开了，你可以通过了")
            bear_moved = True
        elif choice == "taunt bear" or choice =="大吼一声" and bear_moved:
            dead("The bear gets passed and chews your leg off.")
        elif choice == "open door" or choice == "开门" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.我不懂你想让我干嘛")

def cthulhu_room():
    print("""
Here you see the great evil Cthulhu.
He,it,whatever stares at you and you go insane.
Do you flee for your life or eat your head?
在这里有一个大恶魔
这个家伙正注视着你，你感到心慌了
你是要逃走，还是献上你的脑袋？
""")

    choice = input(">")
    if "flee" in choice or "逃" in choice:
        start()
    elif "head" in choice or "脑袋" in choice:
        dead("Well that was tasty! 嗯，很美味")
    else:
        cthulhu_room()

def dead(why):
    print(why,"Good job!")
    exit(100) #此处的参数使用0或者1或者其它数字有什么不同？

def start():
    print("""
You are in a dark room.
There a door to your right and left.
Which one do you take?
现在你在一个小黑屋里面
你的左右两边各有一扇门
你选择哪边的？
""")

    choice = input(">")

    if choice == "左边":
        bear_room()
    elif choice == "右边":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.你也可以不选择，四处转转等着饿死吧！")

start()
