from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)

# create a index site (home site)
@app.route('/')

def index():
    return "<h1> Hello World! </h1>"

# create some user sites
@app.route('/user/<name>')

def user(name):
    return "<h1> Hello {}! </h1>".format(name)

# create a site using render_template
@app.route('/site')

def site():
    return render_template("site1.html")

if __name__ == '__main__':
    app.run(debug=True)