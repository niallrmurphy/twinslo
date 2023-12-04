#!/usr/bin/env python3

import testdata.gen as g
import detect.detect as d

td = g.MonitoringData()
td.generate()
td.gen_df()
td.pprint()
mdf = td.get_df()
dd = d.Detect(mdf, td.get_categories())
dd.inflict_damage()
dd.analyse()
dd.suggest_text()
dd.suggest_gv()