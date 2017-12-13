from flask import Flask, render_template,redirect,session,request
import random
app = Flask(__name__)
app.secret_key = "leprechaun"



@app.route('/')
def list():
    if 'yourgold' not in session:
        session ['yourgold'] = 0
    if 'yourActivity' not in session:
        session ['yourActivity'] = []

    return render_template('index.html')

    
@app.route('/process', methods = ['POST'])
def process():
    print request.form["location"]
    if request.form["location"] == 'Farm':
        goldEarned = random.randint(10, 20)
        session['yourgold'] += goldEarned
        message = 'Went to {} and earned {} Gold'.format(request.form['location'], goldEarned)
        session['yourActivity'].append(message)
        print message
    elif request.form["location"] == 'Cave':
        goldEarned = random.randint(5, 10)
        session['yourgold'] += goldEarned
        message = 'Went to {} and earned {} Gold'.format(request.form['location'], goldEarned)
        session['yourActivity'].append(message)
        print message   
    elif request.form["location"] == 'House':
        goldEarned = random.randint(2, 5)
        session['yourgold'] += goldEarned
        message = 'Went to {} and earned {} Gold'.format(request.form['location'], goldEarned)
        session['yourActivity'].append(message) 
        print message
    elif request.form["location"] == 'Casino':
        goldEarned = random.randint(-50, 50)
        session['yourgold'] += goldEarned
        if goldEarned > 0:
            winloose = 'earned'
        else:
            winloose = 'lost'
        message = 'Went to {} and {} {} gold'.format(request.form['location'], winloose, abs(goldEarned))
        session['yourActivity'].append(message)
        print message
        session['yourgold'] += goldEarned

    return redirect('/')



app.run(debug=True)