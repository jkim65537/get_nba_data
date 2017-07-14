TEAM_NAMES = {
            "ALL TEAMS":0,
            "VS ALL TEAMS":0,
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

PARAMETER_NAME = {
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

DATA_TYPE = {#'Season':'2016-17',
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
            }
'''
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
'''
