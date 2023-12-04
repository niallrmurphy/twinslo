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

	def inflict_damage(self, cust='212'):
		self.df.success_rate = self.df.apply(self.bad_time, axis=1)

	def bad_time(self, x):
		cust = '212'
		if x.customer == f'customer{cust}':
			return self.bad_success
		return x.success_rate

	def analyse(self):
		self.model.fit(self.data, self.df.success_rate < self.threshold)
		print(tree.export_text(self.model))

	def suggest_text(self):
		print(tree.export_text(self.model))

	def suggest_gv(self):
		gvd = tree.export_graphviz(self.model, out_file="out.gv", class_names=self.categories)
		#, feature_names=self.model.feature_names_in_[self.df])
		graphviz.Source(gvd)
		graphviz.render('dot', 'png', 'out.gv')