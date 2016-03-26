from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/goodbye/")
def goodbye():
    return "Good bye!"

if __name__ == "__main__":
    # Set debug mode on
    app.debug = True

    # Start the app
    app.run()