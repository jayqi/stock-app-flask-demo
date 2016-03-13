from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/userform')

@app.route('/userform',methods=['GET','POST'])
def userstockform():
    if request.method == 'GET':
        return render_template('userstockform.html')
    else:
        print 'boo'
        app.vars['tickersymbol'] = request.form['tickersymbol']
        print 'hoo'
        print request.form
        print app.vars

        return render_template('results.html',tickersymbol=app.vars['tickersymbol'])


if __name__ == '__main__':
  app.run(port=33507,debug=True)
