import requests
import pandas as pd
import json
from get_nba_data.get_table import get_table
from get_nba_data import dictionaries
from get_nba_data.get_url_parameter import get_url_parameter

class advanced_stats:

    def __init__(self):
        pass

    def get_data(self,
                season_type="regular season",
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
                opponent="Vs all teams",
                division="",
                vs_division="",
                conference="",
                vs_conference="",
                outcome="",
                location="",
                shot_clock_range="",
                quarter="0",
                by_half="",
                playoff_round="",
                n_games="0"):
        url = "http://stats.nba.com/stats/leaguedashplayerstats?LeagueID=00&GameScope=&MeasureType=Advanced&PerMode=PerGame&PlusMinus=N&PaceAdjust=N&Rank=N&Month=0&DateFrom=&DateTo=&\
        {LastNGames}{SeasonType}{Season}{SeasonSegment}{PlayerPosition}\
        {StarterBench}{PlayerExperience}{DraftYear}{DraftPick}{College}{Country}{Weight}{Height}{TeamID}{OpponentTeamID}{Division}\
        {VsDivision}{Conference}{VsConference}{Outcome}{Location}{ShotClockRange}{Period}{GameSegment}{PORound}".format(
            LastNGames          =get_url_parameter("LastNGames",str(n_games)),
            SeasonType          =get_url_parameter("SeasonType",season_type),
            Season              =get_url_parameter("Season",season),
            SeasonSegment       =get_url_parameter("SeasonSegment",season_segment),
            PlayerPosition      =get_url_parameter("PlayerPosition",dictionaries.POSITION[position.upper()]),
            StarterBench        =get_url_parameter("StarterBench",starter_bench),
            PlayerExperience    =get_url_parameter("PlayerExperience",experience),
            DraftYear           =get_url_parameter("DraftYear",str(draft_year)),
            DraftPick           =get_url_parameter("DraftPick",draft_pick),
            College             =get_url_parameter("College",college),
            Country             =get_url_parameter("Country",country),
            Weight              =get_url_parameter("Weight",weight),
            Height              =get_url_parameter("Height",height),
            TeamID              =get_url_parameter("TeamID",str(dictionaries.TEAM_NAMES[team.upper()])),
            OpponentTeamID      =get_url_parameter("OpponentTeamID",str(dictionaries.TEAM_NAMES[opponent.upper()])),
            Division            =get_url_parameter("Division",division),
            VsDivision          =get_url_parameter("VsDivision",vs_division),
            Conference          =get_url_parameter("Conference",conference),
            VsConference        =get_url_parameter("VsConference",vs_conference),
            Outcome             =get_url_parameter("Outcome",outcome),
            Location            =get_url_parameter("Location",location),
            ShotClockRange      =get_url_parameter("ShotClockRange",shot_clock_range),
            Period              =get_url_parameter("Period",str(quarter)),
            GameSegment         =get_url_parameter("GameSegment",by_half),
            PORound             =get_url_parameter("PORound",playoff_round)
            ).replace(' ', '')

        length = 0
        while length == 0:
            df = get_table(url)
            length = len(df)
        return(df)
