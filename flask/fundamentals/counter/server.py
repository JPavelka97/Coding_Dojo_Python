from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'counters are fun'

@app.route('/')         
def index():
    if 'visit_num' in session:
        session['visit_num'] += 1
    else:
        session['visit_num'] = 0
    return render_template("index.html", visit_num=session['visit_num'])

@app.route('/add2')
def add2():
    if 'visit_num' in session:
        # Add 1 because the redirect will also add 1
        session['visit_num'] += 1
    else:
        session['visit_num'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/custom_incr', methods=['POST'])
def custom_incr():
    if 'visit_num' in session:
        session['visit_num'] += int(request.form['incr'])
    else:
        session['visit_num'] = 0
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    