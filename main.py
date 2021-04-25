import dash
import app_layout


app = dash.Dash(__name__)

app.layout = app_layout.layout()

app_layout.callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
