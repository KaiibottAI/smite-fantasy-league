#!/usr/bin/env python3

import pandas as pd
import numpy as np


smiteGods = pd.read_csv('all-smite-gods.csv')

# print(smiteGods.info())

# Gods = smiteGods["GOD"]
# print(Gods)

# Gods_Pantheon = smiteGods[['GOD','PANTHEON']]
# print(Gods_Pantheon)

# Pantheon_Greek = smiteGods[smiteGods['PANTHEON'] == 'GREEK']
# print(Pantheon_Greek)

Class_HunterGuardian = smiteGods[smiteGods['CLASS'].isin(['HUNTER','GUARDIAN'])]
print(Class_HunterGuardian)