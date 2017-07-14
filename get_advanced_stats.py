http://stats.nba.com/players/advanced/#!?sort=TS_PCT&dir=-1&Season=2016-17&SeasonType=Regular%20Season&DateFrom=07%2F06%2F2017&DateTo=07%2F20%2F2017

http://stats.nba.com/stats/leaguedashplayerstats?
College=& #taken care of by get_url_parameter
Conference=& #taken care of by get_url_parameter
Country=& #taken care of by get_url_parameter
DateFrom=& ###############################
DateTo=& ###############################
Division=& #taken care of by get_url_parameter
DraftPick=& #taken care of by get_url_parameter
DraftYear=& #taken care of by get_url_parameter
GameScope=& #scope should always be S
GameSegment=& #by half
Height=& #taken care of by get_url_parameter
LastNGames=2& #just number 1-15
LeagueID=00& #default 00
Location=& #taken care of by get_url_parameter
MeasureType=Advanced& #should stay this way
Month=0& #numbers
OpponentTeamID=0& #use TeamID
Outcome=&P #W and L
ORound=0& #just number 0-4
PaceAdjust=N&
PerMode=PerGame& #dict
Period=0& #quarter
PlayerExperience=& #taken care of by get_url_parameter
PlayerPosition=& #taken care of by get_url_parameter
PlusMinus=N&
Rank=N&
Season=2013-14& #taken by parameter
SeasonSegment=& #taken care of by get_url_parameter
SeasonType=Regular+Season& #dictionary
ShotClockRange=& #taken care of by get_url_parameter
StarterBench=& #taken care of by get_url_parameter
TeamID=0& #use TeamID
VsConference=& #taken care of by get_url_parameter
VsDivision=& #taken care of by get_url_parameter
Weight= #taken care of by get_url_parameter

import requests
import pandas as pd
import json
import sys

filepath = "C:/Users/jkim118/Documents/get_nba_data/"
sys.path.append(filepath)
from get_table import get_table

def get_advanced_stats(season_type="regular season",
                       season="2016-17",
                       season_segment="entire season",
                       position="all positions",
                       starter_bench="all players",
                       experience="all experience",
                       draft_year="all draft years",
                       draft_pick="all draft rounds",
                       college="all Affliations",
                       country="all Countries",
                       weight="all weights",
                       height="all heights",
                       team="all teams",
                       vs_opponent="VS all teams",
                       division="all divisions",
                       conference="all conferences",
                       vs_conference="VS all conferences",
                       outcome="all outcomes",
                       location="all locations",
                       shot_clock_range="all shot clock ranges",
                       quarter="all quarters",
                       by_half="entire game",
                       playoff_round="all playoff rounds",
                       **kwargs
                        ):

    team_names = {
                "ALL TEAMS":0,
                "HAWKS":1610612737,
                "CELTICS":1610612738,
                "NETS":1610612751,
                "HORNETS":1610612766,
                "BULLS":1610612741,
                "CAVALIERS":1610612739,
                "MAVERICKS":1610612742,
                "PISTONS":1610612743,
                "WARRIORS":1610612744,
                "ROCKETS":1610612745,
                "PACERS":1610612754,
                "CLIPPERS":1610612746,
                "LAKERS":1610612747,
                "GRIZZLIES":1610612763,
                "HEAT":1610612748,
                "BUCKS":1610612749,
                "TIMBERWOLVES":1610612750,
                "PELICANS":1610612740,
                "KNICKS":1610612752,
                "THUNDER":1610612760,
                "MAGIC":1610612753,
                "76ERS":1610612755,
                "SUNS":1610612756,
                "TRAIL BLAZERS":1610612757,
                "TRAILBLAZERS":1610612757,
                "BLAZERS":1610612757,
                "KINGS":1610612758,
                "SPURS":1610612759,
                "RATPORS":1610612761,
                "JAZZ":1610612762,
                "WIZARDS":1610612764
                }

    url = "http://stats.nba.com/stats/leaguedashplayerstats?LeagueID=00&Season=&Scope=S{SeasonType}{Season}{SeasonSegment}{PlayerPosition}{StarterBench}{PlayerExperience}\
                                                                                {DraftYear}{DraftPick}{College}{Country}{Weight}{Height}{TeamID}{OpponentTeamID}\
                                                                                {VsDivision}{Conference}{VsConference}{Outcome}{Location}{ShotClockRange}{Period}{GameSegment}{PORound}".format(
                                                                                    SeasonType=get_url_parameter("SeasonType",season_type),
                                                                                    Season=get_url_parameter("Season",season),
                                                                                    SeasonSegment=get_url_parameter("SeasonSegment",season_segment),
                                                                                    PlayerPosition=get_url_parameter("PlayerPosition",position),
                                                                                    StarterBench=get_url_parameter("StarterBench",starter_bench),
                                                                                    PlayerExperience=get_url_parameter("PlayerExperience",experience),
                                                                                    DraftYear=get_url_parameter("DraftYear",draft_year),
                                                                                    DraftPick=get_url_parameter("DraftPick",draft_pick),
                                                                                    College=get_url_parameter("College",college),
                                                                                    Country=get_url_parameter("Country",country),
                                                                                    Weight=get_url_parameter("Weight",weight),
                                                                                    Height=get_url_parameter("Height",height),
                                                                                    TeamID=get_url_parameter("TeamID",str(team_names[team.upper()])),
                                                                                    OpponentTeamID=get_url_parameter("OpponentTeamID",str(team_names[vs_opponent.upper()])),
                                                                                    VsDivision=get_url_parameter("VsDivision",division),
                                                                                    Conference=get_url_parameter("Conference",conference),
                                                                                    VsConference=get_url_parameter("VsConference",vs_conference),
                                                                                    Outcome=get_url_parameter("Outcome",outcome),
                                                                                    Location=get_url_parameter("Location",location),
                                                                                    ShotClockRange=get_url_parameter("ShotClockRange",shot_clock_range),
                                                                                    Period=get_url_parameter("Period",quarter),
                                                                                    GameSegment=get_url_parameter("GameSegment",byhalf),
                                                                                    PORound=get_url_parameter("PORound",playoff_round)
                                                                                    )

    length = 0

    while length == 0:
        df = get_table(url)
        length = len(df)
    return(df)
division = "Vs all teams"
get_url_parameter("VsDivision",division)
dt = get_advanced_stats()


parameter_name = {
                'SEASON TYPE':'SeasonType',
                'SEASON':'Season',
                'SEASON SEGMENT':'SeasonSegment',
                'POSITION':'PlayerPosition',
                'STARTER BENCH':'StarterBench',
                'EXPERIENCE':'PlayerExperience',
                'DRAFT YEAR':'DraftYear',
                'DRAFT PICK':'DraftPick',
                'COLLEGE':'College',
                'COUNTRY':'Country',
                'WEIGHT':'Weight',
                'HEIGHT':'Height',
                'TEAM':'TeamID',
                'VS OPPONENT':'OpponentTeamID',
                'VS DIVISION':'VsDivision',
                'CONFERENCE':'Conference',
                'VS CONFERENCE':'VsConference',
                'OUTCOME':'Outcome',
                'LOCATION':'Location',
                'SHOT CLOCK RANGE':'ShotClockRange',
                'QUARTER':'Period',
                'BY HALF':'GameSegment',
                'PLAYOFF ROUND':'PORound'
                }



"http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=2016&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=Pre+All-Star&SeasonType=Regular+Season&ShotClockRange=7-4+Late&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
#generator
def category_name_split_generator(name_list):
    i = 0
    name_split = name_list[i]
    while True:
        yield name_split
        i += 1
        name_split = name_list[i]

def get_url_parameter(category, category_name):
    assert (isinstance(category,str)), "Category should be a string. For example, 'College'"
    assert (isinstance(category_name,str)), "Category name should be a string. For example, 'Washington'"

    #for weight and height
    category_name = category_name.replace('<', 'LT')
    category_name = category_name.replace('>', 'GT')

    name_list = category_name.title().split()
    name = category_name_split_generator(name_list)

    url_parameter = "&" + category + "="  + name.__next__()
    for i in range(0, len(name_list)-1):
        url_parameter += "+"
        url_parameter += name.__next__().replace("Vs","VS")

    return(url_parameter)


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
                            },
                ''
                 }
