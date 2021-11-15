#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys


def main():
    try:
        x = int(input("Enter the kilometres: "))
    except:
        sys.exit("Error")
    try:
        if os.stat("theta.csv").st_size > 0:
            theta = np.loadtxt("theta.csv", dtype=float)
            if len(theta) >= 2:
                print("Estimated price: " + str(theta[0] + theta[1] * x))
                return
    except:
        pass
    print("Estimated price: 0")


if __name__ == "__main__":
    main()
