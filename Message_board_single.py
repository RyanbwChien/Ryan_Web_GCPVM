# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:06:24 2023

@author: G0225
"""

import dash
import dash_bootstrap_components as dbc
from dash import Dash,html,dcc,Input, Output, State, callback
import datetime 
import os

# from model import MessageBoard, submit_new_message, fetch_all_message
# dash.register_page(__name__)
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(children=[
    html.Div(html.Marquee('留言板功能測試中','ltr',style={'font-size':28} )),
    # <marquee direction="up">This text will scroll from bottom to top</marquee>
    html.Div(
    dbc.Container(
        [
            html.Div(style={'height': '20px'}),
            html.H2('留言板'),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Input(placeholder='輸入工號：', id='nickname', style={'width': '100%'}),
                            width=3,
                            style={
                                'padding': 0
                            }
                        ),
                        dbc.Col(
                            dbc.Input(placeholder='輸入留言内容：', id='message', style={'width': '100%'}),
                            width=7,
                            style={
                                'padding': 0
                            }
                        ),
                        dbc.Col(
                            dbc.Button('提交', id='submit', color='primary'),
                            width=2,
                            style={
                                'padding': 0
                            }
                        )
                    ]
                ),
                style={
                    'paddingTop': '10px',
                    'width': '70%',
                }
            ),
            dbc.Container(
                id='history-message',
                style={
                    'paddingTop': '50px',
                    'width': '70%',
                    'height': '70%',
                    'overflowY': 'auto',
                    'backgroundColor': '#fafafa'
                }
            ),

        ],
        style={
            'height': '800px',
            'boxShadow': 'rgb(0 0 0 / 20%) 0px 13px 30px, rgb(255 255 255 / 80%) 0px -13px 30px',
            'borderRadius': '10px'
        }
    ),
    style={
        'paddingTop': '50px'
    }
)
    
])

@app.callback(
    Output('history-message', 'children'),
    Input('submit', 'n_clicks'),
    [State('nickname', 'value'),
     State('message', 'value')]
)

def refresh_message_board(n_clicks, nickname, message):
    # if nickname and message:
    #     submit_new_message(nickname, message)
    if (nickname !=None and nickname !="") and (message!=None and message!=""):
        with open(r'message.txt','a') as file:
            file.write("'{" + '"nickname":"{}","message":"{}","Datetime":"{}"'.format(nickname,message,datetime.datetime.now().strftime(format='%Y-%m-%d %H:%M:%S'))+  "}'\n")
    
    if os.path.exists(r'message.txt'):

        temp = []
        with open(r'message.txt','r') as file:
            for lines in file:
                temp.append(eval(eval(lines)))
        
        return [
            html.Div(
                [
                    html.Strong(record["nickname"]),
                    html.Span(' '),
                    html.Em(record["Datetime"]),
                    html.Br(),
                    html.P(record["message"])
                ]
            )
            for record in temp
        ]
# app.run_server()

if __name__ == '__main__':
    app.run_server()
