#pip install dash dash-renderer dash-html-components dash-core-components plotly

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Gráficos"), #separando elementos dos childs por virgula
    dcc.Graph(id="Fulano",
            figure = {
                "data": [{"x": ["cerv1", "cerv2", "cerv3", "cerv4"], "y": ["N consumiu", "1 a 2 vezes", "3 a 4 vezes", "5 ou mais"], "type":"bar", "name": "Cervejas"}
                ],
                "layout": {
                    "title": "Fulano"
                }
            })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)