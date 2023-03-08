from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'greatnumbergame'
import random
x = random.randint(1, 100)

@app.route('/')
def random_number():
    print("Number is randomized:" + str(x))
    return render_template("index.html", x=x)

@app.route('/guess', methods=['GET','POST'])
def check_number():
    if x == int(request.form['guess']):
        session['color1'] = 'green'
        session['box_text'] = str(x) + " was the number!"
    else:
        session['color1'] = 'red'
        if int(request.form['guess']) < x:
            session['box_text'] = 'You were too low!'
        else:
            session['box_text'] = 'You were too high!'
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    