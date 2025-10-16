def picture():
    pic=[f"{f1:^8}{g1:^8}{c1:^8}","------------------------",f"{b1:^24}",
         f"{b2:^24}","------------------------",f"{f2:^8}{g2:^8}{c2:^8}"]
    #用列表将每一行各个物品的位置储存
    for i in pic:
        print(i)

def get_input():
    global f1,f2,g1,g2,c1,c2,b1,b2
    global condition
    if b1=="":
        pos="near"
    else:
        pos="far"
    item=input(f"You are now at the {pos} shore, what do you want to take? ")
    print()
    if item=="g" and (g1==b1 or b2==g2):
        g1,g2=g2,g1#将输入的物品（如果有的话）还有船交换位置
        b1,b2 = b2,b1
    elif item=="c" and (b1==c1 or b2==c2):
        c1,c2=c2,c1
        b1,b2 = b2,b1
    elif item=="f" and (b1==f1 or b2==f2):
        f1,f2=f2,f1
        b1,b2 = b2,b1
    elif item=="m":
        b1,b2 = b2,b1
    elif item=="q":
        print("Thank you for playing!")
        print("see you next time!^ ^")
        condition = 1
    else:
        print("You have entered an invalid command.")
        print("please try again")
def win_lose():
    global condition
    if (b1=="" and f2==g2=="") or (b2=="" and f1==g1==""):#当人不跟fox和goose在一起的情况
        print("You have failed.")
        print("Your fox has eaten your goose.")
        condition = 1
    elif (b1=="" and g2==c2=="") or (b2=="" and g1==c1==""):#当人不跟corn和goose在一起的情况
        print("You have failed.")
        print("Your goose has eaten your corn.")
        condition = 1
    elif f2==g2==c2==b2:
        print("Congratulations!")
        print("You have brought all the items across the river.")
        condition = 1
    else :
        pass

def start():
    print("Welcome.")
    print("You must bring the fox, the goose, and the corn across the river.")
    picture()
    get_input()

f1,g1,c1,b1="","","",""#表示为空，也就是没有物品
#1:表示河对岸各个物品的状态
f2,g2,c2,b2="Fox","Goose","Corn","Boat"
#2：原岸各个物品的状态
condition=0 #用来判断游戏有没有结束
start()
while condition==0:
    picture()
    win_lose()
    if condition==0:
        get_input()


