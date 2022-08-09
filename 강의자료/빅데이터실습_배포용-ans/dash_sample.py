#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://plotly.com/python/getting-started/
# 웹 브라우저에 접속하여 분석 결과 데이터가 그래프로 그려지는 지 실습하기
# Dash 코드를 실행하면 웹 서비스를 실행할 수 있음
# 관리자 권한으로 Anaconda Prompt를 실행해서 pip install dash하면 설치가 완료됨
# flask : 웹 서버 프레임워크
# Dash를 사용하면 flask와 같은 별도 프레임워크 없이, 웹 서버를 간단하게 구축할 수 있음
# Error 발생
# ctrl + c해서 파이썬 파일로 만들면 됨
# 다운로드 후 파이썬 파일로 저장한 다음 파이썬 파일을 실행
# python <파일명>을 실행하면 웹 서버가 구동
# localhost:8050으로 접속하면 sample 화면을 확인할 수 있음
# 웹 서버를 통해 다른 장소나 디바이스에서도 화면을 똑같이 볼 수 있고, 다른 사람과의 공유가 용이

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Color:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Gold', 'MediumTurquoise', 'LightGreen']
        ],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], marker_color=color))
    return fig

app.run_server(debug=True)

