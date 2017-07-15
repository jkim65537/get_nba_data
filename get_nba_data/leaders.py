import requests
import pandas as pd
import json
from get_nba_data import dictionaries

class category_leaders:

    def __init__(self):
        pass

    def get_data(self,season="2016-17",season_type="regular",per_mode="total",stat_cat="points"):

        assert (isinstance(season,str)), "Season number must be a string. Example: '2016-17'"
        assert (season_type.lower() in dictionaries.DATA_TYPE['SeasonType']), "Season type must be one of these three: 'regular', 'pre season', or 'playoffs'."
        assert (per_mode.lower() in dictionaries.DATA_TYPE['PerMode']), "Per mode must be one of these three: 'total', 'per game', or 'per 48 minutes'."
        assert (stat_cat.lower() in dictionaries.DATA_TYPE['StatCategory']), '''Stat category must be one of these ten: 'points', 'minutes',
                                                                    'offensive_rebounds', 'defensive_rebounds', 'rebounds',
                                                                    'assists', 'steals', 'blocks', 'turnovers', or 'efficiency'.
                                                                    '''

        url = "http://stats.nba.com/stats/leagueLeaders?LeagueID=00&Season={Season}&Scope=S{SeasonType}{PerMode}{StatCategory}".format(
                Season=season,
                SeasonType=dictionaries.DATA_TYPE['SeasonType'][season_type.lower()],
                PerMode=dictionaries.DATA_TYPE['PerMode'][per_mode.lower()],
                StatCategory=dictionaries.DATA_TYPE['StatCategory'][stat_cat.lower()],
                )

        def get_table(url):
            headers = {'User-Agent': 'Mozilla/5.0'}
            try:
                response = requests.get(url,headers=headers,timeout = 10)
            except:
                try:
                    url ='http://stats.nba.com/stats/leaguedashplayerstats?LeagueID=00&GameScope=&MeasureType=Advanced&PerMode=PerGame&PlusMinus=N&PaceAdjust=N&Rank=N&Month=0&DateFrom=&DateTo=&%20&LastNGames=0&SeasonType=Regular+Season&Season=2016-17&SeasonSegment=&PlayerPosition=%20&StarterBench=&PlayerExperience=&DraftYear=&DraftPick=&College=&Country=&Weight=&Height=&TeamID=0&OpponentTeamID=0&Division=%20&VsDivision=&Conference=&VsConference=&Outcome=&Location=&ShotClockRange=&Period=0&GameSegment=&PORound='
                    response = requests.get(url,headers=headers,timeout = 10)
                    if isinstance(response,requests.models.Response):
                        raise Exception("http://stats.nba.com/players/advanced/#!?sort=PIE&dir=-1 is down. Try again when it's back up.")
                except:
                    pass
                raise Exception("the data you requested does not exist")
            data = []

            #wait for json to load
            while len(data) == 0:
                try:
                    data = response.json()
                except:
                    pass #do it til it loads
            headers = data['resultSet']['headers']
            rowdata = data['resultSet']['rowSet']
            df = pd.DataFrame(rowdata, columns=headers)
            return(df)

        length = 0
        while length == 0:
            df = get_table(url)
            length = len(df)
        return(df)
