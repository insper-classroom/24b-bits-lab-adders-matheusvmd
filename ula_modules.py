#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b 
        carry.next  = a and b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    haList = [None for i in range(2)]  # (1)
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]  # (1)

    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()

@block
def adder2bits(x, y, soma, vaiUm):
    # adder de 2 bits!
    c = Signal(bool(0))

    ha = halfAdder(x[0], y[0], soma[0], c)
    fa = fullAdder(x[1], y[1], c, soma[1], vaiUm)

    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
