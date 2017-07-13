import requests
import pandas as pd
import os
import json
from bs4 import BeautifulSoup

data_type = {#'Season':'2016-17',
             'SeasonType':{
                        'regular':'&SeasonType=Regular%20Season',
                        'pre season':'&SeasonType=Pre%20Season',
                        'playoffs':'&SeasonType=Playoffs',
                        'allstars':'&SeasonType=All%20Star' #no data availble for all stars
                        },
             'PerMode':{
                        'total':'&PerMode=Totals',
                        'per game':'&PerMode=PerGame',
                        'per 48 minutes':'&PerMode=Per48'
                        },
             'StatCategory':{
                        'points':'&StatCategory=PTS',
                        'minutes':'&StatCategory=MIN',
                        'offensive_rebounds':'&StatCategory=OREB',
                        'defnsive_rebounds':'&StatCategory=DREB',
                        'rebounds':'&StatCategory=REB',
                        'assists':'&StatCategory=AST',
                        'steals':'&StatCategory=STL',
                        'blocks':'&StatCategory=BLK',
                        'turnovers':'&StatCategory=TOV',
                        'efficiency':'&StatCategory=EFF'
                        }
             }
'http://stats.nba.com/leaders/#!?Season=2016-17&StatCategory=REB&SeasonType=Regular%20Season&PerMode=Totals'
leader_url = "http://stats.nba.com/leaders/#!?Season=2015-16{SeasonType}{PerMode}{StatCategory}".format(
                                                                                SeasonType=data_type['SeasonType']['regular'],
                                                                                PerMode=data_type['PerMode']['total'],
                                                                                StatCategory=data_type['StatCategory']['blocks']
                                                                                )
leader_url

response = requests.get(leader_url)
data = json.loads(response.json())


#tests
data_type['SeasonType']['regular']
data_type['players']
data_type['leaders']['points']
