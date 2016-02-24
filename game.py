#!/usr/bin/python
# -*- coding: UTF-8 -*-

Deck = np.array(["2h", "2d", "2c", "2s", 
                "3h", "3d", "3c", "3s", 
                "4h", "4d", "4c", "4s", 
                "5h", "5d", "5c", "5s", 
                "6h", "6d", "6c", "6s",
                "7h", "7d", "7c", "7s", 
                "8h", "8d", "8c", "8s", 
                "9h", "9d", "9c", "9s", 
                "Th", "Td", "Tc", "Ts", 
                "Jh", "Jd", "Jc", "Js", 
                "Qh", "Qd", "Qc", "Qs", 
                "Kh", "Kd", "Kc", "Ks", 
                "Ah", "Ad", "Ac", "As"])

def getCardVal(Card):
	res = {
	'2' : 2,
	'3' : 3,
	'4' : 4,
	'5' : 5,
	'6' : 6,
	'7' : 7,
	'8' : 8,
	'9' : 9,
	'T' : 10,
	'J' : 11,
	'Q' : 12,
	'K' : 13,
	}.get(Card[0])

	return res



def getCardType(Card):
	res = {
	'h' : 1,
	'd' : 2,
	'c' : 3,
	's' : 4,
	}.get(Card[1])

	return res

def HightCard(Card1, Card2):
	c1 = getCardVal(Card1)
	res = Card2
	if Card2 < Card1:
		res = Card1
	return res

def Pair(Card1, Card2):
	res = 0
	if Card2 == Card1:
		res = Card1
	return res

def WinCond(pl1_Card1, pl1_Card2, pl2_Card1, pl2_Card2):
	cond = 0.0
	pl1_h = HightCard(pl1_Card1, pl1_Card2)
	pl2_h = HightCard(pl2_Card1, pl2_Card2)

	pl1_p = Pair(pl1_Card1, pl1_Card2)
	pl2_p = Pair(pl2_Card1, pl2_Card2)

	if pl1_p != 0 or pl2_p != 0:
		if pl1_p > pl2_p:
			cond = 1.0
	else:
		if pl1_h > pl2_h:
			cond = 1.0
	return cond