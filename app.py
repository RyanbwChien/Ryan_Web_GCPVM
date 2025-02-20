# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:28:54 2025

@author: user
"""

import os

import dash 
import dash_core_components as dcc 
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([ html.H2('Hello World'), dcc.Dropdown( id='dropdown', options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']], value='LA' ), html.Div(id='display-value') ])

@app.callback(dash.dependencies.Output('display-value', 'children'), 
              [dash.dependencies.Input('dropdown', 'value')]) 
def display_value(value): 
    return 'You have selected "{}"'.format(value)

if __name__ == 'main': 
    app.run_server()