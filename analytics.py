# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:55:29 2023

@author: user
"""

import dash
import pandas as pd
from dash import Dash,html,dcc,Input, Output, State, callback
import plotly.express as px
import dash_daq as daq
from datetime import datetime 
from zoneinfo import ZoneInfo
import os
import dash_leaflet as dl
import numpy as np

# os.chdir(r"C:\Users\user\ryan_chien_web")
    
# dash.register_page(__name__)

ASE_IQADATA =  pd.read_excel(r"1227309101 all data_(Security C).xlsx")


criteria=[0	,0	,0.005	,0.002	,0	,0.9	,0.94	,0.97	,1	,0	,1	,1	,1	,1	,0	,0]

symbol=['>','>','>','>','>','<','<','<','<','>','<','<','<','<','>','>']

app = dash.Dash(__name__, title="Ryan Chien Website")
# server = app.server



ASE_IQADATA_pivot=ASE_IQADATA.pivot_table(values='AVG',index='SUBLOTID',columns='VALUE_NAME',aggfunc='mean').reset_index()
# ASE_IQAVCAR =  pd.read_excel(r"C:\Users\user\pages\2023 VCAR list_(Security C).xlsx")
labellist = ASE_IQADATA.groupby('VALUE_NAME')['VALUE_NAME'].count().index.insert(0,'ALL')
ASE_IQA23D =  pd.read_csv(r"23D R-adj avg IsolationForest result_(Security C).csv")
labellist23D=ASE_IQA23D.columns[7:]
# fig=px.scatter_3d(ASE_IQADATA_pivot, x="F_FINGER_W", y="M1_CU_T",z="SW_WARPAGE")
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def get_3d_chart():
#     filtered_df = spacex_df
    fig=px.scatter_3d(ASE_IQADATA_pivot, x="F", y="M",z="S")
    fig.update_layout(font_color="white",paper_bgcolor='rgba(0,0,0,0)',
          plot_bgcolor='rgba(0,0,0,0)', title_x=0.5,title={'text':"3D plot Example", 'font':{'size':28},
 "yref": "paper",
"y" : 1,
"yanchor" : 'bottom'},margin=dict(l=25, r=25, t=25, b=25)),
    return fig 


def get_current_time():
    return(datetime.now())


app.layout = html.Div(
    children=[
        html.Div(children=[ 
            
                           html.Div(html.Img(src=dash.get_asset_url("Ryan_Chien.PNG"))),
                           html.Div(children= [
                                    html.H1('錢柏維 Ryan Chien 個人網站', style={ 'textAlign': 'center','color':'white', 'font-size':52, 'margin-left':'100px', 'margin-top':'10px'}),

                                        ]),
    ],style={'display': 'flex','flex-direction': 'row'}),#,style={'textAlign': 'center'}

html.Div([dcc.Loading(
  [
  dcc.Interval(
         id='interval-component',
         interval=30*1000, # in milliseconds
         n_intervals=2
     )      ,
  
  
  html.Div( daq.LEDDisplay(id='time',
label={'label':"目前時間",'style':{ 'color':'white', 'font-size':24}},
value=datetime.strftime(get_current_time(),'%H:%M:%S'),
color="#FF5E5E"
))
  ]) ],style={'textAlign': 'center'}),

html.Div([
    html.Div([
    html.Div(
    [html.H4('請輸入經度座標',style={'display':'inline-block','margin-left':40,'color':'white','font-size':24}),
    dcc.Input(id="longi", type="text",value=25.0330, placeholder="", style={'marginRight':'10px','font-size':24, 'width':100}),    

    html.H4('請輸入緯度座標',style={'display':'inline-block','margin-left':40,'color':'white','font-size':24}),
    dcc.Input(id="lati", type="text",value=121.5654 , placeholder="", style={'marginRight':'10px','font-size':24, 'width':100}),   
    
    html.H4('請輸入zoom',style={'display':'inline-block','margin-left':40,'color':'white','font-size':24}),
    dcc.Input(id="zoom", type="text",value=13, placeholder="", style={'marginRight':'10px','font-size':24, 'width':100}),   
    ],style={'textAlign':'center', 'flex-direction': 'row'}
    ),
    
        html.Div([
            html.H1("Map in Dash",style={'textAlign':'center', 'color':'white'}),
            
            dl.Map(dl.TileLayer(), center=[56,10], zoom=6, style={'height': '50vh'},id = 'map'),
            
            
        ],style={'textAlign':'center'}),
    ]),
],style={'flex-direction': 'row'}
    ),

html.H1("Algorithm",style={'textAlign':'center','margin-top':'10px', 'color':'white'}),
html.Div(children=[

html.Div(html.Img(src=dash.get_asset_url("Find maximun by GD algorithm.gif"),style={ 'width':400, 'height':300,'backgroundColor': 'black'}),style={'margin-top':'30px','margin-left':'40px'}),
html.Div(html.Img(src=dash.get_asset_url("Find maximun by GA algorithm.gif"),style={ 'width':400, 'height':300,'backgroundColor': 'black'}),style={'margin-top':'30px','margin-left':'40px'}),       
html.Div(html.Img(src=dash.get_asset_url("Find maximun by PSO algorithm_degree13_135.gif"),style={ 'width':400, 'height':300,'backgroundColor': 'black'}),style={'margin-top':'30px','margin-left':'40px'}), ],
    style={'display': 'flex','margin-right':20,'margin-top':'10px', 'flex-direction': 'row'}
    ) ,

                         
                                    html.Div([
                                    # html.Div(dcc.Graph(id='Trend-chart')),
                                    # html.H1("3D plot Example",style={'display': 'flex','margin-top':'10px', 'color':'white'}),
                                    html.Div(dcc.Graph(id='3D scatter-chart',figure=get_3d_chart(), style={"width": "100%","height": "100%"}), style={'margin-top':'10px', "width": "100%","height": "100%"})
                                    ],  
                          
                           style={"width": "100%","height": "100%",'margin-right':20,'margin-top':'10px'}),

                               html.Div([
                                    html.H1("Chart and Slider Example",style={'textAlign':'center', 'color':'white'}),
                                    
                                    dcc.Slider(
                                        id='slider',
                                        min=0,
                                        max=10,
                                        step=0.1,
                                        value=5,
                                        marks={i: str(i) for i in range(0, 11)},  # 標記範圍
                                    ),
                                    
                                    dcc.Graph(id='graph')  # 圖表的顯示區
                                ]),
                               
                               html.Div([
    html.H1("Dash Pie Chart with Callback",style={'textAlign':'center', 'color':'white'}),
    
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Category A', 'value': 'A'},
            {'label': 'Category B', 'value': 'B'},
            {'label': 'Category C', 'value': 'C'}
        ],
        value='A'  # 預設選擇的值
    ),
    
    dcc.Graph(id='pie-chart',style={'textAlign':'center', 'color':'white'})  # 用於顯示Pie Chart的區塊
])
                                


    ],style={'backgroundColor': 'black'},
    
    
    )

                                           
                                                                                    
@app.callback(
    Output('time', 'value'),
    [Input('interval-component', 'n_intervals')],
    # [State('primary-key', 'value'), 
    #  State('private-key', 'value')]
)
def update_output(n_clicks):
    # if n_clicks>0:
    # tz = pytz.timezone('Asia/Taipei')
    
    return(datetime.strftime(datetime.now(ZoneInfo("Asia/Taipei")),'%H:%M')    )                                                                             
                                                    


@app.callback(Output(component_id='3D scatter-chart', component_property='figure'),
              [Input(component_id='table_dropdown', component_property='value')]
#               ,              [State("success-pie-chart", 'children')]
             )
def get_3d_chart(table_dropdown):
#     filtered_df = spacex_df
    fig=px.scatter_3d(ASE_IQADATA_pivot, x="F", y="M",z="S")
    fig.update_layout(font_color="white",paper_bgcolor='rgba(0,0,0,0)',
          plot_bgcolor='rgba(0,0,0,0)', title_x=0.5,title={'text':"3D plot Example", 'font':{'size':20},
 "yref": "paper",
"y" : 1,
"yanchor" : 'bottom'},margin=dict(l=25, r=25, t=25, b=25)),
    return fig 



@app.callback(
    Output("map", "children"),
    Input("longi", "value"),
    Input("lati", "value"),
    Input("zoom", "value")
)
def update_map(longi,lati,zoom):


    return dl.Map(dl.TileLayer(), center=[longi,lati], zoom=zoom, style={'height': '50vh'})

# 定義回調函數
@app.callback(
    Output("graph", "figure"),
    [Input("slider", "value")]  # 監聽slider的值變化
)
def update_chart(value):
    # 使用 plotly 建立一個範例的散點圖
    x = np.linspace(0, 10, 100)
    y = np.sin(x + value)
    
    fig = px.scatter(x=x, y=y, title="Dynamic Scatter Plot")
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return fig

@app.callback(
    Output("pie-chart", "figure"),
    [Input("dropdown", "value")]  # 監聽下拉選單的值變化
)
def update_pie_chart(value):
    # 根據選擇的值來更新數據
    data = {
        'A': [40, 30, 30],
        'B': [25, 50, 25],
        'C': [35, 40, 25]
    }
    
    labels = ['Label 1', 'Label 2', 'Label 3']
    values = data[value]  # 根據選擇的dropdown值來選擇數據
    
    fig = px.pie(names=labels, values=values, title=f"Pie Chart for {value}")
    
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    
    return fig


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)