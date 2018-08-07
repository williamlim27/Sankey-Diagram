import json, urllib
import plotly.plotly as py
import pandas as pd
import numpy as np
import urllib.request as ur



with open('sample.txt') as json_file:  
    energy_data = json.loads(json_file)
data_trace = dict(
    type='sankey',
    width = 1118,
    height = 2500,
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",
    valueformat = ".0f",
    valuesuffix = "TWh",
    node = dict(
      pad = 10,
      thickness = 15,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label =  energy_data['data'][0]['node']['label'],
      color =  energy_data['data'][0]['node']['color']
    ),
    link = dict(
      source =  energy_data['data'][0]['link']['source'],
      target =  energy_data['data'][0]['link']['target'],
      value =  energy_data['data'][0]['link']['value'],
      label =  energy_data['data'][0]['link']['label']
  ))

layout =  dict(
    title = "Energy Balance for 41 Cooper Square 2017<br>Source: Siemens BMS Data <a href='https://bost.ocks.org/mike/sankey/'>Data</a>",
    font = dict(
      size = 10
    ),
    height=750,
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

fig = dict(data=[data_trace], layout=layout)
py.iplot(fig, validate=False)