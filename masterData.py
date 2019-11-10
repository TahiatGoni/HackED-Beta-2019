"""
Master file contains all data about the company
such as the worker numbers, working days, working hours
and all other data relevant to calculations that are being performed
Can be accessed and tweaked by authorised personnel
"""
import projectclasses
WorkForce = 50

#___________________________________________________________________________
#producta, first product by company takes 3 hours to make per unit
producta = projectclasses.product("a", 3)
#productb, second product made by company takes 2 hours to make per unit
productb = projectclasses.product("b", 2)
#productc. second product made by company takes 0.5 hours to make per unit
productc = projectclasses.product("c", 2)
#___________________________________________________________________________

#Client info: currently serving only one client
clienta = projectclasses.client("a")
