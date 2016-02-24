#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import random


def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))


class NeuroNet:
	def __init__(self):
		self.syn0 = 2 * np.random.random((2, 30)) - 1
		self.syn1 = 2 * np.random.random((30, 30)) - 1
		self.syn2 = 2 * np.random.random((30, 30)) - 1
		self.syn3 = 2 * np.random.random((30, 1)) - 1

		self.Qgl = np.random.randint(4, size=(100, 4))
		self.LF = 0.5
		self.DF = 0.5

	def SpotResult(self, inputVector, y = None):
		l0 = inputVector
		l1 = nonlin(np.dot(l0,self.syn0))
		l2 = nonlin(np.dot(l1,self.syn1))
		l3 = nonlin(np.dot(l2,self.syn2))
		l4 = nonlin(np.dot(l3,self.syn3))

		if y != None:
		    l4_error = y - l4

		    l4_delta = l4_error*nonlin(l4,deriv=True)

		    # как сильно значения l1 влияют на ошибки в l2?
		    l3_error = l4_delta.dot(self.syn3.T)

		    l3_delta = l3_error*nonlin(l3,deriv=True)

		    # как сильно значения l1 влияют на ошибки в l2?
		    l2_error = l3_delta.dot(self.syn2.T)
		    
		    l2_delta = l2_error*nonlin(l2,deriv=True)

		    # как сильно значения l1 влияют на ошибки в l2?
		    l1_error = l2_delta.dot(self.syn1.T)
		    # в каком направлении нужно двигаться, чтобы прийти к l1?
		    # если мы были уверены в предсказании, то сильно менять его не надо
		    l1_delta = l1_error * nonlin(l1,deriv=True)

		    self.syn0 += l0.T.dot(l1_delta)
		    self.syn1 += l1.T.dot(l2_delta)
		    self.syn2 += l2.T.dot(l3_delta)
		    self.syn3 += l3.T.dot(l4_delta)

		return l4

	def MaxValue(self, s):
		max = self.Qgl[s, 0]
		_, a_s = np.shape(self.Qgl)

		for a in xrange(a_s):
			if self.Qgl[s, a] > max:
				max = self.Qgl[s, a]
		return max

	def MaxValueAct(self, s):
		amax = 0
		_, a_s = np.shape(self.Qgl)

		for a in xrange(a_s):
			if self.Qgl[s, a] > self.Qgl[s, amax]:
				amax = a
		return amax		

	def QLearnUpdate(self, s, r):
		sd = s
		ad = self.MaxValueAct(s)
		self.Qgl[sd, ad] = self.Qgl[sd, ad] + (r + self.MaxValue(s) - self.Qgl[sd, ad])


