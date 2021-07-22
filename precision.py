#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import numpy as np
import os

def checkError():
	try:
		if (os.path.isfile("data.csv") and os.stat("data.csv").st_size > 0) and os.path.isfile("theta.csv") and os.stat("theta.csv").st_size > 0:
			data = np.loadtxt("data.csv", dtype = float, delimiter = ",", skiprows = 1)
			theta = np.loadtxt("theta.csv", dtype = float)
			if (len(data[:, 0]) >= 2 and len(theta) >= 2):
				return [data, theta]
	except:
		pass
	print("Error")
	exit(1)

if __name__ == "__main__":
	[data, theta] = checkError()
	x = data[:, 0]
	y = data[:, 1]
	precision = 0
	for i in range(0, len(x)):
		precision += (theta[0] + theta[1] * x[i] - y[i]) * (theta[0] + theta[1] * x[i] - y[i])
	precision /= 2 * len(x)
	print("The precision is " + str(precision))
