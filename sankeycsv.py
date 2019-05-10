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
from dash.dependencies import Output, Input, State


# Open and read data from csv file
# with open('test.json') as response:  
#     energy_data = json.loads(response.read())
 # moved inside function

# Old town road
#Employing dash to create a flask app. 
app = dash.Dash(__name__)
server = app.server

# Dash outputting html format with updates every 1 second with new data.


#Update the data in csv file using VBA for excel
import win32com.client as w
import pythoncom


pythoncom.CoInitialize()


# data_value = [] 

# Graph type sankey and sankey data links and nodes set up

# def update_sankey(n)
# data_trace = dict(
#     type='sankey',
#     width = 1118,
#     height = 772,
#     domain = dict(
#       x =  [0,1],
#       y =  [0,1]
#     ),
#     orientation = "h",
#     valueformat = ".0f",
#     valuesuffix = "TWh",
#     node = dict(
#       pad = 15,
#       thickness = 15,
#       line = dict(
#         color = "black",
#         width = 0.5
#       ),
#       label =  energy_data['node, label'].dropna(axis=0, how='any'),
#       color =  energy_data['color']
#     ),
#     link = dict(
#       source =  energy_data['source'].dropna(axis=0, how='any'),
#       target =  energy_data['target'].dropna(axis=0, how='any'),
#       value = data_value,


#       # value =  energy_data['value'].dropna(axis=0, how='any'),
#       # label =  energy_data['label'].dropna(axis=0, how='any'),
#   ))
 
    # Graph layout 


    


# @app.callback(
#   dash.dependencies.Output('Sankey','figure'),
#   [dash.dependencies.Input('')])
# def calc_energy():

# app.layout = html.Div(
#     html.Div([
#         html.H4('Sankey Diagram'),
#         html.Div(id='live-update-text'),
#         dcc.Graph(
#             id='Sankey',
#             figure={'data': [data_trace], 'layout': layout})
            
#         # dcc.Interval(
#         #     id='interval-component',
#         #     interval=1*1000, # in milliseconds
#         #     n_intervals=0
#         # )
#     ])
# )

app.layout = html.Div(
    html.Div([
        html.H4('Sankey Diagram'),
        # html.Div(id='live-update-text'),
        
        #Selecting graph type Sankey from Plotly and defining 'data' and 'layout' to use.
        dcc.Graph(
            id='Sankey',
            animate=True,
            # figure={'data': [data_trace], 'layout': layout}
            )
        ,
        
        #trigger event to @app.callback for function update_Sankey    
        dcc.Interval(
            id='interval_component', #identification id for the event.
            interval=1*1000, # update interval in milliseconds*1000
            n_intervals=0
        )
    ])
)

# Update Sankey data every 15 seconds. Function outputs 'figure' to id = 'Sankey' in dcc.Graph. 
@app.callback(Output('Sankey', 'figure'),
                [Input('interval_component','n_intervals')],
                # [State('Sankey', 'figure')]
                ) # trigger
def update_graph(n):
    # data_value = update_sankey_value.update()
    energy_data = pd.read_csv('my plot.csv')

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
      # value = data_value.dropna(axis=0, how='any')
    ))

    layout =  dict(
    title = "Energy Balance for 41 Cooper Square 2017<br>Source: Siemens BMS Data",
    font = dict(
      size = 10
    ),
    height=750,
    width=1500
     
    )

    figure={'data': [data_trace], 'layout': layout} 
    print (data_trace)
    print (layout)
    return figure # Figure is the Output of the @appcallback for the function and updated into the dcc.Graph component 'Sankey'


# update_graph()

    #choose path to original .xlsm file

# data_value = update_sankey_value()


    # path = "D:\Downloads/my plot - VBA.xlsm"
# data_value = update_sankey_value()

#     path = r"C:\Users\wlim\Desktop\Sankey\my plot.csv"
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
#     energy_data = pd.read_csv('my plot.csv')
#     return (figure)







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