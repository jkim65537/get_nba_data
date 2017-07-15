import requests
import pandas as pd
import json
import sys

from get_nba_data.get_table import get_table

class get_leader_data:

    def __init__(self, season="2016-17",season_type="regular",per_mode="total",stat_cat="points"):
        data_type = {#'Season':'2016-17',
                     'SeasonType':{
                                'regular':'&SeasonType=Regular+Season',
                                'pre season':'&SeasonType=Pre+Season',
                                'playoffs':'&SeasonType=Playoffs',
                                'allstars':'&SeasonType=All+Star' #no data availble for all stars
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
                                'defensive_rebounds':'&StatCategory=DREB',
                                'rebounds':'&StatCategory=REB',
                                'assists':'&StatCategory=AST',
                                'steals':'&StatCategory=STL',
                                'blocks':'&StatCategory=BLK',
                                'turnovers':'&StatCategory=TOV',
                                'efficiency':'&StatCategory=EFF'
                                }
                     }
        assert (isinstance(season,str)), "Season number must be a string. Example: '2016-17'"
        assert (season_type.lower() in data_type['SeasonType']), "Season type must be one of these three: 'regular', 'pre season', or 'playoffs'."
        assert (per_mode.lower() in data_type['PerMode']), "Per mode must be one of these three: 'total', 'per game', or 'per 48 minutes'."
        assert (stat_cat.lower() in data_type['StatCategory']), '''Stat category must be one of these ten: 'points', 'minutes',
                                                                'offensive_rebounds', 'defensive_rebounds', 'rebounds',
                                                                'assists', 'steals', 'blocks', 'turnovers', or 'efficiency'.
                                                                '''

        url = "http://stats.nba.com/stats/leagueLeaders?LeagueID=00&Season={Season}&Scope=S{SeasonType}{PerMode}{StatCategory}".format(
                                                                                        Season=season,
                                                                                        SeasonType=data_type['SeasonType'][season_type.lower()],
                                                                                        PerMode=data_type['PerMode'][per_mode.lower()],
                                                                                        StatCategory=data_type['StatCategory'][stat_cat.lower()],
                                                                                        )
def get_data(self):
    length = 0
    while length == 0:
        df = get_table(self.url)
        length = len(df)
    return(df)
