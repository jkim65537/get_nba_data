from get_nba_data import advanced_stats

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
n_games="0"

def test():
    advanced = advanced_stats()
    playoff_data = advanced.get_data(season_type="playoffs")
    twenty_fifteen = advanced.get_data(season="2015-16")
    #no data available for different season segments
    forwards = advanced.get_data(position="forwards")
    starters = advanced.get_data(starter_bench="starters")
    veterans = advanced.get_data(experience="verteran")
    draft_year = advanced.get_data(draft_year=2014)
