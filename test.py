#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import random
from NeuronNet import NeuroNet as nn
import game as g
Actions = np.array([0, 1, 2, 3])

def getAction(Card1, Card2):
    action = 0
    val = float(Card1* Card2)/196.0
    if val > 0.75:
        action = 3
    elif val > 0.50:
        action = 2
    elif val > 0.25:
        action = 1

    if random.randint(0, 4) == 0:
        action += 1
    elif random.randint(0, 4) == 1 and action != 0:
        action -= 1

    return action


Deck = np.array(["2h", "2d", "2c", "2s", 
                "3h", "3d", "3c", "3s", 
                "4h", "4d", "4c", "4s", 
                "5h", "5d", "5c", "5s", 
                "6h", "6d", "6c", "6s",
                "7h", "7d", "7c", "7s", 
                "8h", "8d", "8c", "8s", 
                "9h", "9d", "9c", "9s", 
                "10h", "10d", "10c", "10s", 
                "Jh", "Jd", "Jc", "Js", 
                "Qh", "Qd", "Qc", "Qs", 
                "Kh", "Kd", "Kc", "Ks", 
                "Ah", "Ad", "Ac", "As"])


DeckVal = np.array([2, 2, 2, 2, 
                    3, 3, 3, 3, 
                    4, 4, 4, 4, 
                    5, 5, 5, 5, 
                    6, 6, 6, 6,
                    7, 7, 7, 7, 
                    8, 8, 8, 8, 
                    9, 9, 9, 9, 
                    10, 10, 10, 10, 
                    11, 11, 11, 11, 
                    12, 12, 12, 12, 
                    13, 13, 13, 13, 
                    14, 14, 14, 14])


CurDeck = np.copy(DeckVal)

pl1_Card1 = 0.0
pl1_Card2 = 0.0
pl1_Stack = 100.0

pl2_Card1 = 0.0
pl2_Card2 = 0.0
pl2_Action = 0
pl2_Stack = 100.0

inputData = np.array([[pl1_Card1, pl1_Card2, pl2_Action]])
neuro = nn()
for j in xrange(60000):
	#print("================================================================")  
	np.random.shuffle(CurDeck)
	pl1_Card1 = CurDeck[0]
	pl1_Card2 = CurDeck[1]
	pl1_Action = 0

	pl2_Card1 = CurDeck[3]
	pl2_Card2 = CurDeck[4]
	pl2_Action = getAction(pl2_Card1, pl2_Card2)
	#print(pl1_Card1, pl1_Card2)

	# for a in xrange(4):
	res = 0
	pl1_Action = 0
	y = g.WinCond(pl1_Card1, pl1_Card2, pl2_Card1, pl2_Card2)
	inputData = np.array([[pl1_Card1, pl1_Card2]])
	#wr = int(round(neuro.SpotResult(inputData, y), 2) * 100)
	wr = neuro.SpotResult(inputData, y)
	if wr > 0.5:
		pl1_Action = 1
	if y == 1:
		res = pl1_Action
	else:
		res = -pl1_Action

    #neuro.QLearnUpdate(wr, res)

	if (j - 59900) > 0:
		pl1_Stack += res
		pl2_Stack -= res
		print("=============================================================================")
		print(res)
		print(pl1_Card1, pl1_Card2, pl1_Action, pl1_Stack)
		print(pl2_Card1, pl2_Card2, pl2_Action, pl2_Stack)
	#print(neuro.Qgl)
