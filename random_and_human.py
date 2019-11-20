import random

class Random_player: #randomプレイヤー
    def __init__(self):self.name="Random"
    def act(self,prenumber): #ランダムに選択する
        choose=random.randint(1,2) #prenumber=status
        return choose

class Human_player: #人間プレイヤー
    def __init__(self):self.name="Human"
    def act(self,prenumber): #入力を受け付ける
        while True: #prenumber=status
            print("opponent:",prenumber)
            print("1:",[prenumber+1,prenumber+2],"2:",[prenumber+1,0])
            choose=int(input("please input 1 or 2"))
            if choose==1 or choose==2:break
        return choose
