import requests
import pandas as pd
import json

def get_table(url):
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
    return(df)
