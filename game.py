#!/usr/bin/python
# -*- coding: UTF-8 -*-

RoyalFlushVal = 1000
StraightFlushVal = 900
FourVal = 800
FullHouseVal = 700
FlushVal = 600
StraightVal = 500
ThreeVal = 400
TwoPairsVal = 300
PairVal = 200
HightVal = 100
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

NilHand = np.array(["", ""])
roundCards = np.array(["", "", "", "", ""])
def WinResult(Hand1, Hand2, Hand3 = NilHand, Hand4 = NilHand, Hand5 = NilHand, Hand6 = NilHand, Hand7 = NilHand, Hand8 = NilHand, Hand9 = NilHand):




def getHandValue(Hand):




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
	'A' : 14,
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

def Hight(HandVal):
	res = 0
	for c in HandVal:
		if c > res:
			res = c

	res += HightVal

	return res

def Pair(HandVal):
	res = 0
	for c1 in range(len(HandVal)):
		f = 0
		for c2 in range(len(HandVal)):
			if HandVal[c1] == HandVal[c2]:
				f += 1
			if f = 2:
				res = PairVal + HandVal[c1]
				break
		if res != 0:
			break
	return res

def TwoPairs(HandVal):
	res = 0
	pair = Pair(HandVal) - PairVal
	if pair != 0:
		for c1 in range(len(HandVal)):
			f = 0
			for c2 in range(len(HandVal)):
				if HandVal[c1] == HandVal[c2] and HandVal[c1] != pair:
					f += 1
				if f = 2:
					if HandVal[c1] > pair:
						res = TwoPairsVal + HandVal[c1]
					else:
						res = TwoPairsVal + pair
					break
			if res != 0:
				break
	return res

def Three(HandVal):
	res = 0
	for c1 in range(len(HandVal)):
		f = 0
		for c2 in range(len(HandVal)):
			if HandVal[c1] == HandVal[c2]:
				f += 1
			if f = 3:
				res = ThreeVal + HandVal[c1]
				break
		if res != 0:
			break
	return res


def Straight(HandVal):
	res = 0
	copyHand = sorted(np.copy(HandVal))
	f = 0
	hc = 0
	for c in range(len(HandVal)-1): 
		if HandVal[c+1] - HandVal[c] == 1:
			f += 1
			hc = HandVal[c+1]
		else:
			f = 0
		if f == 4:
			res = StraightVal + hc
			break
	return res

def Flush(HandVal, HandType):
	res = 0
	hc = 0
	for c1 in range(len(HandType)):
		f = 0
		for c2 in range(len(HandType)):
			if HandType[c1] == HandType[c2]:
				f += 1
				if HandVal[c1] > HandVal[c2]:
					hc = 

			if f = 5:
				res = FlushVal + HandType[c1]
				break
		if res != 0:
			break
	return res

def FullHouse(HandVal):
	res = 0
	three = Three(HandVal)
	pair =  Pair(HandVal)
	if three != 0 and pair != 0 and (there - ThreeVal) != (pair - PairVal):
		res = FullHouse + there - ThreeVal

	return res

def Four(HandVal):
	res = 0
	for c1 in range(len(HandVal)):
		f = 0
		for c2 in range(len(HandVal)):
			if HandVal[c1] == HandVal[c2]:
				f += 1
			if f = 4:
				res = FourVal + HandVal[c1]
				break
		if res != 0:
			break
	return res

def StraightFlush(HandVal, HandType):
	res = 0
	if HandType[0] == HandType[1] == HandType[2] == HandType[3] == HandType[4]:
		val = Straight(HandVal)
		if val != 0:
			res = StraightFlushVal + val - StraightVal
	return res

def RoyalFlush(HandVal, HandType):
	res = 0
	if HandType[0] == HandType[1] == HandType[2] == HandType[3] == HandType[4]:
		if HandVal[0] == 14 or HandVal[1] == 14 or HandVal[2] == 14 or HandVal[3] == 14 or HandVal[4] == 14:
			if HandVal[0] == 13 or HandVal[1] == 13 or HandVal[2] == 13 or HandVal[3] == 13 or HandVal[4] == 13:
				if HandVal[0] == 12 or HandVal[1] == 12 or HandVal[2] == 12 or HandVal[3] == 12 or HandVal[4] == 12:
					if HandVal[0] == 11 or HandVal[1] == 11 or HandVal[2] == 11 or HandVal[3] == 11 or HandVal[4] == 11:
						if HandVal[0] == 10 or HandVal[1] == 10 or HandVal[2] == 10 or HandVal[3] == 10 or HandVal[4] == 10:
							res = RoyalFlushVal
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