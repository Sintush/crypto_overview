import plotly.express as px
from utils import get_coin_gecko
import dash_html_components as html
import dash_core_components as dcc

from utils import css_styles


def currency_chart(df):
    fig = px.line(df,
                  x="Date",
                  y="Price",
                  color='Crypto',
                  color_discrete_sequence=px.colors.sequential.RdBu,
                  )

    fig.update_layout(
        font_family=css_styles.font['font-family'],
        plot_bgcolor='white',
    )

    return fig


def chart_to_html(fig):
    return html.Div([
        dcc.Graph(figure=fig),
    ])


def main(crypto, from_date, amount):
    prices_by_date = get_coin_gecko.get_prices(crypto, from_date, amount)
    fig = currency_chart(prices_by_date)
    return chart_to_html(fig)
