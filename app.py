from flask import Flask , render_template , request

import marks as m


app = Flask(__name__)


"""
@app.route("/", methods = ["GET", "POST"] )
def marks():
    if request.method == "POST":
        hrs = request.form["hrs"]
        
        
    return render_template("index.html")"""



@app.route("/", methods = ["GET", "POST"])
def marks():
    # HTML -> py file
    if request.method == "POST":
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediction(hrs)

    # send data from py -> to HTML
    return render_template("index.html", n = marks_pred)



"""
@app.route("/sub", methods = ["POST"])
def submit():
    # HTML -> py file
    if request.method == "POST":
        name = request.form["username"]


    # send data from py -> to HTML
    return render_template("sub.html", n = name)
"""


if __name__ == "__main__":
    app.run(debug=True)