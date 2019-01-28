import datetime
import json, urllib
import plotly.plotly as py
import pandas as pd
import numpy as np
import urllib.request as ur
import dash
import dash_core_components as dcc
import dash_html_components as html
# import pilibSE
# import pilib
from dash.dependencies import Input, Output


# Open and read data
# with open('test.json') as response:  
#     energy_data = json.loads(response.read())
energy_data = pd.read_csv('my plot.csv')


app = dash.Dash(__name__)

# Dash outputting html format with updates every 1 second with new data.


#Update the data in csv file using VBA for excel
# import win32com.client as w
# def update_sankey
#     #choose path to original .xlsm file
#     # path = "D:\Downloads/my plot - VBA.xlsm"
#     path = 
#     xl = w.Dispatch("Excel.Application")
#     wb = xl.Workbooks.Open(path)
#     ws = wb.ActiveSheet
#     lastRow = 68
#     lastCol = "G"

#     xl.Application.Run("GetVals")
#     for row in range(0,3):
#         ws.Columns(lastCol).EntireColumn.Delete()

#     for row in range(lastRow,75):
#         ws.Rows(lastRow + 1).EntireRow.Delete()

#     xl.DisplayAlerts = False
#     wb.SaveAs("sankey.csv", 24)
#     wb.Close(1)
#     xl.DisplayAlerts = True


# Graph type sankey and sankey data links and nodes set up

# def update_sankey(n)
data_trace = dict(
    type='sankey',
    width = 1118,
    height = 772,
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",
    valueformat = ".0f",
    valuesuffix = "TWh",
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label =  energy_data['node, label'].dropna(axis=0, how='any'),
      color =  energy_data['color']
    ),
    link = dict(
      source =  energy_data['source'].dropna(axis=0, how='any'),
      target =  energy_data['target'].dropna(axis=0, how='any'),
      value =  energy_data['value'].dropna(axis=0, how='any'),
      # label =  energy_data['label'].dropna(axis=0, how='any'),
  ))
 
    # Graph layout 

layout =  dict(
    title = "Energy Balance for 41 Cooper Square 2017<br>Source: Siemens BMS Data",
    font = dict(
      size = 10
    ),
    height=750,
    width=1500,
    updatemenus= [
            dict(
                y=1,
                buttons=[
                    dict(
                        label='Light',
                        method='relayout',
                        args=['paper_bgcolor', 'white']
                    ),
                    dict(
                        label='Dark',
                        method='relayout',
                        args=['paper_bgcolor', 'black']
                    )
                ]
            
            ),
            dict(
                y=0.9,
                buttons=[
                    dict(
                        label='Thick',
                        method='restyle',
                        args=['node.thickness', 15]
                    ),
                    dict(
                        label='Thin',
                        method='restyle',
                        args=['node.thickness', 8]
                    )      
                ]
            ),
            dict(
                y=0.8,
                buttons=[
                    dict(
                        label='Small gap',
                        method='restyle',
                        args=['node.pad', 15]
                    ),
                    dict(
                        label='Large gap',
                        method='restyle',
                        args=['node.pad', 20]
                    )
                ]
            ),
            dict(
                y=0.7,
                buttons=[
                    dict(
                        label='Snap',
                        method='restyle',
                        args=['arrangement', 'snap']
                    ),
                    dict(
                        label='Perpendicular',
                        method='restyle',
                        args=['arrangement', 'perpendicular']
                    ),
                    dict(
                        label='Freeform',
                        method='restyle',
                        args=['arrangement', 'freeform']
                    ),
                    dict(
                        label='Fixed',
                        method='restyle',
                        args=['arrangement', 'fixed']
                    )       
                ]
            ),
            dict(
                y=0.6,
                buttons=[             
                    dict(
                        label='Horizontal',
                        method='restyle',
                        args=['orientation', 'h']
                    ),
                    dict(
                        label='Vertical',
                        method='restyle',
                        args=['orientation', 'v']
                
                    )
                ]
            
            )
        ]

)
    


# @app.callback(
# 	dash.dependencies.Output('Sankey','figure'),
# 	[dash.dependencies.Input('')])
# def calc_energy():

app.layout = html.Div(
    html.Div([
        html.H4('Sankey Diagram'),
        html.Div(id='live-update-text'),
        dcc.Graph(
            id='Sankey',
            figure={'data': [data_trace], 'layout': layout})
            
        # dcc.Interval(
        #     id='interval-component',
        #     interval=1*1000, # in milliseconds
        #     n_intervals=0
        # )
    ])
)

# @app.callback(Output('wind-speed', 'figure'), [Input('wind-speed-update', 'n_intervals')])
# def gen_data(interval):

#     now = dt.datetime.now()
#     sec = now.second
#     minute = now.minute
#     hour = now.hour

#     total_time = (hour * 3600) + (minute * 60) + (sec)

#     con = sqlite3.connect("./Data/gendata.db")
#     df = pd.read_sql_query('SELECT node, link, source from Wind where\
#                             rowid > "{}" AND rowid <= "{}";'
#                             .format(total_time-200, total_time), con)

#     val = df['Speed'].iloc[-1]
#     direction = [0, (df['Direction'][0]-20), (df['Direction'][0]+20), 0]
# update_sankey()
# app.layout = server_layout
if __name__ == '__main__':
    app.run_server()