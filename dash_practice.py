# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)
app.title = "Meetings Analytics: Understand Your Meeting!"

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")



app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="D:\project\python\my_icon.jpg", className="header-emoji"),
                html.H1(
                    children="Team 1 Meetings Analytics", className="header-title",  style={"text-align": "center"}
                ),
                html.P(
                    children="Analyze the behavior of team meetings"
                    " and the number of users had in China"
                    " between 2022 and 2023", style={"text-align": "center"},
                    className="header-description",
                ),
            ],
            className="header",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id='example-graph',
                        config={"displayModeBar": False},
                        figure={
                                "data": [
                                    {
                                        "x": df["Fruit"],
                                        "y": df["Amount"],
                                        "color": df["City"],
                                        "type": "bar",

                                    },
                                ],
                                "layout": {
                                    "title": {
                                        "text": "Avocados Sold",
                                        "x": 0.05,
                                        "xanchor": "left",
                                    },
                                    "xaxis": {"fixedrange": True},
                                    "yaxis": {"fixedrange": True},
                                    "colorway": ["#E12D39"],
                                },
                            },
                    ),
                ),
            ],    
            className="wrapper",
        ),
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)
