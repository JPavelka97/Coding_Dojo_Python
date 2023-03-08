from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def boxes():
    return render_template('index.html', times=3)

@app.route('/play/<x>')
def boxes_variable(x):
    return render_template('index.html', times=int(x))

@app.route('/play/<x>/<color>')
def boxes_variable_color(x, color):
    return render_template('index.html', times=int(x), color=color)

if __name__=="__main__":
    app.run(debug=True)