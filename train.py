#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def showGraph(x, y, predict):
	plt.title("price of a car according to its kilometers")
	plt.xlabel("kilometers")
	plt.ylabel("price")
	plt.scatter(x, y)
	plt.plot(x, predict, "r")
	plt.show()

def destandardization(data, mean, std):
	for i in range(0, len(data)):
		data[i] = data[i] * std + mean
	return data

def gradientDescent(x, y, theta0, theta1):
	alpha = 0.1
	m = len(x)
	for _ in range(1000):
		tmpTheta0 = 0
		tmpTheta1 = 0
		for i in range(0, m):
			tmpTheta0 += theta0 + theta1 * x[i] - y[i]
			tmpTheta1 += (theta0 + theta1 * x[i] - y[i]) * x[i]
		theta0 -= (alpha / m) * tmpTheta0
		theta1 -= (alpha / m) * tmpTheta1
	return [theta0, theta1]

def standardization(data, mean, std):
	for i in range(0, len(data)):
		data[i] = (data[i] - mean) / std
	return data

def sqrt(nb):
	diff = 1
	a = nb
	if nb <= 0:
		return 0
	while diff > 0.001:
		b = 0.5 * (a + nb / a)
		diff = a - b
		a = b
	return a

def meanStd(data):
	mean = sum(data) / len(data)
	std = 0
	for number in data:
		std += (number - mean) * (number - mean)
	std = sqrt(std / len(data))
	return [mean, std]

def linearRegression(x, y):
	[meanX, stdX] = meanStd(x)
	[meanY, stdY] = meanStd(y)
	x = standardization(x, meanX, stdX)
	y = standardization(y, meanY, stdY)
	[theta0, theta1] = gradientDescent(x, y, 0, 0)
	predict = destandardization(theta0 + theta1 * x, meanY, stdY)
	x = destandardization(x, meanX, stdX)
	y = destandardization(y, meanY, stdY)
	return [x, y, predict]

if __name__ == "__main__":
	try:
		if os.stat("data.csv").st_size > 0:
			data = np.loadtxt("data.csv", dtype = float, delimiter = ",", skiprows = 1)
		else:
			sys.exit("Error")
	except:
		sys.exit("Error")
	[x, y, predict] = linearRegression(data[:, 0], data[:, 1])
	showGraph(x, y, predict)
	theta1 = (predict[0] - predict[1]) / (x[0] - x[1])
	theta0 = theta1 * -x[0] + predict[0]
	np.savetxt("theta.csv", [theta0, theta1])
