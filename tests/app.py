# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from get_nba_data import advanced_stats

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='NBA Advanced Stats'),

    html.Div(children='''
        NBA Dash App: App created with data from http://stats.nba.com & get_nba_data (https://github.com/jkim65537/get_nba_data).
    '''),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Offensive Rating', 'value': 'OFF_RATING'},
            {'label': 'Defensive Rating', 'value': 'DEF_RATING'},
            {'label': 'Net Rating', 'value': 'NET_RATING'},
            {'label': 'Assist Percentage', 'value': 'AST_PCT'},
            {'label': 'Assist to Turnover Ratio', 'value': 'AST_TO'},
            {'label': 'Assist Ratio', 'value': 'AST_RATIO'},
            {'label': 'Offensive Rebound Percentage', 'value': 'OREB_PCT'},
            {'label': 'Defensive Rebound Percentage', 'value': 'DREB_PCT'},
            {'label': 'Rebound Percentage', 'value': 'REB_PCT'},
            {'label': 'Turnover Ratio', 'value': 'TM_TOV_PCT'},
            {'label': 'Effective Field Goal Percentage', 'value': 'EFG_PCT'},
            {'label': 'True Shooting Percentage', 'value': 'TS_PCT'},
            {'label': 'Usage Percentage', 'value': 'USG_PCT'},
            {'label': 'Pace', 'value': 'PACE'},
            {'label': 'Player Impact Estimate', 'value': 'PIE'},
        ],
        value='OFF_RATING' #defaults to
    ),

    dcc.Graph(id='advanced-graph')
])

@app.callback(Output('advanced-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    advanced = advanced_stats()
    df = advanced.get_data()
    df = df.ix[(df.GP>40)&(df.MIN>15)].sort_values([selected_dropdown_value], ascending=False)[0:51].reset_index()

    def get_column(df,col_name):
        if col_name == "REB_PCT":
            df = df[df.columns[df.columns.to_series().str.contains(col_name)]].ix[:,2]
        else:
            df = df[df.columns[df.columns.to_series().str.contains(col_name)]].ix[:,0]
        return(df)

    df['mccolumn'] = get_column(df,selected_dropdown_value)
    return {
        'data': [#go.Bar(x=df.PLAYER_NAME, y=df.DEF_RATING)]
                {'x':df.PLAYER_NAME,
                 'y':df.mccolumn}
                ]
    }

if __name__ == '__main__':
    app.run_server()
