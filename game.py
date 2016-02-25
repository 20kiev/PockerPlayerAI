#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np 

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

NilHand = np.array(["  ", "  "])
RoundCards = np.array(["  ", "  ", "  ", "  ", "  "])
def GetCardId(Card):
	for i in range(len(Deck)):
		if Card == Deck[i]:
			return i



def WinResult(Hand1, Hand2, Hand3 = NilHand, Hand4 = NilHand, Hand5 = NilHand, Hand6 = NilHand, Hand7 = NilHand, Hand8 = NilHand, Hand9 = NilHand):
	hvMax = getHandValue(Hand1)
	hid = 1

	hvTmp = getHandValue(Hand2)
	if hvMax < hvTmp:
		hvMax = hvTmp
		hid = 2

	hvTmp = getHandValue(Hand3)
	if hvMax < hvTmp:
		hvMax = hvTmp
		hid = 3
	hvTmp = getHandValue(Hand4)
	if hvMax < hvTmp:
		hvMax = hvTmp
		hid = 4

	hvTmp = getHandValue(Hand5)
	if hvMax < hvTmp:
		hvMax = hvTmp
		hid = 5

	hvTmp = getHandValue(Hand6)
	if hvMax < hvTmp:
		hvMax = hvTmp
		hid = 6

	hvTmp = getHandValue(Hand7)
	if hvMax < hvTmp:
		hvMax = hvTmp
		hid = 7

	hvTmp = getHandValue(Hand8)
	if hvMax < hvTmp:
		hvMax = hvTmp
		hid = 8

	hvTmp = getHandValue(Hand9)
	if hvMax < hvTmp:
		hvMax = hvTmp
		hid = 9

	return hid

def getHandValue(Hand):
	if Hand[0] != NilHand[0]:
		HandVal = np.array([getCardVal(Hand[0]), getCardVal(Hand[1]), getCardVal(RoundCards[0]), getCardVal(RoundCards[1]), getCardVal(RoundCards[2]), getCardVal(RoundCards[3]), getCardVal(RoundCards[4])])
		HandType = np.array([getCardType(Hand[0]), getCardType(Hand[1]), getCardType(RoundCards[0]), getCardType(RoundCards[1]), getCardType(RoundCards[2]), getCardType(RoundCards[3]), getCardType(RoundCards[4])])

		v = RoyalFlush(HandVal, HandType)
		if v != 0:
			return v

		v = StraightFlush(HandVal, HandType)
		if v != 0:
			return v

		v = Four(HandVal)
		if v != 0:
			return v

		v = FullHouse(HandVal)
		if v != 0:
			return v

		v = Flush(HandVal, HandType)
		if v != 0:
			return v
		
		v = Straight(HandVal)
		if v != 0:
			return v

		v = Three(HandVal)
		if v != 0:
			return v

		v = TwoPairs(HandVal)
		if v != 0:
			return v

		v = Pair(HandVal)
		if v != 0:
			return v

		v = Hight(HandVal)
		if v != 0:
			return v

	return 0

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
			if f == 2:
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
				if f == 2:
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
			if f == 3:
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
		elif HandVal[c+1] - HandVal[c] == 0:
			continue
		elif HandVal[c+1] - HandVal[c] > 1:
			f = 0
	if f >= 4:
		res = StraightVal + hc

	return res

def Flush(HandVal, HandType):
	res = 0
	hc = 0
	for c1 in range(len(HandType)):
		f = 0
		for c2 in range(len(HandType)):
			if HandType[c1] == HandType[c2]:
				f += 1
				if HandVal[c1] > hc:
					hc = HandVal[c1]
	if f >= 5:
		res = FlushVal + hc

	return res

def FullHouse(HandVal):
	res = 0
	three = Three(HandVal)
	pair =  Pair(HandVal)
	if three != 0 and pair != 0 and (three - ThreeVal) != (pair - PairVal):
		res = FullHouseVal + three - ThreeVal

	return res

def Four(HandVal):
	res = 0
	for c1 in range(len(HandVal)):
		f = 0
		for c2 in range(len(HandVal)):
			if HandVal[c1] == HandVal[c2]:
				f += 1
			if f == 4:
				res = FourVal + HandVal[c1]
				break
		if res != 0:
			break
	return res

def StraightFlush(HandVal, HandType):
	res = 0
	copyHand = sorted(np.copy(HandVal))
	f = 0
	hc = 0
	for c in range(len(HandVal)-1): 
		if (HandVal[c+1] - HandVal[c]) == 1 and HandType[c+1] == HandType[c]:
			f += 1
			hc = HandVal[c+1]
		elif (HandVal[c+1] - HandVal[c]) == 0 and HandType[c+1] == HandType[c]:
			f += 1
			hc = HandVal[c+1]
		elif (HandVal[c+1] - HandVal[c]) > 1:
			f = 0
	if f >= 4:
		res = StraightFlushVal + hc

	return res

def RoyalFlush(HandVal, HandType):
	res = 0
	sf = StraightFlush(HandVal, HandType)
	if sf != 0 and sf - StraightFlushVal == 14:
		res = RoyalFlushVal
	return res

	
