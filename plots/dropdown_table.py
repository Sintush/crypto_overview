import dash_html_components as html
import dash_table
import pandas as pd

from utils import css_styles


def dummy_df():
    return pd.DataFrame(
        {
            'Date bought (d/m/Y)': ['1/1/2021'],
            'Currency': ['bitcoin'],
            'Amount': [1.11]
        }
    )


def crypto_table(df):
    return html.Div([
        html.Div('Owned Cryptos', style={**css_styles.font, 'margin-bottom': '25px'}),
        dash_table.DataTable(
            id='table-dropdown',
            data=df.to_dict('records'),
            columns=[
                {'id': 'Date bought (d/m/Y)', 'name': 'Date bought (d/m/Y)'},
                {'id': 'Currency', 'name': 'Currency', 'presentation': 'dropdown'},
                {'id': 'Amount', 'name': 'Amount', 'type': 'numeric'},
            ],

            editable=True,
            row_deletable=True,
            dropdown={
                'Currency': {
                    'options': [
                        {'label': i, 'value': i}
                        for i in ['bitcoin', 'aave', 'cardano', 'ethereum', 'polkadot', 'chainlink']
                    ]
                }
            },
            style_cell={**css_styles.font,
                        'textAlign': 'left',
                        'maxWidth': 0,
                        'fontSize': 14
                        },
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold'
            },
            style_as_list_view=True,
        )
    ])


def main():
    return crypto_table(dummy_df())
