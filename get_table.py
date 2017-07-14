import requests
import pandas as pd
import json

def get_table(url):
    response = requests.get(url)
    data = []

    #wait for json to load
    while len(data) == 0:
        data = response.json()
    headers = data['resultSet']['headers']
    rowdata = data['resultSet']['rowSet']
    df = pd.DataFrame(rowdata, columns=headers)
    return(df)
