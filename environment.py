import random
import pickle

#環境#10言ったら勝ちゲーム、数字2個まで言える

class Game: #ゲームを定義 #選択肢返す、勝利判定する
    def __init__(self):
        self.board=[]
        self.prenumber=0 #prenumber=status
        self.player_turn=1
        self.winner=0
    def canchoose_number(self): #選べる行動を返す
        canchoose=[[],[]]
        canchoose[0].append(self.prenumber+1)
        canchoose[1].append(self.prenumber+1)
        canchoose[0].append(self.prenumber + 2)
        canchoose[1].append(0)
        return canchoose

    #どっちが勝ったか判断 #watchは画面に結果見せるかどうか
    def check_win(self,choose_number,watch=True):
        if choose_number==[9,10] or choose_number==[10,0] or choose_number==[10,11]:
            if self.player_turn==1:
                self.winner=1
                if watch==True:print("player1:Win")
            if self.player_turn==2:
                self.winner=2
                if watch==True:print("player2:Win")
    def choose(self,choose_12): #1,2で選択。次のprenumber返す
        canchoose=self.canchoose_number()
        if choose_12==1: #input=1:2数選択
            self.prenumber = max(canchoose[0])
            return canchoose[0]
        if choose_12==2: #input=2:1数選択
            self.prenumber = max(canchoose[1])
            return canchoose[1]

class Organizer: #進行役、プレイヤーに環境に触らせない
    def __init__(self,p1,p2): #inputはプレイヤーのクラス
        self.p1_name=p1
        self.p2_name=p2
    def progress(self,t=0,watch=True): #ゲーム進行
        game=Game() #tの値で好きなところから始められる
        game.prenumber=t #prenumber=status
        while game.winner==0: #act:プレイヤーの行動
            choose_p1=self.p1_name.act(game.prenumber)
            choose_p1=game.choose(choose_p1)
            game.check_win(choose_p1,watch)
            if game.winner==1:break
            game.player_turn=2
            choose_p2 = self.p2_name.act(game.prenumber)
            choose_p2 = game.choose(choose_p2)
            game.check_win(choose_p2,watch)
            if game.winner==2:break
            game.player_turn=1
        return game.winner
