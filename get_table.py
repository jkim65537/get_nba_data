import requests
import pandas as pd
import json

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
    headers = data['resultSets'][0]['headers']
    rowdata = data['resultSets'][0]['rowSet']
    df = pd.DataFrame(rowdata, columns=headers)
    return(df)
