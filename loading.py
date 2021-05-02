"""
loading.py:
Collection of python files responsible for loading and cleaning data.
"""

__author__ = "Ali Hussain"
__version__ = "1.0"

# Import Libraries
import pandas as pd
import numpy as np

def load_serve_mens():
	"""
	Load and process the mens service direction data csv file
	"""
	mens = pd.read_csv("data/charting-m-stats-ServeDirection.csv")
	mens = mens.reset_index()
	for i in reversed(range(5, len(mens.columns))):
		mens.iloc[:, i] = mens.iloc[:, i-5]
	mens = mens.drop(
    	columns = ['level_2', 'level_3', 'level_4',
    	           'match_id', 'row'])
	mens = clean_serve(mens, 'M')
	mens['Player Name'] = mens['level_1'].apply(
		lambda x: x.split(" ")[0].replace("_", " "))
	mens = calculate_pecentages_serve(mens)
	mens = mens.drop(
		columns = ['err_net', 'err_wide', 'err_deep',
		'err_wide_deep', 'err_foot', 'err_unknown'])
	return mens

def load_serve_womens():
	"""
	Load and process the womens service data csv file
	"""
	womens = pd.read_csv("data/charting-w-stats-ServeDirection.csv")
	womens = womens.drop(
		columns = ['err_net', 'err_wide', 'err_deep',
				   'err_wide_deep', 'err_foot', 'err_unknown'])
	womens = womens.reset_index()
	womens = womens.rename(
		columns = {'match_id': 'level_0', 'row': 'level_1'}
		).drop(columns = 'index')
	womens = clean_serve(womens, 'W')
	womens['Player Name'] = womens['level_1'].apply(
		lambda x: x.split(" ")[0].replace("_", " "))
	womens = calculate_pecentages_serve(womens)
	return womens

def clean_serve(data, string):
	"""
	Cleans the serve csv file
	"""
	data['year'] = data['level_0'].str[0:4]
	data['tournament'] = data['level_0'].apply(
		lambda x: x.partition(f"-{string}-")[2].partition("-")[0])
	def clean_level(x):
		p1 = x.loc[:, 'level_0'].iloc[0].rsplit("-",1)[0].rsplit("-", 1)[1]
		p2 = x.loc[:, 'level_0'].iloc[0].rsplit("-",1)[1]
		return pd.DataFrame(
			data = {'level_0': [f"{p1} Total", f"{p1} First Serve",
			        f"{p1} Second Serve", f"{p2} Total",
			        f"{p2} First Serve", f"{p2} Second Serve"]
			}, index = x.index)
	data = data.groupby("level_0").filter(lambda x: len(x) == 6)
	data['level_1'] = data.groupby("level_0").apply(lambda x: clean_level(x))
	return data

def calculate_pecentages_serve(data):
	"""
	Converts total serves into percentages
	"""
	deuce = [2,3,4]
	ad = [5,6,7]
	for i in range(0, len(data), 3):
	    data.iloc[i+1, deuce]\
	     = data.iloc[i+1, deuce]/ np.sum(data.iloc[i+1, deuce])
	    data.iloc[i+1, ad]\
	     = data.iloc[i+1, ad]/ np.sum(data.iloc[i+1, ad])
	    data.iloc[i+2, deuce]\
	     = data.iloc[i+2, deuce]/ np.sum(data.iloc[i+2, deuce])
	    data.iloc[i+2, ad]\
	     = data.iloc[i+2, ad]/ np.sum(data.iloc[i+2, ad])
	return data

def load_shot_mens():
	"""
	Load and process mens shot direction data csv file
	"""
	mens = pd.read_csv("data/charting-m-stats-ShotDirection.csv")
	mens = mens.reset_index()
	for i in reversed(range(12, len(mens.columns))):
		mens.iloc[:, i] = mens.iloc[:, i-12]
	mens = mens.drop(
			columns = ['level_0', 'level_1',  'level_2', 'level_3',
		           	   'level_4', 'level_5', 'level_6', 'level_7',
		               'level_8','level_9', 'level_10', 'level_11'])
	mens = clean_shot(mens, 'M')
	mens['player'] = mens['player'].apply(
		lambda x: x.split(" ")[0].replace("_", " "))
	mens = calculate_percentages_shot(mens)
	return mens

def load_shot_womens():
	"""
	Load and process womens shot direction data csv file
	"""
	womens = pd.read_csv("data/charting-w-stats-ShotDirection.csv")
	womens = womens.reset_index()
	womens = clean_shot(womens, 'W')
	womens['player'] = womens['player'].apply(
		lambda x: x.split(" ")[0].replace("_", " "))
	womens = womens.drop(columns = 'index')
	womens = calculate_percentages_shot(womens)
	return womens

def clean_shot(data, string):
	"""
	Cleans the shot csv file
	"""
	data['year'] = data['match_id'].str[0:4]
	data['tournament'] = data['match_id'].apply(
		lambda x: x.partition(f"-{string}-")[2].partition("-")[0])
	data = data.groupby("match_id").filter(lambda x: len(x) == 8)
	def clean_level(x):
		p1 = x.loc[:, 'match_id'].iloc[0].rsplit("-",1)[0].rsplit("-", 1)[1]
		p2 = x.loc[:, 'match_id'].iloc[0].rsplit("-",1)[1]
		return pd.DataFrame(
			data = {'player': [p1, p1, p1, p1,p2, p2, p2, p2]},
			index = x.index)
	data['player'] = data.groupby("match_id").apply(lambda x: clean_level(x))
	return data

def calculate_percentages_shot(data):
	"""
	Converts total shots into percentages
	"""
	cols = [3,4,5,6,7]
	for i in range(0, len(data), 4):
		data.iloc[i+1, cols] =\
		 data.iloc[i+1, cols]/ np.sum(data.iloc[i+1, cols])
		data.iloc[i+2, cols] =\
		 data.iloc[i+2, cols]/ np.sum(data.iloc[i+2, cols])
		data.iloc[i+3, cols] =\
		 data.iloc[i+3, cols]/ np.sum(data.iloc[i+3, cols])
	return data

def load_returns_mens():
	"""
	Loads the mens returns data
	"""
	mens = pd.read_csv("data/charting-m-stats-ReturnOutcomes.csv")
	mens = mens.reset_index()
	for i in reversed(range(9, len(mens.columns))):
		mens.iloc[:, i] = mens.iloc[:, i-9]
	mens = mens.drop(
		columns = ['level_0', 'level_1',  'level_2', 'level_3',
				   'level_4', 'level_5', 'level_6', 'level_7',
				   'level_8'])
	mens = clean_returns(mens, 'M')
	return mens

def load_returns_womens():
	"""
	Load the womens returns data
	"""
	womens = pd.read_csv("data/charting-w-stats-ReturnOutcomes.csv")
	womens = clean_returns(womens, 'W')
	return womens

def clean_returns(data, string):
	"""
	Cleans the returns csv
	"""
	data = data[['match_id', 'player', 'row', 'pts', 'in_play']]
	data = data[data['row'].isin(['4D', '4A', '5D', '5A', '6D', '6A'])]
	data['year'] = data['match_id'].str[0:4]
	data['tournament'] = data['match_id'].apply(
		lambda x: x.partition(f"-{string}-")[2].partition("-")[0])
	data['return_percentage'] = data['in_play'] / data['pts']
	data['row'] = data['row'].replace(
		{'4D': 'deuce_wide', '4A': 'ad_wide',
		 '5D': 'deuce_middle','5A': 'ad_middle',
		 '6D':'deuce_t', '6A': 'ad_t'})
	def clean_level(x):
		p1 = x.loc[:, 'match_id'].iloc[0].rsplit("-",1)[0].rsplit("-", 1)[1]
		p2 = x.loc[:, 'match_id'].iloc[0].rsplit("-",1)[1]
		return pd.DataFrame(
			data = {'player': [p1, p1, p1, p1, p1, p1,
			                   p2, p2, p2, p2, p2, p2]
			       },
			index = x.index)
	data = data.groupby("match_id").filter(lambda x: len(x) == 12)
	data['player'] = data.groupby("match_id").apply(lambda x: clean_level(x))
	data['Player Name'] = data['player'].apply(
		lambda x: x.split(" ")[0].replace("_", " "))
	return data