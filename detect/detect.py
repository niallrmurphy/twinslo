#!/usr/bin/env python3

import pprint

import graphviz

import numpy as np
import pandas as pd

from sklearn import tree

class Detect():
	def __init__(self, df, categories, threshold=.95, bad_threshold=0.25):
		self.df = df
		self.model = tree.DecisionTreeClassifier(criterion='entropy')
		self.categories = categories
		self.threshold = threshold
		self.bad_success = 0.25
		self.data = pd.get_dummies(self.df.filter(categories))

	def inflict_damage(self, target='customer212'):
		self.df.success_rate = self.df.apply(bad_time, axis=1, customer=target)

	def analyse(self):
		self.model.fit(self.data, self.df.success_rate < self.threshold)

	def suggest_text(self):
		print(tree.export_text(self.model))

	def suggest_gv(self):
		# This does the graphic output
		tree.export_graphviz(self.model, out_file="out.gv",
			feature_names=self.model.feature_names_in_, filled=True)
		# This does the string output
		gvd = tree.export_graphviz(self.model, out_file=None,
			feature_names=self.model.feature_names_in_, filled=True)
		graphviz.Source(gvd)
		graphviz.render('dot', 'png', 'out.gv')
		return gvd

	def tree_internals(self):
		pprint.pprint(self.model.tree_.feature)
		pprint.pprint(self.model.tree_.value)


def bad_time(x, customer='customer212'):
	if x.customer == customer:
		return 0.25
	return x.success_rate