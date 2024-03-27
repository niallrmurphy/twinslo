#!/usr/bin/env python3

# A DecisionTreeClassifier is not very introspectable, so we're using
# sad hacks to pull out what we need to. Hopefully someone else can
# provide a better way to do this.

import pprint
import re

import testdata.gen as g
import detect.detect as d

BROKEN_CUSTOMER = 'customer213'
BROKEN_REGION = 'region5'
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
dd.inflict_specific_customer_damage(target = BROKEN_CUSTOMER)
dd.analyse()
t2 = dd.suggest_gv()
res = re.findall(BROKEN_CUSTOMER, t2, re.MULTILINE)
print (res)
if len(res) > 0:
    print("Found %s as expected" % BROKEN_CUSTOMER)
# Punish a specific region - make new pristine data first
td2 = g.MonitoringData()
td2.generate()
td2.gen_df()
mdf2 = td2.get_df()
dd2 = d.Detect(mdf2, td2.get_categories())
# now inflict damage
dd2.inflict_specific_region_damage(target = 'region5')
dd2.analyse()
t3 = dd2.suggest_gv()
res2 = re.findall(BROKEN_REGION, t3, re.MULTILINE)
print (res2)
if len(res2) > 0:
    print("Found %s as expected" % BROKEN_REGION)



