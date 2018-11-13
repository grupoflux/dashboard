#pip install dash dash-renderer dash-html-components dash-core-components plotly

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Consumo Jornada do Usuário"),

    dcc.Graph(id = "TendênciaVendas",
    figure = {
        "data": [{"labels": ["Cerveja", "cafe", "hamburguer", "nhoque", "suco"], "values": [300, 200, 59, 23, 14], "type":"pie", "name":"tendências"}
        ],
        "layout":{
            "title":"Tendências de consumo"
        }
    }),

    dcc.Graph(id = "CadastroPlataforma",
    figure = {
        "data": [{"x": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"], "y": [2,7,5,5,9,8], "type": "line", "name": "Realizaram cadastro"},
                 {"x": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"], "y": [1,9,2,4,8,2], "type": "line", "name": "Não terminaram cadastro"}
        ],
        "layout":{
            "title": "Cadastro de usuários"
        }
    }),

    dcc.Graph(id = "HabitosConsumo",
    figure = {
        "data": [{"x": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"], "y":[49, 78, 32, 50, 45, 70], "type": "bar", "name": "Cervejas"},
                 {"x": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"], "y":[31, 35, 56, 60, 21, 47], "type": "bar", "name": "Cafés"}
        ],
        "layout":{
            "title":"Hábitos de consumo"
        }
    }),

    html.H1("Experiência dos Clientes"),

    dcc.Graph(id = "VisitaApolo",
    figure = {
        "data": [{"x": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab"], "y": [22, 15, 26, 32, 89, 42], "type": "bar", "name": "Cliente Club Apolo"}
        ],
        "layout":{
            "title": "Visita ao Apolo"
        }
    }),

])
if __name__ == '__main__':
    app.run_server(debug=True)
