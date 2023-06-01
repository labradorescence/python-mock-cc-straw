#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1=Visitor("Jenny")
    np1=NationalPark("Yosemite")
    t1=Trip(v1, np1, "5/31","5/31")

    ipdb.set_trace()
