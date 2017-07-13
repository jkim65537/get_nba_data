####################################################################
#Author = Jun Kim
#
#Purpose: function to scrape and load categorical NBA leader data by
#         str season
#         str season_type
#         str per_mode
#         str stat_cat
####################################################################

import requests
import pandas as pd
import json

def get_leader_data(season="2016-17",season_type="regular",per_mode="total",stat_cat="points"):

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

    leader_url = "http://stats.nba.com/stats/leagueLeaders?LeagueID=00&Season={Season}&Scope=S{SeasonType}{PerMode}{StatCategory}".format(
                                                                                    Season=season,
                                                                                    SeasonType=data_type['SeasonType'][season_type.lower()],
                                                                                    PerMode=data_type['PerMode'][per_mode.lower()],
                                                                                    StatCategory=data_type['StatCategory'][stat_cat.lower()],
                                                                                    )

    leader_url
    response = requests.get(leader_url)
    data = []

    #wait for json to load
    while len(data) == 0:
        data = response.json()
    headers = data['resultSet']['headers']
    rowdata = data['resultSet']['rowSet']
    df = pd.DataFrame(rowdata, columns=headers)
    return(df)
if __name__ == "__main__":
    df = get_leader_data()
