from flask import Flask, render_template, request, redirect
import requests
import pandas as pd

from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
    return redirect('/userform')

@app.route('/userform',methods=['GET'])
def userstockform():
    return render_template('userstockform.html')

@app.route('/results',methods=['POST'])
def stockresults():

    # Read user input from form
    tickersymbol = request.form['tickersymbol']

    # Get data and create dataframe
    dataurl = 'https://www.quandl.com/api/v3/datasets/WIKI/' + tickersymbol + '.json'
    r = requests.get(dataurl)
    dataset_df = pd.DataFrame(r.json())['dataset'].apply(pd.Series)
    data = dataset_df.ix['data',:].apply(pd.Series)
    data.columns = dataset_df.ix['column_names',0:12]
    data['Date'] = pd.to_datetime(data['Date'])

    p = figure(title=tickersymbol)
    p.line(data['Date'],data['Open'])

    script, div = components(p)

    return render_template('results.html',tickersymbol=tickersymbol, script=script, div=div)



if __name__ == '__main__':
    app.run(port=33507,debug=True)
