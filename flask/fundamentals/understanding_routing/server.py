from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', phrase="hello", times=5)

@app.route('/dojo')
def dojo():
    return "Dojo!"    

@app.route('/say/<name>')
def hi(name):
    return("Hi, " + str(name) + "!")

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    i = int(num)
    str = ""
    while i > 0:
        i = i-1
        str += word + "\n"
    return(str)

@app.errorhandler(404)
def page_not_found(empty):
    return("Sorry! No response. Try again")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.