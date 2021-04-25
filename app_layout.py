from dash.dependencies import Input, Output, State
import dash_html_components as html
import pandas as pd

from plots import dropdown_table, overview_plot
from utils import css_styles


def layout():
    return html.Div([
        html.H1("CRYPTO FLUCTUATION COMPARISON",
                style={**css_styles.font,
                       'text-align': 'center',
                       'background-color': '#E8E8E8',
                       "padding": "2.5rem 1rem",
                       }),
        html.Div("Compare trends and value in EUR of the crypto(s) you own ",
                 style={**css_styles.font,
                        'text-align': 'center',
                        'background-image': '#E8E8E8',
                        'padding': 0,
                        'font-size': 10,
                        'margin-top': '-70px',
                        'margin-bottom': '70px',
                        }),
        html.Div(dropdown_table.main()),
        html.Button('Add Currency',
                    id='editing-rows-button',
                    n_clicks=0,
                    style={**css_styles.button_style,
                           'background-color': 'white',
                           'border': '0.5px solid grey',
                           },
                    ),
        html.Button('Ready',
                    id='run_gecko',
                    n_clicks=0,
                    style={**css_styles.button_style,
                           'margin-top': '25px',
                           'float': 'right',
                           'width': '100%',
                           }),
        html.Div(id="line-chart",
                 style={**css_styles.font,
                        'margin-top': '50px',
                        }),
    ])


def callbacks(app):
    @app.callback(
        Output('table-dropdown', 'data'),
        Input('editing-rows-button', 'n_clicks'),
        State('table-dropdown', 'data'),
        State('table-dropdown', 'columns'))
    def add_row(n_clicks, rows, columns):
        if n_clicks > 0:
            rows.append({c['id']: '' for c in columns})
        return rows

    @app.callback(
        Output("line-chart", 'children'),
        Input('run_gecko', 'n_clicks'),
        State('table-dropdown', 'data'))
    def return_overview(n_clicks, data):
        if n_clicks > 0:
            df = pd.DataFrame.from_dict(data)
            try:
                return overview_plot.main(df['Currency'].tolist(), df['Date bought (d/m/Y)'].tolist(),
                                          df['Amount'].tolist())
            except ValueError:
                return "*Please make sure that all fields are filled and the date is valid and in the following " \
                       "format: d/m/Y "
        else:
            return
