# Import Supporting Libraries
import pandas as pd

# Import Dash Visualization Libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash.dependencies
from dash.dependencies import Input, Output, State
import plotly


# Load datasets
dadosClientes = 'https://raw.githubusercontent.com/grupoflux/dashboard/master/dadosClientes.csv'
df_dados = pd.read_csv(dadosClientes)
print(df_dados.head())

# Create our app layout
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H2('Clientes Club Apolo'),
    dt.DataTable(
        id='my-datatable',
        rows=df_dados.to_dict('records'),
        editable=False,
        row_selectable=False,
        filterable=True,
        sortable=True,
        selected_row_indices=[]
    )], 
    style={'width': '40%',
            'height': '40%',
            'margin-left': '10%',
            'margin-right': '10%'})

if __name__ == '__main__':
    app.run_server(debug=True)
