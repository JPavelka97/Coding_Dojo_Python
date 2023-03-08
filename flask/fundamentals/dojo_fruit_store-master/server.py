from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    count = int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    print("Charging " + request.form['first_name'] + " " + request.form['last_name'] + " for " + str(count) + " fruits.")
    return render_template("checkout.html", fruit_amount = request.form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    