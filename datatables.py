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
US_STATES_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
US_AG_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv'
df_st = pd.read_csv(US_STATES_URL)
df_ag = pd.read_csv(US_AG_URL)
print(df_st.head())
print(df_ag.head())

# Create our app layout
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H2('My Dash App'),
    dt.DataTable(
        id='my-datatable',
        rows=df_ag.to_dict('records'),
        editable=False,
        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[]
    )], 
    style={'width': '75%',
            'margin-left': '10%',
            'margin-right': '10%'})

if __name__ == '__main__':
    app.run_server(debug=True)
