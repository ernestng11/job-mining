# -*- coding: utf-8 -*-
"""
Created on Sun May  3 02:27:35 2020

@author: ernes
"""

import glassdoor_scraper as gs

path = "C:/Users/ernes/Documents/datasci-salary/chromedriver"

slp_time = 15

df = gs.get_jobs('data scientist', 15, False, path, slp_time)

df.to_csv('glassdoor_jobs.csv', index = False)
