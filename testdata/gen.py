#!/usr/bin/env python3

import pprint

import numpy as np
import pandas as pd

from scipy.stats import pareto, beta

class MonitoringData():
    def __init__(self):
        self.l_p = np.array([95, 5, 3] + [1] * 77).astype('float64')
        #[95, 5, 3, 1, 1, 1, ...] etc
        self.l_p /= self.l_p.sum() # Bias towards 0th element
        self.data = {}
        self.categories = ['customer', 'region', 'language', 'success_rate', 'query_size']
        self.rng = np.random.default_rng()
        self.mu, self.sigma = 3., 1. # mean and standard deviation

    def generate(self):
        """Generate data for testing."""
        # 3000 rows, with region being purely randomly selected, language 
        # being biased towards 0th element. It is expected this will more accurately
        # represent a real-world scenario than pure random on every axis.
        self.data = {
	        'customer': [f'customer{x}' for x in range(3000)],
	        'region': [f'region{x}' for x in np.random.choice(range(20), 3000)],
	        'language': [f'language{x}' for x in np.random.choice(range(80), 3000, p=self.l_p)],
	        'success_rate': beta.rvs(a=999, b=1, size=3000),
            'query_size': [f'{x}' for x in np.random.choice([1024, 2048, 4096, 8192], 3000)],
        }

    def gen_df(self):
        self.df = pd.DataFrame(self.data)
        self.df.customer = self.df.customer.astype('category')
        self.df.region = self.df.region.astype('category')
        self.df.language = self.df.language.astype('category')
        self.df.query_size = self.df.query_size.astype('category')
    
    def get_data(self):
        return self.data

    def get_df(self):
        return self.df
    
    def get_categories(self):
        return self.categories

    def pprint(self):
        pprint.pprint(self.df)

