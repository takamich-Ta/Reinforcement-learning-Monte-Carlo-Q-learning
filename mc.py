import random
import pickle
from environment import *
from random_and_human import *

class Mc: #モンテカルロプレイヤー
    def __init__(self):self.name="MC"
    def trial(self,prenumber): #ランダム対戦一回実行
        p1=Random_player()
        p2=Random_player()
        t=Organizer(p1,p2) #prenumber=status
        win=t.progress(prenumber,watch=False)
        if win==1:return 1
        else:return 0

    def act(self,prenumber): #順番が来るたびに行動評価
        count=100 #ランダム対戦回数 #prenumber=status
        point1=0
        if prenumber<8:
            for a in range(count): #2数選択をしたとする
                point1+=self.trial(prenumber+2)
        if prenumber==8:return 1 #2数選択で勝ち
        if prenumber==9:return 2 #1数選択で勝ち
        if count-point1>=count/2:return 1
        else:return 2 #1:2数選択,2:1数選択
