from flask import Flask, render_template, request
app = Flask(__name__)

     
@app.route('/')
def index():
    return "Index"

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return "You just submitted: " + request.form['username'] + "   " + request.form['password']
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

