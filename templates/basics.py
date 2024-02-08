from flask import Flask, render_template

app = Flask(_name_)


@app.route('/home')
def home():
    return render_template('home.html')

if _name_ == "_main_":
    app.run(debug=True)