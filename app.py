from flask import Flask, render_template, request, flash


app = Flask(__name__)


@app.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form["name_input"]) + ", nice to meet you !")
    request.form['name_input']
    return render_template("index.html")


if __name__ == "__main__":
    app.secret_key = 'super Key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
