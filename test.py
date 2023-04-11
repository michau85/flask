from flask import Flask, redirect, url_for,render_template
from example_blueprint import example_blueprint
from admin_blueprint import admin_blueprint
from blueprints.fol.fol_blueprint import fol_blueprint

app=Flask(__name__)
app.register_blueprint(example_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(fol_blueprint)

@app.route("/")
def home():
    return render_template('home.html',name="Mariusz", age=22)
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/<name>")
def name(name):
    return f'Hello {name}'

if __name__=="__main__":
    app.run(debug=True)