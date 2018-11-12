#pip install dash dash-renderer dash-html-components dash-core-components plotly

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Gráficos"), #separando elementos dos childs por virgula
    dcc.Graph(id="Fulano",
            figure = { #Consumo Mensal x Nome dos produtos
                "data": [{"x": ["pale ale", "weissbier", "itaipava", "skol"], "y": [0, 5, 4, 2], "type":"bar", "name": "Cervejas"},
                         {"x": ["expresso", "cappuccino", "mocaccino", "cafe4"], "y": [0, 0, 2, 1], "type":"line", "name": "Cafés"},
                ],
                "layout": {
                    "title": "Fulano"
                }
            }),
    
    dcc.Graph(id="Sicrano",
            figure = { #Consumo Mensal x Nome dos produtos
                "data": [{"x": ["pale ale", "weissbier", "itaipava", "skol"], "y": [0, 1, 1, 0], "type":"bar", "name": "Cafés"},
                         {"x": ["expresso", "cappucino", "mocaccino", "cafe4"], "y": [7, 0, 3, 2], "type":"line", "name": "Cafés"}
                ],
                "layout": {
                    "title": "Sicrano"
                }
            })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
