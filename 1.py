from environment import *
from random_and_human import *
from mc import *
from ql import *

def vs(p1,p2,battle=1000): #対戦実行して、p1の勝利パーセントを出す
    game=Organizer(p1,p2)
    score=0
    for a in range(battle):
        t=game.progress(watch=False)
        if t==1:score+=1
    score=int((score/battle)*100)
    print("p1:",p1.name,":",score,"%","vs p2:",p2.name)

vs(Random_player(),Random_player()) #random vs random
vs(Random_player(),Mc()) #random vs mc
vs(Random_player(),Qlearning()) #random vs ql

vs(Mc(),Random_player()) #random vs mc
vs(Mc(),Mc()) #mc vs mc
vs(Mc(),Qlearning()) #mc vs pl

vs(Qlearning(),Random_player()) #random vs ql
vs(Qlearning(),Mc()) #ql(p1) vs mc(p2)
vs(Qlearning(),Qlearning()) #ql vs ql
