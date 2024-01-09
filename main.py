from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.express as px
import json

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv('templates/repos.csv')
    fig = px.bar(data, x='language', y='num_repos', title='Repository Count by Programming Language')
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', data=data.to_dict('records'), graph_json=graph_json)

if __name__ == '__main__':
    app.run(debug=True)
