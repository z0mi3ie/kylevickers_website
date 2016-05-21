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
    # Create the pull request and display the string
    if request.method == 'POST':
        formatted_response = create_pull_request(
            summary=request.form['summary'],
            ticket=request.form['ticket'],
        )
        print('Formatted Response...')
        print(formatted_response)
        return render_template('pr.html', output=formatted_response)
    # Display the PR template
    if request.method == 'GET':
        return render_template('pull.html')


def create_pull_request(summary, ticket):
    pull_request_format = """
    # Summary
    {summary}

    # Ticket
    {ticket}
    """

    return pull_request_format.format(summary=summary, ticket=ticket)

# Start the debug server
if __name__ == "__main__":
    # Set debug mode on
    app.debug = True
    log.debug('new message')

    # Start the app
    app.run()
