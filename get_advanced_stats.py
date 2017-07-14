import requests
import pandas as pd
import json
import sys

filepath = "C:/Users/jkim118/Documents/get_nba_data/"
filepath_mac = "/Users/junkim/Documents/nba_stats/get_nba_data"
sys.path.append(filepath_mac)
from get_table import get_table
import dictionaries

def get_advanced_stats(season_type="regular season",
                       season="2016-17",
                       season_segment="",
                       position="",
                       starter_bench="",
                       experience="",
                       draft_year="",
                       draft_pick="",
                       college="",
                       country="",
                       weight="",
                       height="",
                       team="all teams",
                       vs_opponent="Vs all teams",
                       division="",
                       conference="",
                       vs_conference="",
                       outcome="",
                       location="",
                       shot_clock_range="",
                       quarter="0",
                       by_half="",
                       playoff_round="",
                       **kwargs
                        ):

    url = "http://stats.nba.com/stats/leaguedashplayerstats?LeagueID=00&GameScope=&MeasureType=Advanced&PerMode=PerGame&PlusMinus=N&PaceAdjust=N&Rank=N&Month=0&DateFrom=&DateTo=&LastNGames=2\
        {SeasonType}{Season}{SeasonSegment}{PlayerPosition}{StarterBench}{PlayerExperience}\
        {DraftYear}{DraftPick}{College}{Country}{Weight}{Height}{TeamID}{OpponentTeamID}\
        {VsDivision}{Conference}{VsConference}{Outcome}{Location}{ShotClockRange}{Period}{GameSegment}{PORound}".format(
        SeasonType      =get_url_parameter("SeasonType",season_type),
        Season          =get_url_parameter("Season",season),
        SeasonSegment   =get_url_parameter("SeasonSegment",season_segment),
        PlayerPosition  =get_url_parameter("PlayerPosition",position),
        StarterBench    =get_url_parameter("StarterBench",starter_bench),
        PlayerExperience=get_url_parameter("PlayerExperience",experience),
        DraftYear       =get_url_parameter("DraftYear",draft_year),
        DraftPick       =get_url_parameter("DraftPick",draft_pick),
        College         =get_url_parameter("College",college),
        Country         =get_url_parameter("Country",country),
        Weight          =get_url_parameter("Weight",weight),
        Height          =get_url_parameter("Height",height),
        TeamID          =get_url_parameter("TeamID",str(dictionaries.TEAM_NAMES[team.upper()])),
        OpponentTeamID  =get_url_parameter("OpponentTeamID",str(dictionaries.TEAM_NAMES[vs_opponent.upper()])),
        VsDivision      =get_url_parameter("VsDivision",division),
        Conference      =get_url_parameter("Conference",conference),
        VsConference    =get_url_parameter("VsConference",vs_conference),
        Outcome         =get_url_parameter("Outcome",outcome),
        Location        =get_url_parameter("Location",location),
        ShotClockRange  =get_url_parameter("ShotClockRange",shot_clock_range),
        Period          =get_url_parameter("Period",quarter),
        GameSegment     =get_url_parameter("GameSegment",by_half),
        PORound         =get_url_parameter("PORound",playoff_round)
        )
url
    response = requests.get(url)
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
    length = 0

    while length == 0:
        df = get_table(url)
        length = len(df)
    return(df)

#generator
def category_name_split_generator(name_list):
    i = 0
    name_split = name_list[i]
    while True:
        yield name_split
        i += 1
        name_split = name_list[i]

def get_url_parameter(category, category_name):
    if not category_name:
        url_parameter = "&" + category + "="
        return(url_parameter)
    assert (isinstance(category,str)), "Category should be a string. For example, 'College'"
    assert (isinstance(category_name,str)), "Category name should be a string. For example, 'Washington'"

    #for weight and height
    category_name = category_name.replace('<', 'LT')
    category_name = category_name.replace('>', 'GT')

    name_list = category_name.title().split()
    name = category_name_split_generator(name_list)

    url_parameter = "&" + category + "="  + name.__next__().replace("Vs","VS")
    for i in range(0, len(name_list)-1):
        url_parameter += "+"
        url_parameter += name.__next__()

    return(url_parameter)

if __name__ == "__main__":
    df = get_advanced_stats()
