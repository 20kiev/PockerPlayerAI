#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import random
from NeuronNet import NeuroNet as nn
import game as g
Actions = np.array([0, 1, 2, 3, 4, 5])

inputData = np.array([[0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0,  
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0]])

def getAction(Hand):

	c1 = g.GetCardId(Hand[0])
	c2 = g.GetCardId(Hand[1])

	action = 0
	val = float(c1 + c2)/100.0
	if val > 0.80:
		action = 5
	elif val > 0.70:
		action = 4
	elif val > 0.60:
		action = 3
	elif val > 0.40:
		action = 2
	elif val > 0.20:
		action = 1
	return action

def predictAction(Hand):
	val = g.getHandValue(Hand)

	if val > g.FullHouseVal:
		action = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])
	elif val > g.StraightVal:
		action = np.array([[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]])
	elif val > g.ThreeVal:
		action = np.array([[0.0, 0.0, 0.0, 1.0, 0.0, 0.0]])
	elif val > g.TwoPairsVal:
		action = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0]])
	elif val > g.PairVal:
		action = np.array([[0.0, 1.0, 0.0, 0.0, 0.0, 0.0]])
	else:
		action = np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

	return action

CurDeck = np.copy(g.Deck)

pl1_Hand = np.array(["  ", "  "])
pl1_Stack = 100.0

pl2_Hand = np.array(["  ", "  "])
pl2_Action = 0
pl2_Stack = 100.0
#inputData = np.array([[pl1_Hand, pl2_Hand, pl2_Action]])
neuro = nn()
for j in xrange(60000):
	#print("================================================================")  
	np.random.shuffle(CurDeck)
	pl1_Hand[0] = CurDeck[0]
	pl1_Hand[1] = CurDeck[1]
	pl1_Action = 0
	pl2_Hand[0] = CurDeck[3]
	pl2_Hand[1] = CurDeck[4]
	pl2_Action = getAction(pl2_Hand)

	g.RoundCards[0] = CurDeck[5]
	g.RoundCards[1] = CurDeck[6]
	g.RoundCards[2] = CurDeck[7]
	g.RoundCards[3] = CurDeck[9]
	g.RoundCards[4] = CurDeck[11]

	# for a in xrange(4):
	res = 0
	pl1_Action = 0
	y = predictAction(pl1_Hand)
	#y[g.WinResult(pl1_Hand, pl2_Hand) - 1] = 1.0
	inputData = np.array([[0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0,  
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0, 0.0, 0.0, 0.0, 
					0.0]])
	inputData[0, g.GetCardId(pl1_Hand[0])] = 1.0
	inputData[0, g.GetCardId(pl1_Hand[1])] = 1.0
	inputData[0, 52] = pl2_Action

	#wr = int(round(neuro.SpotResult(inputData, y), 2) * 100)
	wr = neuro.SpotResult(inputData, y)

	amax = 0
	
	for a in xrange(6):
		if wr[0, a] > wr[0, amax]:
			amax = a


	pl1_Action = amax
	if g.WinResult(pl1_Hand, pl2_Hand) == 1:
		res = pl1_Action
	else:
		res = -pl1_Action

    #neuro.QLearnUpdate(wr, res)

	if (j - 59900) > 0:
		pl1_Stack += res
		pl2_Stack -= res
		print("=============================================================================")
		print(wr)
		print(y)
		print(g.RoundCards)
		print(pl1_Hand, pl1_Action, pl1_Stack)
		print(pl2_Hand, pl2_Action, pl2_Stack)
	#print(neuro.Qgl)
