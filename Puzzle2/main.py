# main.py
# Stein's summer puzzle problem
# Daniel Kogan 6/19/2020

import cmath
from math import *

def main():

    def DerriveSequence(terms):
        x=complex(0.5,sqrt(3)/2)
        # print(x)
        ValueList = []
        for i in range(terms):
            i+=1
            Value = x**i + (1/x**i)
            ValueList.append(round(Value.real))
        return(ValueList)

    def Seq(terms):
        ValueList = []
        for x in range(terms):
            x+=1
            ValueList.append(round(2*cos((1/3)*pi*x)))
        return ValueList

    print(DerriveSequence(15))
    print(Seq(15))




if __name__ == '__main__':
    main()