#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
pd.options.plotting.backend = 'plotly'

app = dash.Dash(__name__)
# 웹 서버가 구동될 때, 저장된 분석 결과를 읽어오는 과정
# 저장된 분석결과 데이터를 읽어서 data에 저장
data = pd.read_excel('data/covid_top10.xlsx', header = [0, 1])
# 첫 번째 컬럼을 로우 인덱스로 변경
data = data.set_index(data.columns[0])[1:]

# 02. html 관련 코드에 원하는 내용으로 변경하기
app.layout = html.Div([
    html.P("Type:"), # 01. 데이터 타입 변경
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['new_cases', 'new_deaths', 'new_tests'] # 02. 3개의 컬럼명 변경
        ],
        value='new_cases',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

# 03. 분석 결과를 그래프로 보여주기
@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
# 함수 변경하기
def display_color(val): # 선택한 값(val)에 해당하는 데이터의 그래프를 그림
    fig = data[val].plot()
    return fig

app.run_server(debug=True)

