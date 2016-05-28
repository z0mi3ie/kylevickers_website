# Native imports
import logging

# 3rd Party imports
from flask import Flask
from flask import render_template
from flask import request

# Logging setup
log = logging.getLogger('werkzeug')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pull", methods=['POST', 'GET'])
def pull():
    # Create the pull request
    if request.method == 'POST':
        return render_template('pr.html',
                ticket_number=request.form['ticket_number'],
                ticket_title=request.form['ticket_title'],
                ticket_url=request.form['ticket_url'],
                summary=request.form['summary'],
                review_a=request.form['review_a'],
                review_b=request.form['review_b'],
                setup=request.form['setup'],
                test=request.form['test'],
                verify=request.form['verify'],
        )

    # Display the PR template
    if request.method == 'GET':
        return render_template('pull.html')

# Start the debug server
if __name__ == "__main__":
    # Set debug mode on
    app.debug = True
    log.debug('new message')

    # Start the app
    app.run()
