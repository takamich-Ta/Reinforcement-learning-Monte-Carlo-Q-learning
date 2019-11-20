import random
import pickle
from environment import *
from random_and_human import *
from mc import *

class Qlearning: #Q-learningプレイヤー
    
    def __init__(self):
        self.name="ql"
        f=open("train_ql.pkl","rb") #学習済みデータを読み込む
        self.q_as = pickle._load(f)
        f.close()

    def train(self): #学習する,(status,action)に対応した配列を更新
        w=0.01 #学習率
        z=0.99
        finish_q_as_win=0.1 #勝って終了でのmaxQ(s,a)
        finish_q_as_lose=-0.1 #負けて終了でのmaxQ(s,a)
        status=random.randint(0,9)
        action=random.randint(1,2) #学習するために用意
        status,action,reward,next_status=self.train_data(status,action)
        if next_status==1000: #勝って終了の時の更新
            self.q_as[action - 1][status] = (1 - w) * self.q_as[action - 1][status] + w * (
            reward + z * finish_q_as_win) #maxQ(s,a)が計算できない
        elif next_status==500: #負けて終了の時の更新
            self.q_as[action - 1][status] = (1 - w) * self.q_as[action - 1][status] + w * (
                reward + z * finish_q_as_lose) #maxQ(s,a)が計算できない
        else: #相手の打ち手をQlearningで決定してmaxQ(s,a)を計算して更新
            if self.q_as[0][next_status]>self.q_as[1][next_status]:next_action=1
            else:next_action=2
            self.q_as[action-1][status]=(1-w)*self.q_as[action-1][status]+w*(reward+z*self.q_as[next_action-1][next_status])
            
    def reset(self): #学習リセット
        self.q_as=[[],[]]
        for a in range(10):
            self.q_as[0].append(random.randint(0,100)/100)
            self.q_as[1].append(random.randint(0, 100) / 100)

    def train_data(self,status,action): #更新に必要なデータが揃う
        if status==8 and action==1: #次の一手で勝てる
            reward=1
            next_status=1000
        elif status==9 and (action==2 or action==1):
            reward=1 #次の一手で勝てる
            next_status=1000
        elif status==8 and action==2:
            reward=0 #次の相手の一手で負ける
            next_status=500
        elif status==7 and action==1:
            reward=0 #次の相手の一手で負ける
            next_status=500
        elif status==7 and action==2:
            reward=0 #次の相手の一手で負ける
            next_status=500
        elif status==6 and action==1:
            reward=0 #次の相手の一手で負ける
            next_status=500
        else: #すぐにゲームは終わらないパターン
            reward=0
            next_status=self.next_status_get(status,action)
        return status,action,reward,next_status

    #次の自分のstatusを返す。学習用
    def next_status_get(self,status,action):
        if action==1:status_op=status+2 #2数選択
        if action==2:status_op=status+1 #1数選択
        if self.q_as[0][status_op]>self.q_as[1][status_op]:
            action_op=1 #qlで相手の一手を決定
        else:action_op=2
        if action_op == 1:next_status = status_op + 2
        if action_op == 2:next_status = status_op + 1
        return next_status #次の自分の状態がわかる

    def act(self,prenumber): #qlにより学習された配列をもとに行動
        if self.q_as[0][prenumber]>self.q_as[1][prenumber]:
            action=1
        else:action=2
        return action

ql=Qlearning()
ql.reset() #学習をリセット

for a in range(10000): #学習
    ql.train()

f=open("train_ql.pkl","wb") #パラメータを保存
pickle.dump(ql.q_as,f)
f.close()
