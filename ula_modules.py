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
    s1 = Signal(bool(0)) # (1)
    s2 = Signal(bool(0)) 
    s3 = Signal(bool(0))

    half_1 = halfAdder(a, b, s1, s2) 
    half_2 = halfAdder(c, s1, soma, s3) 

    @always_comb
    def comb():
        carry.next = s2 | s3 

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
