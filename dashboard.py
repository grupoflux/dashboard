#pip install dash dash-renderer dash-html-components dash-core-components plotly

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Gráficos"), #separando elementos dos childs por virgula
    dcc.Graph(id="FulanoCerveja",
            figure = {
                "data": [{"x": ["cerv1", "cerv2", "cerv3", "cerv4"], "y": [0, 5, 4, 2], "type":"bar", "name": "Cervejas"}
                ],
                "layout": {
                    "title": "Fulano (Cerveja)"
                }
            }),
    dcc.Graph(id="FulanoCafe",
            figure = {
                "data": [{"x": ["cafe1", "cafe2", "cafe3", "cafe"], "y": [0, 0, 2, 1], "type":"bar", "name": "Cafés"}
                ],
                "layout": {
                    "title": "Fulano (Café)"
                }
            })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
