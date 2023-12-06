#!/usr/bin/env python3

import re

import testdata.gen as g
import detect.detect as d

BROKEN_CUSTOMER = 'customer213'
NO_BROKEN = 'entropy = 0.0'

# Create object, generate data
td = g.MonitoringData()
td.generate()
td.gen_df()
mdf = td.get_df()
# Start detection of broken-ness
dd = d.Detect(mdf, td.get_categories())
dd.analyse()
t2 = dd.suggest_gv()
# We shouldn't find any particular customer to be broken
res = re.findall(NO_BROKEN, t2, re.MULTILINE)
print (res)
if len(res) > 0:
    print("Found no particular entropy loss as expected")
# Punish one particular customer
dd.inflict_damage(target = BROKEN_CUSTOMER)
dd.analyse()
t2 = dd.suggest_gv()
res = re.findall(BROKEN_CUSTOMER, t2, re.MULTILINE)
print (res)
if len(res) > 0:
    print("Found %s as expected" % BROKEN_CUSTOMER)
