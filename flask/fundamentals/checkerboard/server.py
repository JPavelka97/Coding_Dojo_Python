from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard_template():
    return render_template('index.html')

@app.route('/<int:row>')
@app.route('/<int:row>/<int:col>')
@app.route('/<int:row>/<int:col>/<color1>')
@app.route('/<int:row>/<int:col>/<color1>/<color2>')
def checkerboard_rows(row, col=8, color1='red', color2='black'):
    return render_template('index.html', rows=row, cols=col, color1=color1, color2=color2)
    
if __name__=="__main__":
    app.run(debug=True)